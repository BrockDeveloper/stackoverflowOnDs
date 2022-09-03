import discord
from data.courses import Courses
from components.survey import Survey


class Select(discord.ui.Select):

    def __init__(self, bot):
        self.bot = bot
        super().__init__(placeholder="Corso", options=self.__generate_options())


    def __generate_options(self):
        options = []
        for course in Courses:
            options.append(discord.SelectOption(label=course))
        return options


    async def callback(self, interaction):
        modal = Survey(self.values[0], interaction, self.bot)
        await interaction.response.send_modal(modal)