from discord.ext import commands

class Fetch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command
    async def fetch(ctx):
        # 851855270685835264
        # 702972566419144875
        channel = self.client.get_channel(851855270685835264)
        messages = await channel.history(limit=10).flatten()

        for msg in messages:
            if len(msg.embeds)>0:
                embed = msg.embeds[0]
                await ctx.channel.send(f"From {msg.guild}\n{embed.title} : {embed.description}")
