import discord
from common import constant
from utility import sheet
import traceback

class VerificationButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green, emoji="✅",custom_id="VButtonConfirm")
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(VerificationModal(timeout=10))

class VerificationModal(discord.ui.Modal, title='Enter you Stanza ID!'):
    name: discord.ui.TextInput = discord.ui.TextInput(
        label='Stanza User ID',
        placeholder='Enter your Stanza ID here',
        required=True,
        style=discord.TextStyle.short
    )
    async def on_submit(self, interaction: discord.Interaction) -> None:
        record: str | None = sheet.ClientSheet().get_values().get(self.name.value)
        if(record == None):
            await interaction.response.send_message("Unable to find your ID")
            self.stop()
            return
        if record.upper() == "FEMALE":
            role = await interaction.guild.get_role(constant.BOT_GENDER_ROLE_ID)
            await interaction.user.add_roles(role,reason="Added by Bot verification")
        await interaction.response.send_message("Verified!", ephemeral=True)
        self.stop()
        
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Error occured! Please contact moderator for futher help!', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)