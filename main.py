import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='g!')

T = os.environ['TOKEN']

@client.event
async def on_ready():
    print(f"Logged into {client.user}\n\n\n")


@client.command()
async def fetch(ctx):
    # 851855270685835264
    # 702972566419144875
    channel = client.get_channel(851855270685835264)
    messages = await channel.history(limit=100).flatten()
    if (ctx.channel.id == 944452868218437632 or ctx.channel.id == 427546996178419714):    
        for msg in messages:
            if (len(msg.embeds)>0 and msg.author.name=="Auto Upload Bot"):
                embed = msg.embeds[0]
                await ctx.channel.send(f"From {msg.guild}\n{embed.title}\n{embed.description}\n------------------")

client.run(T)