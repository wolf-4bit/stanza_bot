import enum


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseCodes(enum.Enum):
    NO_DATA = 1
    DATA_WITH_STANZA_ID = 2
    DATA_WITH_DISCORD_ID = 3
    DATA_WITH_BOTH = 4
