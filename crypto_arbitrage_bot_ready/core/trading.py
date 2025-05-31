import logging
TRADE_ENABLED = False
logger = logging.getLogger("arb_bot")

def toggle_trade():
    global TRADE_ENABLED
    TRADE_ENABLED = not TRADE_ENABLED
    logger.info(f'Trade enabled: {TRADE_ENABLED}')
    return TRADE_ENABLED