import discord
from discord.ext import commands
import httpx

class Parser(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('- Dota Parser cog loaded')

    @commands.command(name="parser", description="OpenDota parser")
    @commands.cooldown(1, 10, commands.BucketType.user)  # Add a cooldown to prevent spamming
    async def parser(self, ctx: commands.Context, player_name: str):
        await ctx.trigger_typing()

        # Define your OpenDota API URL with the player_name
        api_url = f"https://api.opendota.com/api/players/{player_name}"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(api_url)

            if response.status_code == 200:
                data = response.json()
                # Extract and display relevant player information
                player_id = data["profile"]["account_id"]
                mmr = data["mmr_estimate"]["estimate"]
                winrate = data["winrate"]
                await ctx.send(f"Player ID: {player_id}\nMMR Estimate: {mmr}\nWinrate: {winrate}%")
            else:
                await ctx.send(f"Failed to retrieve data from OpenDota API. Status Code: {response.status_code}")

        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(Parser(bot))
