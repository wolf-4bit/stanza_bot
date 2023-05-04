import discord
from common import constant
from utility import sheet
import traceback
from utility import database
from common import classes


class VerificationButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Confirm",
        style=discord.ButtonStyle.green,
        emoji="✅",
        custom_id="VButtonConfirm",
    )
    async def confirm(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(VerificationModal(timeout=10))


class VerificationModal(discord.ui.Modal, title="Enter you Stanza ID!"):
    stanzaid: discord.ui.TextInput = discord.ui.TextInput(
        label="Stanza User ID",
        placeholder="Enter your Stanza ID here",
        required=True,
        style=discord.TextStyle.short,
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        record: str | None = sheet.ClientSheet().get_values().get(self.stanzaid.value)
        if record == None:
            await interaction.response.send_message(
                "Unable to find your ID", ephemeral=True
            )
            self.stop()
            return
        value = await database.check_for_verified_data(
            stanza_id=self.stanzaid.value,
            discord_id= interaction.user.id
        )
        if value is classes.DatabaseCodes.DATA_WITH_STANZA_ID:
            await interaction.response.send_message(
                "This Stanza ID is already linked with another account, please contact moderator for further info!", ephemeral=True
            )
            self.stop()
            return
        if value is classes.DatabaseCodes.DATA_WITH_DISCORD_ID:
            await interaction.response.send_message(
                "This Discord ID is already linked with another account, please enter valid stanza ID or contact moderator for further info!", ephemeral=True
            )
            self.stop()
            return
        if value is classes.DatabaseCodes.NO_DATA:
            await database.insert_verified_data(
                stanza_id=self.stanzaid.value,
                discord_id=interaction.user.id,
                gender=record.upper(),
                verified=True,
            )
        if record.upper() == "FEMALE":
            role = interaction.guild.get_role(constant.BOT_GENDER_ROLE_ID)
            await interaction.user.add_roles(role, reason="Added by Bot verification")
        await interaction.response.send_message("Verified your entry!", ephemeral=True)
        self.stop()

    async def on_error(
        self, interaction: discord.Interaction, error: Exception
    ) -> None:
        await interaction.response.send_message(
            "Error occured! Please contact moderator for futher help!", ephemeral=True
        )
        traceback.print_exception(type(error), error, error.__traceback__)
