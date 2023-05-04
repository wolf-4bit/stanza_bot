import aiosqlite
import enum
from common import classes


async def create_table_guard() -> None:
    async with aiosqlite.connect("database.db") as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS users (discord_id BIGINT, stanza_id MEDIUMTEXT, gender TINYTEXT, verified BOOLEAN)"
        )
        await db.commit()


async def insert_verified_data(
    discord_id: int, stanza_id: str, gender: str, verified: bool
) -> None:
    async with aiosqlite.connect("database.db") as db:
        data = (discord_id, stanza_id, gender, verified)
        await db.execute(
            "INSERT INTO users (discord_id, stanza_id, gender, verified) VALUES (?, ?, ?, ?)",
            data,
        )
        await db.commit()


async def check_for_verified_data(stanza_id: str, discord_id: str) -> any:
    async with aiosqlite.connect("database.db") as db:
        result = await db.execute(
            "SELECT * FROM users WHERE stanza_id = ? OR discord_id = ?",
            (stanza_id, discord_id),
        )
        row = await result.fetchone()
        if row is None:
            return classes.DatabaseCodes.NO_DATA
        elif row[1] == stanza_id:
            return classes.DatabaseCodes.DATA_WITH_STANZA_ID
        elif row[0] == discord_id:
            return classes.DatabaseCodes.DATA_WITH_DISCORD_ID
        else:
            return classes.DatabaseCodes.DATA_WITH_BOTH
