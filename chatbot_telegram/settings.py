import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    telegram_bot_token: str


@lru_cache
def get_settings():
    telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")

    if not telegram_bot_token:
        raise ValueError("Must set environment variable TELEGRAM_BOT_TOKEN.")

    settings = Settings(
        telegram_bot_token=telegram_bot_token,
    )

    return settings
