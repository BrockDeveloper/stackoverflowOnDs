import discord
from discord.ui import View
from data.config import Config
from discord.ext import commands
from components.select import Select


class Client(commands.Bot):


    @commands.command()
    async def test(ctx):
        print("test")


    def __init__(self):
        super().__init__(command_prefix='$')
        super().add_command(self.test)


    async def on_ready(self):

        embed=discord.Embed(title=Config["title"], description=Config["description"], color=0xffae00)
        embed.set_thumbnail(url=Config["icon"])
        embed.set_footer(text=Config["footer"])

        select = Select(self)

        view = View()
        view.add_item(select)

        channel = self.get_channel(965312718963879956)

        await channel.send(embed=embed)
        await channel.send("Seleziona un macroargomento (knowed issue: a volte si blocca, tentare più volte la selezione):", view=view)


    async def on_message(self, message):
        pass