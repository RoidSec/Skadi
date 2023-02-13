import discord
from discord import app_commands
from discord.ext import commands

class commandSync(commands.Cog):
    def __init__ (self,bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(
            f"Synchronised {len(fmt)} commands to the current guild"
        )
        return

async def setup(bot):
    await bot.add_cog(commandSync(bot))