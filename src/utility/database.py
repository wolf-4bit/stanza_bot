import aiosqlite


async def insert_verified_data(
    discord_id: int, stanza_id: str, gender: str, verified: bool
):
    async with aiosqlite.connect("database.db") as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS users (discord_id BIGINT stanza_id MEDIUMTEXT gender TINYTEXT verified BOOLEAN)"
        )

        data = (discord_id,stanza_id, gender, verified)
        await db.execute(
            "INSERT INTO users (discord_id, stanza_id, gender, verified) VALUES (?, ?, ?, ?)", data
        )
        await db.commit()

async def check_for_verified_data(
    stanza_id: str
):
    async with aiosqlite.connect("database.db") as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS users (discord_id BIGINT stanza_id MEDIUMTEXT gender TINYTEXT verified BOOLEAN)"
        )

        data = (stanza_id)
        await db.execute(
            "INSERT INTO users (id, name, verified) VALUES (?, ?, ?, ?)", data
        )
        await db.commit()
