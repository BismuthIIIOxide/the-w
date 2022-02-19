import os
import discord
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
client = commands.Bot(command_prefix='g!', description=description)
T = os.environ['TOKEN']

for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        client.load_extension("cogs." + f[:-3])

@client.event
async def on_ready():
    print('Logged on as', client.user)



client.run(T)