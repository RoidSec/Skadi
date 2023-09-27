import discord
from discord import app_commands
from discord.ext import commands

class Parse(commands.Cog):
    def __init__ (self,bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('- Dota Parser cog loaded')
    
    @app_commands.command(name="parse", description="OpenDota parser")
    @app_commands.describe(parse='Choose a person to parse')
    @app_commands.choices(parse=[
        discord.app_commands.Choice(name='Colin', value=1),
        discord.app_commands.Choice(name='Connor', value=2),
        discord.app_commands.Choice(name='Shanise', value=3),
        discord.app_commands.Choice(name='Tim', value=4),
        discord.app_commands.Choice(name='Shaun', value=5),
        discord.app_commands.Choice(name='Anthony', value=6),
        discord.app_commands.Choice(name='Harry', value=7),
        discord.app_commands.Choice(name='Casey', value=8)
    ])
    async def parse(self, interaction: discord.Interaction, parse: discord.app_commands.Choice[int]):
        await interaction.response.send_message(f'Parse started for {parse.name}', ephemeral=True)
        
        '''discord.app_commands.Choice(name='Colin', value=44067861),
        discord.app_commands.Choice(name='Connor', value=39958451),
        discord.app_commands.Choice(name='Shanise', value=337288948),
        discord.app_commands.Choice(name='Tim', value=99084628),
        discord.app_commands.Choice(name='Shaun', value=145692671),
        discord.app_commands.Choice(name='Anthony', value=282780720),
        discord.app_commands.Choice(name='Harry', value=83942876),
        discord.app_commands.Choice(name='Casey', value=69558459)'''

async def setup(bot):
    await bot.add_cog(Parse(bot))