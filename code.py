import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!') 

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
       ' Hi! I\'m TeckTalk and I can answer to your questions relating the currenty technology and society.',
        'Hey,how can I help?',
        (
            'Cool. Do you have something on your mind today?'
        ),
    ]

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

    if message.content == 'Tell me your favorite technology tool and why you use it':
    
        await message.channel.send("Well, my favorite piece of technology is my phone because of the accessibility.  The ability to keep in contact with my friends and help track of my work and being able to look up things such as locations and information.")

    if message.content == 'Hi!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)




client.run(TOKEN)
