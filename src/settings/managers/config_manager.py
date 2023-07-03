from configparser import ConfigParser
import os


class ConfigManager:
    @classmethod
    def __get_init_file(cls) -> str:
        settings_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        init_file = os.path.join(settings_folder, 'config/chats.ini')

        return init_file

    @classmethod
    def __get_config_by_chat_id(cls, chat_id) -> ConfigParser:
        config = ConfigParser()

        # Read the existing config.ini file
        init_file = cls.__get_init_file()
        config.read(init_file)

        # Set the section for the specific chat_id
        if not config.has_section(str(chat_id)):
            config.add_section(str(chat_id))

        return config

    @classmethod
    def set_language_to_config(cls, chat_id: int, language: str) -> None:
        config = cls.__get_config_by_chat_id(chat_id)
        config.set(str(chat_id), 'language', language)

        # Write the updated configuration to the config.ini file
        init_file = cls.__get_init_file()
        with open(init_file, 'w', encoding="utf8") as configfile:
            config.write(configfile)

    @classmethod
    def set_mafia_to_config(cls, chat_id: int, quantity: str):
        config = cls.__get_config_by_chat_id(chat_id)
        config.set(str(chat_id), 'mafia', str(quantity))

        # Write the updated configuration to the config.ini file
        init_file = cls.__get_init_file()
        with open(init_file, 'w', encoding="utf8") as configfile:
            config.write(configfile)
