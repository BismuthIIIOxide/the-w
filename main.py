import os
import discord

T = os.environ['TOKEN']
            
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self,message):
        if (message.channel.id == 702972566419144875 and message.author.id != self.user.id):
            # chan = self.get_channel(702972566419144875)
            await message.channel.send(f'message from {message.author.name} in {message.channel.name}:\n  {message.content}')


client = MyClient()
client.run(T)