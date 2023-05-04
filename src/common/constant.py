import discord

BOT_PREFIX = ".."
BOT_INTENTS = discord.Intents.all()
GSPREAD_SHEET_NAME = "Stanza-Database"
GSPREAD_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
GSPREAD_CELL_REFERENCE = "A2:B"
BOT_GENDER_ROLE_ID = 1103599030036082739
BOT_VERIFED_ROLE_ID = 1103599030036082739
