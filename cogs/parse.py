import discord
from discord import app_commands
from discord.ext import commands
import requests

class Parse(commands.Cog):
    def __init__ (self,bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('- Dota Parser cog loaded')
    
    @app_commands.command(name="parse", description="OpenDota parser")
    @app_commands.describe(parse='Choose a person to parse')
    @app_commands.choices(parse=[
        discord.app_commands.Choice(name='Colin',value=1),
        discord.app_commands.Choice(name='Connor',value=2),
        discord.app_commands.Choice(name='Shanise',value=3),
        discord.app_commands.Choice(name='Tim',value=4),
        discord.app_commands.Choice(name='Shaun',value=5),
        discord.app_commands.Choice(name='Anthony',value=6),
        discord.app_commands.Choice(name='Harry',value=7),
        discord.app_commands.Choice(name='Casey',value=8)
    ])
    async def parse(self, interaction: discord.Interaction, parse: discord.app_commands.Choice[int]):
        await interaction.response.send_message(f'Parse started for {parse.name}', ephemeral=True)
        

        anthonyID=282780720
        colinID=44067861
        connorID=39958451
        shaniseID=337288948
        timID=99084628
        shaunID=145692671
        harryID=83942876
        caseyID=69558459

        try:
            api_url = f'https://api.opendota.com/api/players/{player_name}?api_key={api_key}'
            
            response = requests.get(api_url)
            data = response.json()
            
            if response.status_code == 200:
                player_id = data['profile']['account_id']
                player_name = data['profile']['personaname']
                mmr = data['mmr_estimate'][0]['estimate']
                
                embed = discord.Embed(title=f'Stats for {player_name}', color=discord.Color.blue())
                embed.add_field(name='Player ID', value=player_id, inline=False)
                embed.add_field(name='MMR Estimate', value=mmr, inline=False)
                
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Player not found or an error occurred while fetching data.")
        
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}")



async def setup(bot):
    await bot.add_cog(Parse(bot))