import os
import discord; from discord.ext import commands
import random
import requests
import re
import asyncpraw
from faker import Faker; from faker.providers import internet
import asyncio
TOKEN = os.environ['TOKEN']
reddit = asyncpraw.Reddit(
    client_id = os.environ['CLIENT_ID'],
    client_secret = os.environ['CLIENT_SECRET'],
    user_agent = os.environ['USER_AGENT']
)

client = commands.Bot(command_prefix='g!', case_insensitive=True)
client.remove_command('help')

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
    
#########################################################
    if message.guild.id == 427546996178419712 or message.guild.id == 753255421887905834:
        #print(message.content)
        if message.author.id == 829844831710609441: # This is jerry
            if (random.randint(1,5) == 1):
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
Fetch Command
    Just fetches the messages from 2PS
'''
@client.command()
@commands.cooldown(1,5)
async def fetch(ctx):
    # 851855270685835264
    # 702972566419144875
    channel = client.get_channel(851855270685835264)
    messages = await channel.history(limit=100).flatten()
    for msg in messages:
        if (len(msg.embeds) > 0 and msg.author.name == "Auto Upload Bot"):
            embed = msg.embeds[0]
            if ('3' in embed.title):
                continue
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
@client.command(aliases=['memes', 'reddit'])
@commands.cooldown(1,0.25)
async def meme(ctx, *, red=None):
    if 'r/' in red:
        red = red.replace('r/','')
        sub = await reddit.subreddit(red)
    else:
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
Troll
    I love faker!
'''
@client.command()
async def troll(ctx, user: discord.User = None):
    if user == None:
        return
    fake = Faker('en_US')
    Faker.seed(user.id)
    
    if user.id == 193932229959876610:
        await ctx.channel.send("sorry i cant hack anonymous")
        return
    if user.id == 695728013626835055: 
        return
        
    await ctx.channel.send(
        f"""
{fake.first_name_male()} {fake.last_name_male()}
                           
IP: {fake.ipv4_private()}
Address: {fake.address()}
                           
SSN: {fake.ssn()}

Credit Card: {fake.credit_card_number()} / {fake.credit_card_expire()} / {fake.credit_card_security_code()}
"""
    )

'''
Ban
    real ban?!
'''
@client.command()
async def ban(ctx, user: discord.User = None, *reason: str):
    if user == None:
        return
    if len(reason) == 0:
        await ctx.channel.send(f"Banned {user.name} for: No reason")
        return
    await ctx.channel.send(f"Banned {user.name} for: {' '.join(reason)}")

'''
Eval
    Worst idea ever ?
'''  
@client.command(aliases=['eval'])
async def test(ctx, *args: str):
    args = ' '.join(args)
    if ctx.message.author.id != 193932229959876610: 
        return

    await ctx.channel.send(f"{eval(args)}")

'''ok
ok
    ok
'''


'''
nickanem 
    TROL!!!
'''
@client.command(pass_context=True)
async def nickname(ctx, channel: int, *args: str):
    if ctx.message.author.id != 193932229959876610: 
        return

    args = ' '.join(args)
    server = client.get_guild(channel)
    for member in server.members:
        if member.id != 193932229959876610:
            await member.edit(nick=args)
            await asyncio.sleep(0.25)

@client.command(pass_context=True)
async def removenick(ctx,channel: int):
    if ctx.message.author.id != 193932229959876610: 
        return

    
    server = client.get_guild(channel)
    for member in server.members:
        if member.id != 193932229959876610:   
            await member.edit(nick=None)
            await asyncio.sleep(0.25)
    
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

@food.error
async def food_error(ctx, err):
    if isinstance(err,commands.CommandOnCooldown):
        return

@troll.error
async def troll_error(ctx,err):
    if isinstance(err,commands.UserNotFound):
        return
'''
@hello.error
async def hello_error(ctx,err):
    if isinstance(err, commands.NSFWChannelRequired):
        await ctx.channel.send("not nsfw channel")
        return
   '''     
client.run(TOKEN)

