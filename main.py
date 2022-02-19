import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='g!')
T = os.environ['TOKEN']

for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        client.load_extension("cogs." + f[:-3])

@client.event
async def on_ready():
    print(f'Logged on as {client.user}\n\n\n')



client.run(T)