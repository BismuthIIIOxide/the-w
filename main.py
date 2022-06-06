import os
import discord; 
from discord.ext import commands
import requests
import re
TOKEN = os.environ['TOKEN']

print('loaded everything')

client = commands.Bot(command_prefix='g!')
channelID = 925876223878508694

@client.event
async def on_ready():
    print(f"Logged into {client.user}\n##########")
    
    chan = client.get_channel(channelID)
    await chan.send("hacker mode..... ON")

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
    if not message.guild.id:
        return
    if message.channel.id == channelID:
        await message.channel.send('I HATE YOU')
      #  if 'this' in msg:
           # if message.author.id != 829844831710609441 or message.author.id != 193932229959876610 or message.author.id != 878159432482177045 or message.author.id != 367714419179913216:
                # await message.channel.send('https://imgur.com/aBUCsv2')
    await client.process_commands(message)

@client.command()
async def test(ctx):
    print("hello")
    await ctx.channel.send("hi")
'''
Fetch Command
    Just fetches the messages from 2PS
'''
@client.command()
@commands.cooldown(1,2.5)
async def fetch(ctx):
    # 851855270685835264
    # 702972566419144875
    channel = client.get_channel(851855270685835264)
    messages = await channel.history(limit=100).flatten()
    for msg in messages:
        if (len(msg.embeds) > 0 and msg.author.name == "Auto Upload Bot"):
            embed = msg.embeds[0]
            #if ('3' in embed.title):
                #continue
            if ("banned" in embed.title) or ("banned" in embed.description):
                await ctx.channel.send(f"From {msg.guild}\n{embed.title}\n{embed.description}")
                return
            
            url = re.search("(?P<url>https?://[^\s]+)", embed.description).group("url")
            await ctx.channel.send(f"1 trying bypass on {url}")
            
            req = requests.get(f"https://bypass.bot.nu/bypass2?url={url}")
            try_byp = req.json()
            if 'destination' in try_byp:
                await ctx.channel.send(
                    f"From {msg.guild}\n{embed.title}\n{try_byp['destination']}"
                )
            else:
                print('failed')
                await ctx.channel.send(f"From {msg.guild}\n{embed.title}\n{embed.description}")


client.run(TOKEN, bot=False)

