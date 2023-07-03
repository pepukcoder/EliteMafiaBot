import json
import os

from src.settings.builder import BotSettingsManager
import configparser

from src.settings.language import Language
from src.settings.mafia import Mafia
from src.settings.managers.config_manager import ConfigManager


def set_language_by_chat_id(chat_id: int, lang: str):
    config = configparser.ConfigParser()

    # Read the config.ini file
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config/chats.ini')
    config.read(initfile)

    try:
        langauge = config.get(str(chat_id), 'language')
        if lang == langauge:
            return Language(langauge)
        else:
            ConfigManager.set_language_to_config(chat_id, lang)
            return Language(langauge)
    except:
        ConfigManager.set_language_to_config(chat_id, lang)
        config.read(initfile)
        langauge = config.get(str(chat_id), 'language')
        return Language(langauge)

def get_language_by_chat_id(chat_id: int):
    config = configparser.ConfigParser()

    # Read the config.ini file
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config/chats.ini')
    config.read(initfile)

    langauge = config.get(str(chat_id), 'language')
    return Language(langauge)

def set_mafia_by_chat_id(chat_id: int, maf: str):
    config = configparser.ConfigParser()

    # Read the config.ini file
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config/chats.ini')
    config.read(initfile)

    try:
        mafia = config.get(str(chat_id), 'mafia')
        if maf == mafia:
            return mafia
        else:
            ConfigManager.set_mafia_to_config(chat_id, maf)
            return mafia
    except:
        ConfigManager.set_mafia_to_config(chat_id, maf)
        config.read(initfile)
        mafia = config.get(str(chat_id), 'mafia')
        return mafia

def get_mafia_by_chat_id(chat_id: int):
    config = configparser.ConfigParser()

    # Read the config.ini file
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config/chats.ini')
    config.read(initfile)

    mafia = config.get(str(chat_id), 'mafia')
    return mafia

def get_api_key():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the config.ini file
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config/config.ini')
    config.read(initfile)

    api_key = config.get('API', 'APIKey')
    return api_key

def load_phrases(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        return json.load(file)

def get_settings(chat_id: int):
    manager = BotSettingsManager()

    # Retrieve the language from the chat_id
    language_code = get_language_by_chat_id(chat_id)
    mafia = get_mafia_by_chat_id(chat_id)
    # Set the language and API key in the manager
    return manager.setLanguage(language_code).setMafia(mafia).setApiKey(get_api_key())

def set_settings(chat_id: int, language: str, mafia: str):
    manager = BotSettingsManager()

    # Set the language and API key in the manager
    return manager.setLanguage(set_language_by_chat_id(chat_id, language))\
        .setMafia(set_mafia_by_chat_id(chat_id, mafia))\
        .setApiKey(get_api_key())

def get_language(chat_id: int):
    try:
        settings = get_settings(chat_id)
        retrieved_settings = settings.getSettings()
        retrieved_language = retrieved_settings.language

        thisfolder = os.path.dirname(os.path.abspath(__file__))
        jsons = thisfolder + '/phrases/{}.json'

        phrases_file_path = jsons.format(retrieved_language.value)
        phrases = load_phrases(phrases_file_path)
        return phrases
    except:
        set_settings(chat_id, 'en', '1to3')
        settings = get_settings(chat_id)
        retrieved_settings = settings.getSettings()
        retrieved_language = retrieved_settings.language

        thisfolder = os.path.dirname(os.path.abspath(__file__))
        jsons = thisfolder + '/phrases/{}.json'

        phrases_file_path = jsons.format(retrieved_language.value)
        phrases = load_phrases(phrases_file_path)
        return phrases

def get_default_settings():
    manager = BotSettingsManager()

    # Set the language and API key in the manager
    return manager.setLanguage(Language.ENGLISH).setMafia(Mafia.M1FOR3).setApiKey(get_api_key())

