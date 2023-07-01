from os import environ
from typing import Final

from src.settings.main import get_default_settings

settings = get_default_settings()
retrieved_settings = settings.getSettings()


class TgKeys:
    TOKEN: Final = environ.get('TOKEN', retrieved_settings.api_key)
