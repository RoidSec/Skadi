import discord
from discord import app_commands
from discord.ext import commands

class Class(commands.Cog):
    def __init__ (self,bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('WoW Class cog loaded')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(
            f"synced {len(fmt)} commands to the current guild"
        )
        return
    
    @app_commands.command(name="chooseclass", description="Class selector")
    @app_commands.describe(wowclass='Classes to choose from')
    @app_commands.choices(wowclass=[
        discord.app_commands.Choice(name='Death Knight', value=1),
        discord.app_commands.Choice(name='Demon Hunter', value=2),
        discord.app_commands.Choice(name='Druid', value=3),
        discord.app_commands.Choice(name='Evoker', value=4),
        discord.app_commands.Choice(name='Hunter', value=5),
        discord.app_commands.Choice(name='Mage', value=6),
        discord.app_commands.Choice(name='Monk', value=7),
        discord.app_commands.Choice(name='Paladin', value=8),
        discord.app_commands.Choice(name='Priest', value=9),
        discord.app_commands.Choice(name='Rogue', value=10),
        discord.app_commands.Choice(name='Shaman', value=11),
        discord.app_commands.Choice(name='Warlock', value=12),
        discord.app_commands.Choice(name='Warrior', value=13),
    ])
    async def chooseclass(self, interaction: discord.Interaction, wowclass: discord.app_commands.Choice[int]):
        await interaction.response.send_message(f'Class selected: {wowclass.name}')

async def setup(bot):
    await bot.add_cog(Class(bot))