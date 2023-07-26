import discord
from discord import app_commands
from discord.ext import commands


class Raid(commands.Cog):
    def __init__ (self,bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('- Raid Maker cog loaded')
    
    @commands.command()
    async def embed(self,ctx):
        if member == None:
            member = ctx.author

        name = member.display_name
        pfp = member.display_avatar

        embed = discord.Embed(title="Raid Time!", description="this is the description", color=discord.colour.random())
        embed.set_author(name=f"{name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=f"{pfp}")
        embed.add_field(name='Role',value='value', inline = True)
        embed.add_field(name='Player',value='value', inline = True)
        embed.set_footer(text=f"{name}")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Raid(bot))