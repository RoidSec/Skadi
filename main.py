import os
import config
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print('Skadi Bot online, loading Cogs...')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
        
async def main():
    await load()
    load_dotenv()
    token = os.getenv("discord_token")
    await bot.start(token)

asyncio.run(main())