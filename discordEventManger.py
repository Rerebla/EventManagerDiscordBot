import discord
import re
import time
import datetime
token = ''
with open('auth.txt', mode='r') as authFile:
    token = authFile.readlines()[0]


async def resolveMethods(argument, passthroughArguments, message):
    methodSwitcher = {
        'registerEvent': MyClient.registerEventCommands
    }
    func = methodSwitcher.get(argument)
    if func is None:
        func = MyClient.failedCommand
    await func(client, passthroughArguments, message)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('!!') is False:
            return

        messageAndArguments = message.content[2:].split(' ')
        await resolveMethods(messageAndArguments[0], messageAndArguments[1:], message)

    async def internalEventRegister(self, embed, arguments, message, myEmbed, channel):
        dateTimeStr = arguments[1] + " " + arguments[2]
        try:
            dateTimeObj = datetime.datetime.strptime(
                dateTimeStr, '%Y-%m-%d %H:%M')
        except:
            client.failedCommand(arguments, message)
        print(dateTimeObj)
        currentTime = datetime.datetime.now()
        duration = dateTimeObj - currentTime
        if duration.total_seconds() <= 0:
            print("The event already was supposed to happen")
            await message.author.send(
                "You are trying to make a event for the past. That's not how time works.")
        elif duration.total_seconds() > 0:
            print("The event is sceduled")
            await channel.send(embed=myEmbed)
        print(duration)

    async def registerEventCommands(self, arguments, message):
        # registerEvent <Title> <Date> <Time 24h> <ChannelID> <Additional Notes>
        additionalNotes = ""
        try:
            additionalNotes = arguments[4]
        except:
            additionalNotes = None

        try:
            myEmbed = discord.Embed(
                title="New Event at {0}".format(arguments[1]), color=0x00ff00)
            myEmbed.add_field(name="Event type",
                              value=arguments[0], inline=False)
            channelID = arguments[3]
            channel = client.get_channel(int(channelID))
            if additionalNotes is not None:
                myEmbed.add_field(name="Additional Notes",
                                  value=additionalNotes)
        except:
            await client.failedCommand(arguments, message)

        await client.internalEventRegister(myEmbed, arguments, message, myEmbed, channel)

    async def failedCommand(self, arguments, message):
        await message.author.send(
            "It seems like that you've performed an unknown command! OR One or more of your arguments were faulty")


client = MyClient()
client.run(token)
