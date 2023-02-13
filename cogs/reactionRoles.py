import discord
from discord import app_commands
from discord.ext import commands

class reactRoles(commands.Cog):
    def __init__ (self,bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('- Reaction roles cog loaded')

async def setup(bot):
    await bot.add_cog(reactRoles(bot))