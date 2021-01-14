import discord
token = "Nzk5MzU3NjIxNDQ1NDU5OTc5.YACZzA.T-ERezJPLifXpLzz7ICcU5nJ6C8"


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('!!'):
            await message.channel.send("Summon the upside down bear")


client = MyClient()
client.run(token)
