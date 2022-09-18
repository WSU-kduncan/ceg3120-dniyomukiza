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

    question1_to_ask = [
       ' Hi! I\'m TeckTalk and I can answer to your questions relating the currenty technology and society.',
        'Hey,how can I help?',
        (
            'Cool. Do you have something on your mind today?'
        ),
    ]

    good_answers_bot = [
        'I do not really worry honestly.',
        'Yes,technology providers do not provide as much digital security as they possibly can.',
        'In fact I have never thought about this.',
        'I do not worry about my privacy, if someone really wants your data they will get it.',
    ]


    dictionary = [
            'Was nice to have you!',
            'Have a nice day!',
            
            ]
    personal_questions = [
              'I was born before the creation of the universe.',
              '2000 years BE',
              
              ]
    some_random_answer = [
       'Well, my favorite piece of technology is my phone.',
       'My favorite technology I use daily is google. Google is my friend.',
       'The main favorite for me in technology would be my arcade stick.',
        
    ]
    
    if message.content == 'Tell me your favorite technology tool and why you use it':
        response = random.choice(some_random_answer)
        await message.channel.send(response)

    if message.content == 'Hi!':
        response = random.choice(question1_to_ask)
        await message.channel.send(response)

    if message.content == 'Do you worry your technology provider is doing everything in their control to provide digital security?':
        response = random.choice(good_answers_bot)
        await message.channel.send(response)
    if message.content == 'goodbye!':
        response = random.choice(dictionary)
        await message.channel.send(response)
    if message.content == 'how old are you?':
        response = random.choice(personal_questions)
        await message.channel.send(response)
client.run(TOKEN)