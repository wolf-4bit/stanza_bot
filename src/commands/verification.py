from discord.ext import commands
import discord
from view import verification

class Setup(commands.Cog):

    def __init__(self, bot: discord.Client):
        self.bot = bot 

    @commands.command()
    async def set_verify(self, ctx):
        embed = discord.Embed(
            color=discord.Color.blue(),
            title="Stanza Verification!",
            description="Please click here to verify yourself",
        )
        await ctx.send(embed=embed, view=verification.VerificationButton())
         
async def setup(bot):
        await bot.add_cog(Setup(bot))