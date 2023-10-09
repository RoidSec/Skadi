import discord
import requests
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("apikey")

class opendota(commands.Cog):
    def __init__ (self,bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('- Open Dota cog loaded')

    @app_commands.command(name="opendota", description="OpenDota parse")
    @app_commands.describe(parse='Choose a person to parse')
    @app_commands.choices(parse=[
        discord.app_commands.Choice(name='Zzzonked',value=1),
        discord.app_commands.Choice(name='Connor',value=2),
        discord.app_commands.Choice(name='Shanise',value=3),
        discord.app_commands.Choice(name='Tim',value=4),
        discord.app_commands.Choice(name='Shaun',value=5),
        discord.app_commands.Choice(name='Anthony',value=6),
        discord.app_commands.Choice(name='Harry',value=7),
        discord.app_commands.Choice(name='Casey',value=8)
    ])
    async def check_stats(self, ctx, player_name):
        try:
            api_url = f'https://api.opendota.com/api/players/{app_commands.Choice}?api_key={apikey}'
            
            response = requests.get(api_url)
            data = response.json()
            
            if response.status_code == 200:
                player_id = data['profile']['account_id']
                player_name = data['profile']['personaname']
                mmr = data['mmr_estimate'][0]['estimate']
                
                embed = discord.Embed(title=f'Stats for {player_name}', color=discord.Color.blue())
                embed.add_field(name='Player ID', value=player_id, inline=False)
                embed.add_field(name='MMR Estimate', value=mmr, inline=False)
                
                await ctx.send(embed=embed)
            else:
                await ctx.send("Player not found or an error occurred while fetching data.")
        
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(opendota(bot))