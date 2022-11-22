import discord
from discord.ext import commands

class Buttons(discord.ui.view):
    def __init__(self,*, timeout=100):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="clickme",style=discord.ButtonStyle.gray)
    async def click(self, interaction: discord.interaction, button: discord.ui.Button,):
        await interaction.response.send_message("you clicked me!")

class Clickme(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Clickme cpg loaded')

    @commands.command()
    async def click(self,ctx):
        await ctx.send("Message with a button", view=Buttons())


async def setup(client):
    await client.add_cog(Clickme(client))