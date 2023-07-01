import json
import os

from src.settings.builder import BotSettingsManager
import configparser

from src.settings.language import Language, get_language_from_code

def set_language_to_config(chat_id: int, language: str):
    config = configparser.ConfigParser()

    # Read the existing config.ini file
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config/chats.ini')
    config.read(initfile)

    # Set the language value for the specific chat_id
    if not config.has_section(str(chat_id)):
        config.add_section(str(chat_id))
    config.set(str(chat_id), 'language', language)

    # Write the updated configuration to the config.ini file
    with open(initfile, 'w') as configfile:
        config.write(configfile)

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
            set_language_to_config(chat_id, lang)
            return Language(langauge)
    except:
        set_language_to_config(chat_id, lang)
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


def get_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the config.ini file
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'config/config.ini')
    config.read(initfile)

    api_key = config.get('API', 'APIKey')
    return api_key

def load_phrases(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_settings(chat_id: int):
    manager = BotSettingsManager()

    # Retrieve the language from the chat_id
    language_code = get_language_by_chat_id(chat_id)
    # Set the language and API key in the manager
    return manager.setLanguage(language_code).setApiKey(get_config())

def set_settings(chat_id: int, language: str):
    manager = BotSettingsManager()

    # Set the language and API key in the manager
    return manager.setLanguage(set_language_by_chat_id(chat_id, language)).setApiKey(get_config())

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
        set_settings(chat_id, 'uk')
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
    return manager.setLanguage(Language.UKRAINIAN).setApiKey(get_config())

