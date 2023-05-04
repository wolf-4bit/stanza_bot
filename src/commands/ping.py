from discord.ext import commands
import discord

class Ping(commands.Cog):

    def __init__(self, bot: discord.Client):
        self.bot = bot 

    @commands.command()
    async def ping(self, ctx):
         await ctx.send(f'Pong! In {round(self.bot.latency * 1000)}ms')
         
async def setup(bot):
        await bot.add_cog(Ping(bot))