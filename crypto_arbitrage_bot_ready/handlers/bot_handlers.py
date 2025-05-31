from telegram import Update
from telegram.ext import ContextTypes
from core.trading import toggle_trade, TRADE_ENABLED

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот запущен. /toggle_trade для вкл/выкл торговли.")

async def toggle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if toggle_trade():
        await update.message.reply_text("Автоторговля включена.")
    else:
        await update.message.reply_text("Автоторговля выключена.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Торговля сейчас: {'ON' if TRADE_ENABLED else 'OFF'}")