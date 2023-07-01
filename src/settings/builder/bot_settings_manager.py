from src.settings.builder import BotSettingsBuilder


class BotSettingsManager:
    def __init__(self):
        self.builder = BotSettingsBuilder()

    def setLanguage(self, language):
        self.builder.setLanguage(language)
        return self

    def setApiKey(self, api_key):
        self.builder.setApiKey(api_key)
        return self

    def getSettings(self):
        return self.builder.build()