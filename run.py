import os
import discord
from dotenv import load_dotenv
from connection.client import Client


load_dotenv()


# generic bot intents, admin level permissions
intents = discord.Intents.default()
intents.message_content = True


# client connection, that is the bot
client = Client()
client.run(os.getenv("TOKEN"))