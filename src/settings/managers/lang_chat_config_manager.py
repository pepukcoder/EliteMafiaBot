from src.settings.exceptions.ConfigOptionNotFoundError import ConfigOptionNotFoundError
from src.settings.language import Language
from src.settings.managers.chat_config_manager import ChatConfigManager


class LangChatConfigManager(ChatConfigManager):
    @classmethod
    def set_language_to_config(cls, chat_id: int, language: str) -> None:
        config = super(cls, cls).get_config_by_chat_id(chat_id)

        # Check if this language already had set
        if config.has_option(str(chat_id), 'language'):
            if config.get(str(chat_id), 'language') == language:
                return

        config.set(str(chat_id), 'language', language)

        # Write the updated configuration to the config.ini file
        init_file = super(cls, cls).get_init_file()
        with open(init_file, 'w', encoding="utf8") as configfile:
            config.write(configfile)

    @classmethod
    def get_language_from_config(cls, chat_id: int) -> Language:
        config = super(cls, cls).get_config_by_chat_id(chat_id)

        if config.has_option(str(chat_id), 'language'):
            langauge = config.get(str(chat_id), 'language')
            return Language(langauge)
        else:
            raise ConfigOptionNotFoundError("Option language for chat_id not found", chat_id)
