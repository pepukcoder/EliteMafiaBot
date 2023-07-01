import enum


class Language(enum.Enum):
    RUSSIAN = 'ru'
    RUSSIAN_MOD = 'ru_mod'
    UKRAINIAN = 'uk'
    ENGLISH = 'en'


def get_language_from_code(language_code):
    for lang in Language:
        if lang.value == language_code:
            return lang
    return None
