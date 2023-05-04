from common import helper
from utility import sheet
import os
from discord.ext import tasks
from view import verification
import common.constant as constant
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix=constant.BOT_PREFIX, intents=constant.BOT_INTENTS)

commands_list = helper.find_py_files("src/commands")
event_list = helper.find_py_files("src/events")


@tasks.loop(minutes=10)  
async def sheet_update_task():
    sheet.ClientSheet().update_values()

@bot.event
async def on_ready():
    await helper.load_extensions(bot, cogs = commands_list + event_list)
    sheet_update_task.start()
    bot.add_view(verification.VerificationButton())

if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))