import discord
from discord.ui import Modal, InputText
from connection.util import create_thread


class Survey(Modal):


    def __init__(self, course: str, interaction: discord.Interaction, bot) -> None:

        super().__init__(title="Nuova domanda di: " + course)
        self.channel = interaction.channel
        self.message = interaction.message
        self.course = course
        self.bot = bot

        self.add_item(InputText(label="Titolo", placeholder="Titolo"))
        self.add_item(InputText(label= "Domanda completa", placeholder="Domanda completa", value= "", style=discord.InputTextStyle.long))


    async def callback(self, interaction: discord.Interaction):


        embed = discord.Embed(title="Nuova domanda", color=discord.Color.blurple())

        embed.add_field(name="Corso", value=self.course, inline=False)
        embed.add_field(name="Titolo", value=self.children[0].value, inline=False)
        embed.add_field(name="Domanda", value=self.children[1].value, inline=False)

        channelstorico = self.bot.get_channel(965312781702271067)
        storico = await channelstorico.send(embeds=[embed])

        await create_thread(self.children[0].value, 1440, storico, interaction.channel)
        await interaction.response.defer()