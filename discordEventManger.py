import discord
token = ''
with open('auth.txt', mode='r') as authFile:
    token = authFile.readlines()[0]


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
