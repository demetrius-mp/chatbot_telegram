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

    if intencao == "ver_cardapio":
        await update.message.reply_text("Certo, você quer o cardápio.")
        await update.message.reply_text(
            "No momento não consigo te enviar o cardápio, mas se quiser, pode fazer seu pedido e eu te digo se temos em estoque ou não."  # noqa
        )

    if intencao == "fazer_pedido":
        await update.message.reply_text("Opa, parece que você quer fazer seu pedido.")
        await update.message.reply_text(
            "Estarei encaminhando os itens do seu pedido para um de nossos colaboradores."  # noqa
        )

    if intencao == "fechar_conta":
        await update.message.reply_text("Beleza, vamos fechar a sua conta então.")
        await update.message.reply_text("O valor total da sua conta foi de 0.007 BTC.")
        await update.message.reply_text("Agradecemos sua atenção, até a proxima!")


handle_start = CommandHandler("start", start)
handle_help = CommandHandler("help", help)
handle_classify = MessageHandler(filters.CHAT & ~filters.COMMAND, classify)
