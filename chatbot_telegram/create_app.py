from handlers import handle_classify, handle_help, handle_start
from settings import get_settings
from telegram.ext import ApplicationBuilder

settings = get_settings()


def create_app():
    token = settings.telegram_bot_token
    app = ApplicationBuilder().token(token).build()

    app.add_handler(handle_start)
    app.add_handler(handle_help)
    app.add_handler(handle_classify)

    return app
