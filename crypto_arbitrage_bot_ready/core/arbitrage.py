import asyncio, os, math, logging
from .logger import logger
from .risk_ai import ai_risk_check

MIN_SPREAD_PCT = float(os.getenv("MIN_SPREAD_PCT", "2"))

async def get_price(exchange, symbol):
    ticker = await exchange.fetch_ticker(symbol)
    return ticker['last']

async def check_spread(ex1, ex2, symbol):
    p1, p2 = await asyncio.gather(get_price(ex1, symbol), get_price(ex2, symbol))
    spread = abs(p1 - p2) / ((p1 + p2) / 2) * 100
    return spread, p1, p2

async def scan_pairs(exchanges, symbols):
    alerts = []
    keys = list(exchanges.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            ex_a = exchanges[keys[i]]
            ex_b = exchanges[keys[j]]
            for sym in symbols:
                try:
                    spread, pa, pb = await check_spread(ex_a, ex_b, sym)
                    if spread >= MIN_SPREAD_PCT:
                        text = (f"Spread {spread:.2f}% for {sym} between {keys[i]} ({pa}) and {keys[j]} ({pb})")
                        safe = await ai_risk_check(text)
                        if safe:
                            alerts.append(text)
                            logger.info(text)
                        else:
                            logger.info("AI blocked trade: " + text)
                except Exception as e:
                    logger.warning(f"Error for {sym}: {e}")
    return alerts