import discord
import requests

async def create_thread(name, minutes, message, channel: discord.TextChannel):

    token = 'Bot ' + channel._state.http.token
    url = f"https://discord.com/api/v9/channels/965312781702271067/messages/{message.id}/threads"

    headers = {
        "authorization" : token,
        "content-type" : "application/json"
    }
    
    data = {
        "name" : name,
        "type" : 11,
        "auto_archive_duration" : minutes
    }

    return requests.post(url,headers=headers,json=data).json()