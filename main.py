import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

#intents
client = commands.Bot(command_prefix="/", intents = discord.Intents.all())
intents = discord.Intents.all()
intents.message_content = True
intents.members = True

#login & sync commands
@client.event
async def on_ready():
    print(f"{client.user.name} is logged in.")
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

#loading cogs
@client.event
async def load():
  for file in os.listdir('cogs'):
    if file.endswith('.py'):
      await client.load_extension(f'cogs.{file[:-3]}')

#first Command
@client.tree.command(name="hello")
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hey, {interaction.user.mention}!")

#load token from secrets
load_dotenv()
token = os.getenv("discord_token")
client.run(token)