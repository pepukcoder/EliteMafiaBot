from configparser import ConfigParser
import os


class ChatConfigManager:
    @classmethod
    def get_init_file(cls) -> str:
        settings_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        init_file = os.path.join(settings_folder, 'config/chats.ini')

        return init_file

    @classmethod
    def get_config_by_chat_id(cls, chat_id) -> ConfigParser:
        config = ConfigParser()

        # Read the existing config.ini file
        init_file = cls.get_init_file()
        config.read(init_file)

        # Set the section for the specific chat_id
        if not config.has_section(str(chat_id)):
            config.add_section(str(chat_id))

        return config
