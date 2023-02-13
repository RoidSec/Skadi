import discord
from discord import app_commands
from discord.ext import commands

class Role(commands.Cog):
    def __init__ (self,bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('- WoW Role cog loaded')
    
    @app_commands.command(name="chooserole", description="Role selector")
    @app_commands.describe(wowrole='Role to choose from')
    @app_commands.choices(wowrole=[
        discord.app_commands.Choice(name='Tank', value=1),
        discord.app_commands.Choice(name='DPS', value=2),
        discord.app_commands.Choice(name='Healer', value=3),
    ])
    async def chooserole(self, interaction: discord.Interaction, wowrole: discord.app_commands.Choice[int]):
        await interaction.response.send_message(f'Role selected: {wowrole.name}')

async def setup(bot):
    await bot.add_cog(Role(bot))