from classifier import intencoes as _intencoes
from classifier import make_prediction
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = """Comandos disponíveis:
- /help -> exibe uma mensagem de ajuda.
"""
    await update.message.reply_text(msg)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intencoes = ", ".join(_intencoes)
    await update.message.reply_text(
        f"Esta rede neural foi treinada para detectar as seguintes intenções: {intencoes}."  # noqa: E501
    )

    await update.message.reply_text(
        "Envie uma mensagem e tentarei descobrir qual a sua intenção!"
    )


async def classify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intencao = make_prediction(update.message.text)

    await update.message.reply_text(f"Você quer {intencao}")


handle_start = CommandHandler("start", start)
handle_help = CommandHandler("help", help)
handle_classify = MessageHandler(filters.CHAT & ~filters.COMMAND, classify)
