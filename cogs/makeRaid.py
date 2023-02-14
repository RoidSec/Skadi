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
    async def makeraid(self,ctx):
        role = 'Tank'
        player = 'Roidbear'
        raidteam = discord.Embed(title="Raid Time!",color=0x03dffc)
        raidteam.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        raidteam.set_thumbnail(url='https://i.imgur.com/U2N9l0E.jpg')
        raidteam.add_field(name='Role',value=' \n'.join(role), inline = True)
        raidteam.add_field(name='Player',value=' \n'.join(player), inline = True)
        await ctx.send(embed=raidteam)

async def setup(bot):
    await bot.add_cog(Raid(bot))