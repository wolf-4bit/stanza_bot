from common import helper
from utility import sheet
import os
import aiosqlite
import asyncio
from discord.ext import tasks
from view import verification
import logging
import logging.handlers
import common.constant as constant
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


commands_list = helper.find_py_files("src/commands")
event_list = helper.find_py_files("src/events")


# Tasks
@tasks.loop(minutes=10)
async def sheet_update_task():
    sheet.ClientSheet().update_values()


# Class delcaration
class CustomBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=constant.BOT_PREFIX, intents=constant.BOT_INTENTS
        )

    async def setup_hook(self) -> None:
        for cog in commands_list + event_list:
            await self.load_extension(cog)
        sheet_update_task.start()
        self.add_view(verification.VerificationButton())


async def main():
    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename="discord.log",
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,
        backupCount=5,
    )
    dt_fmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(
        "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    bot = CustomBot()
    await bot.start(os.getenv("BOT_TOKEN"))


if __name__ == "__main__":
    asyncio.run(main())
