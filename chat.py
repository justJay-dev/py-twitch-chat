from twitchio.ext import commands
from twitchio.ext.commands.errors import CommandNotFound
from config import *

class Color:
    blue ='\u001b[34;1m'
    yellow = '\u001b[33m'
    white = '\u001b[37m'

bot = commands.Bot(
    irc_token = TWITCH_OAUTH,
    client_id ='test',
    nick = TWITCH_USERNAME,
    prefix = '!',
    initial_channels = [TWITCH_USERNAME]
)

@bot.event
async def event_ready():
    print(f'Goliath Online | {bot.nick}')

@bot.event
async def event_message(message):
    print(f'{Color.blue} <{message.channel.name}> {Color.yellow} {message.author.name} : {Color.white}{message.content}')

bot.run()



