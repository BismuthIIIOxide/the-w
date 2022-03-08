import os
import discord; from discord.ext import commands
import random
import requests
import re
import asyncpraw
TOKEN = os.environ['TOKEN']
reddit = asyncpraw.Reddit(
    client_id = os.environ['CLIENT_ID'],
    client_secret = os.environ['CLIENT_SECRET'],
    user_agent = "u/bbcdeepinmythroat"
)

client = commands.Bot(command_prefix='g!')
client.remove_command('help')

channelID = 925876223878508694

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
    
#########################################################
    if message.guild.id == 427546996178419712 or message.guild.id == 753255421887905834:
        if message.author.id == 829844831710609441 or message.author.id == 367714419179913216:
            if (random.randint(1,12) == 1):
                await message.delete()
                return

        if (random.randint(1,500000) == 1):
            url = "https://api.kanye.rest"
            r = requests.get(url)
            quote = r.json()['quote']
            await message.reply(f"\"{quote}\" - Kanye West")

        if message.author.id == 921685903477452820:
            await message.add_reaction('<:myassitches:948189191022456853')

        if message.channel.id == 950392976843096125:
            chan = client.get_channel(channelID)
            await chan.send(message.content)
      #  if 'this' in msg:
           # if message.author.id != 829844831710609441 or message.author.id != 193932229959876610 or message.author.id != 878159432482177045 or message.author.id != 367714419179913216:
                # await message.channel.send('https://imgur.com/aBUCsv2')
    await client.process_commands(message)

'''
Help
    Took too long to come, will take even longer to be used
'''
@client.command(aliases=['cmds'])
@commands.cooldown(1,2)
async def help(ctx):
    await ctx.channel.send(
        """g!fetch
        g!kanye, g!ye
        g!meme
        g!speak <text>
        g!food
        
        loser.
        """
    )

'''
Fetch Command
    Just fetches the messages from 2PS
'''
@client.command()
@commands.cooldown(1,25)
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
            if ("banned" in embed.title) or ("banned" in embed.description):
                await ctx.channel.send(f"From {msg.guild}\n{embed.title}\n{embed.description}")
                return
            url = re.search("(?P<url>https?://[^\s]+)", embed.description).group("url")
            req = requests.get(f"https://bypass.bot.nu/bypass2?url={url}")
            try_byp = req.json()
            if 'destination' in try_byp:
                
                await ctx.channel.send(
                    f"From {msg.guild}\n{embed.title}\n{try_byp['destination']}"
                )
            else:
                await ctx.channel.send(f"From {msg.guild}\n{embed.title}\n{embed.description}")
                                       
            
'''
Kanye
    I'm a genius!
'''
@client.command(aliases=['quote','ye'])
async def kanye(ctx):
    url = "https://api.kanye.rest"
    r = requests.get(url)
    quote = r.json()['quote']
    await ctx.channel.send(f'\"{quote}\" - Kanye West')


'''
Reddit
    dank meme jojo joylen try not to laugh
'''
@client.command(aliases=['memes'])
@commands.cooldown(1,2)
async def meme(ctx):
    subs = ["ShitPostCrusaders", 
            "animemes", 
            "furry_irl", 
            "wholesomeanimemes"]
    if (random.randint(1,10) == 1):
        subs.append("furry_irl")
    sub = await reddit.subreddit(random.choice(subs))
    submissions = [submission async for submission in sub.hot(limit=35) if not submission.stickied]

    post = submissions[random.randint(0, len(submissions) - 1)]
    await ctx.channel.send(f'{post.title} ({post.score} upvotes) {post.url}')


'''
Speak
    just speaks whatever the user sends to
    another discord
'''
@client.command()
async def speak(ctx, *, message=None):
    global channelID
    if message==None: 
        return
    chan = client.get_channel(channelID)
    
    await chan.send(message)

@client.command(aliases=['channel', 'chan']) # this is an easier way to set a target channel for "Speak"
async def setChannel(ctx, *, id=None):
    global channelID
    if ctx.message.author.id != 193932229959876610:
        return

    channelID = int(id)

'''
Food
    ruh
'''
@client.command()
@commands.cooldown(1,2)
async def food(ctx, *, instructions=False):
    req = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    req = req.json()
    meal = req['meals'][0]
    
    await ctx.channel.send(f"{meal['strMeal']}\n{meal['strMealThumb']}")
    if instructions==True:
        await ctx.channel.send(f"{meal['strInstructions']}\n{meal['strSource']}")


'''
Error Handeling
'''
@fetch.error
async def fetch_error(ctx, err):
    if isinstance(err, commands.CommandOnCooldown):
        return

@meme.error
async def meme_error(ctx, err):
    if isinstance(err,commands.CommandOnCooldown):
        return

@help.error
async def help_error(ctx, err):
    if isinstance(err,commands.CommandOnCooldown):
        return

@food.error
async def food_error(ctx, err):
    if isinstance(err,commands.CommandOnCooldown):
        return
client.run(TOKEN)
