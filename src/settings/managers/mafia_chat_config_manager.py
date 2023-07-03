from src.settings.exceptions.ConfigOptionNotFoundError import ConfigOptionNotFoundError
from src.settings.mafia import Mafia
from src.settings.managers.chat_config_manager import ChatConfigManager


class MafiaChatConfigManager(ChatConfigManager):
    @classmethod
    def set_mafia_to_config(cls, chat_id: int, quantity: str) -> None:
        config = super(cls, cls).get_config_by_chat_id(chat_id)

        if config.has_option(str(chat_id), 'mafia'):
            if config.get(str(chat_id), 'mafia') == str(quantity):
                return

        config.set(str(chat_id), 'mafia', str(quantity))

        # Write the updated configuration to the config.ini file
        init_file = super(cls, cls).get_init_file()
        with open(init_file, 'w', encoding="utf8") as configfile:
            config.write(configfile)

    @classmethod
    def get_mafia_from_config(cls, chat_id: int) -> Mafia:
        config = super(cls, cls).get_config_by_chat_id(chat_id)

        if config.has_option(str(chat_id), 'mafia'):
            mafia = config.get(str(chat_id), 'mafia')
            return Mafia(mafia)
        else:
            raise ConfigOptionNotFoundError("Option mafia for chat_id not found", chat_id)
