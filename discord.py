
import discord
from discord.ext import commands 

# Initializes the bots intents and access to content
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
