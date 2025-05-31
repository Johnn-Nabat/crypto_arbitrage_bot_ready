import os, asyncio, uvloop
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from core.exchanges import ExchangeFactory
from core.arbitrage import scan_pairs
from core.logger import logger
from handlers.bot_handlers import start, toggle, status

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SYMBOLS = ["BTC/USDT", "ETH/USDT"]

exchange_creds = {
    "kucoin": {
        "api_key": os.getenv("KUCOIN_API_KEY"),
        "api_secret": os.getenv("KUCOIN_API_SECRET"),
        "passphrase": os.getenv("KUCOIN_API_PASSPHRASE"),
    },
    "bybit": {
        "api_key": os.getenv("BYBIT_API_KEY"),
        "api_secret": os.getenv("BYBIT_API_SECRET"),
    },
    "mexc": {
        "api_key": os.getenv("MEXC_API_KEY"),
        "api_secret": os.getenv("MEXC_API_SECRET"),
    },
}

async def main():
    exchanges = {name: ExchangeFactory.create(name, creds) for name, creds in exchange_creds.items()}
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("toggle_trade", toggle))
    app.add_handler(CommandHandler("status", status))

    async def loop():
        while True:
            alerts = await scan_pairs(exchanges, SYMBOLS)
            for msg in alerts:
                await app.bot.send_message(chat_id=os.getenv("OWNER_CHAT_ID"), text=msg)
            await asyncio.sleep(10)

    app.create_task(loop())
    logger.info("Bot started")
    await app.run_polling()

if __name__ == "__main__":
    uvloop.install()
    asyncio.run(main())