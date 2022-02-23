import os
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='g!')
client.remove_command('help')
TOKEN = os.environ['TOKEN']


@client.event
async def on_ready():
    print(f"Logged into {client.user}\n##########")

'''
On Message Event
    For various goofs
'''
@client.event
async def on_message(message):
    if message.guild.id == 427546996178419712 or message.guild.id == 753255421887905834:
        msg = message.content.lower()
        if 'this' in msg:
            await message.channel.send('https://imgur.com/aBUCsv2')

        if message.author.id == 829844831710609441 or message.author.id == 878159432482177045 or message.author.id == 367714419179913216:
            if (random.randint(1,5) == 5):
                await message.reply("stfu")
                
    await client.process_commands(message)

'''
Fetch Command
    Just fetches the messages from 2PS
'''
@client.command()
async def fetch(ctx):
    # 851855270685835264
    # 702972566419144875
    channel = client.get_channel(851855270685835264)
    messages = await channel.history(limit=100).flatten()
    for msg in messages:
        if (len(msg.embeds) > 0 and msg.author.name == "Auto Upload Bot"):
            embed = msg.embeds[0]
            await ctx.channel.send(
                f"From {msg.guild}\n{embed.title}\n{embed.description}\n------------------"
            )


client.run(TOKEN)
