from src.settings.language import Language
from src.settings.mafia import Mafia


class BotSettings:
    def __init__(self):
        self.language = Language.UKRAINIAN
        self.mafia = Mafia.M1FOR3
        self.api_key = ""
