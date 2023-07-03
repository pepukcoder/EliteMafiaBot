from src.settings.language import Language
from src.settings.mafia import Mafia


class BotSettings:
    def __init__(self, language: Language = Language.UKRAINIAN, mafia: Mafia = Mafia.M1FOR3):
        self.language: Language = language
        self.mafia: Mafia = mafia
