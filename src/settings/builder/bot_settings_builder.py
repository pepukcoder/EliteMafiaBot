import configparser

from src.settings.builder import BotSettings


class BotSettingsBuilder:
    def __init__(self):
        self.settings = BotSettings()

    def setLanguage(self, language):
        self.settings.language = language
        return self

    def setMafia(self, quantity):
        self.settings.mafia = quantity
        return self

    def setApiKey(self, api_key):
        self.settings.api_key = api_key
        return self

    def build(self):
        return self.settings
