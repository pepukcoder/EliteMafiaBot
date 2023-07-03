import json
import os

from src.settings.builder import BotSettings

from src.settings.exceptions.ConfigOptionNotFoundError import ConfigOptionNotFoundError
from src.settings.managers.lang_chat_config_manager import LangChatConfigManager
from src.settings.managers.mafia_chat_config_manager import MafiaChatConfigManager


# def get_api_key():
#     # Create a ConfigParser object
#     config = configparser.ConfigParser()
#
#     # Read the config.ini file
#     thisfolder = os.path.dirname(os.path.abspath(__file__))
#     initfile = os.path.join(thisfolder, 'config/config.ini')
#     config.read(initfile)
#
#     api_key = config.get('API', 'APIKey')
#     return api_key


def load_phrases(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        return json.load(file)


def get_settings(chat_id: int) -> BotSettings:
    language = LangChatConfigManager.get_language_from_config(chat_id)
    mafia = MafiaChatConfigManager.get_mafia_from_config(chat_id)

    return BotSettings(language, mafia)


def set_settings(chat_id: int, language: str, mafia: str) -> None:
    LangChatConfigManager.set_language_to_config(chat_id, language)
    MafiaChatConfigManager.set_mafia_to_config(chat_id, mafia)


def get_language(chat_id: int):
    def handle(settings: BotSettings):
        language = settings.language

        this_folder = os.path.dirname(os.path.abspath(__file__))
        jsons = this_folder + '/phrases/{}.json'

        phrases_file_path = jsons.format(language.value)
        phrases = load_phrases(phrases_file_path)
        return phrases

    try:
        settings = get_settings(chat_id)
        return handle(settings)

    except ConfigOptionNotFoundError:
        set_settings(chat_id, 'en', '1to3')
        settings = get_settings(chat_id)
        return handle(settings)
