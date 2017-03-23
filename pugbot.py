import json
import os

import discord

# Commands #
from commands.pug import pug

CLIENT = discord.Client()
config = json.laods(open('config.json').read())  #Loads Config File
DISCORD_TOKEN = config["discord_token"]

@CLIENT.event
async def on_ready():
    print('Logged in as')
    print(CLIENT.user.name)
    print(CLIENT.user.id)
    print('------')


@CLIENT.event
async def on_message(message):

    if message.content.startswith('!info') or message.content.startswith('!help'):
        await CLIENT.send_message(message.channel, "I'm PugBot, the pug analyzer!\n"
                                                   "Use: !pug <name> <server> <region> \n"
                                                   "Example: !pug NiczeAlind Area-52 us")

    if message.content.startswith('!pug'):
        await pug(CLIENT, message)

CLIENT.run(DISCORD_TOKEN)
