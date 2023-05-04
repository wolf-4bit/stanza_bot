import aiosqlite
from common import classes

class DatabaseClient(aiosqlite,metaclass=classes.Singleton):
    ...
    
