import os
from dotenv import load_dotenv
import discord


load_dotenv()


# generic bot intents, admin level permissions
intents = discord.Intents.default()
intents.message_content = True


# client connection, that is the bot
client = Client()
client.run(os.getenv("TOKEN"))