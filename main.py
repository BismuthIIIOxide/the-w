import os
import discord
from discord.ext import commands
import random
import asyncio
import requests
import re


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
# 193932229959876610 
# 878159432482177045 // meca
# 829844831710609441 // jerry
# 367714419179913216 // mako
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.guild and message.author.id == 193932229959876610:
        if "say ok if" in message.content.lower() or "say" in message.content.lower():
            return
        await asyncio.sleep(1)
        await message.channel.send('ok')
    elif message.guild.id == 427546996178419712 or message.guild.id == 753255421887905834:
        msg = message.content.lower()
        if message.author.id == 829844831710609441 or message.author.id == 367714419179913216:
            if (random.randint(1,5) == 5):
                await message.reply("stfu")

        
        if message.author.id == 878159432482177045:
            if (random.randint(1,10) == 10):
                await message.reply("Rule 1/Rule2:\n(1)No bad opinions\n(2)Don't be unfunny\n(If you believe this was a mistake, DM me with details.)")
                await message.delete()
        
        if 'this' in msg:
            if message.author.id != 829844831710609441 or message.author.id != 193932229959876610 or message.author.id != 878159432482177045 or message.author.id != 367714419179913216:
                await message.channel.send('https://imgur.com/aBUCsv2')
        
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
            if ('30' in embed.title) or ('30' in embed.description):
                return

            await ctx.channel.send(
                f"From {msg.guild}\n{embed.title}\n{embed.description}\n------------------"
            )
            url = re.search("(?P<url>https?://[^\s]+)", embed.description).group("url")
            req = requests.get(f"https://bypass.bot.nu/bypass2?url={url}")
            try_byp = req.json()
            if 'destination' in try_byp:
                await ctx.channel.send(f"Linkvertise bypassed:\n{try_byp['destination']}")
            else:
                await ctx.channel.send("Linkvertise failed to bypass")
                                       
            


client.run(TOKEN)
