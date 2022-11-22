from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = """Comandos disponíveis:
- /help -> exibe uma mensagem de ajuda.
"""
    await update.message.reply_text(msg)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ajuda.")


async def classify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá, mundo!")


handle_start = CommandHandler("start", start)
handle_help = CommandHandler("help", help)
handle_classify = MessageHandler(filters.PHOTO & ~filters.COMMAND, classify)
