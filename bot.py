# Starter Discord Bot
# Author: Jan Rylan Pueblo
# Version 1.1 Simple Events and Valorant Utils
# January 25th, 2022


import valorantProfile
import discord
import random

client = discord.Client()

TOKEN = "OTM4MzAwMDk4MzczMzY1Nzgw.YfoSEA.jJqTfMkmBCCO62JIYjvajGU8QM0"


#  This event notifies when the bot is ready to be used
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):

    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # This is to ensure the bot does not infinitely respond
    # to its own messages

    if message.author == client.user:
        return

    if message.channel.name == "discord-bot-test":
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}!")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == 'random':
            response = f'Your random number is: {random.randrange(100)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'coin flip':
            flip = "Tails"
            if(random.randrange(100) > 50):
                flip = "Heads"
            response = f'It is {flip}'
            await message.channel.send(response)
            return

    if message.channel.name == "valorant-bot":
        #looking up valorant rank
        if user_message.startswith("!lookup"):
            response = user_message.split(" ")
            username = response[1]
            tag = response[2].replace("#", "")
            profile = valorantProfile.valorantProfile(username, tag)
            await message.channel.send("Current Rank: " + profile.getMainStats()[0])
            await message.channel.send("K/D Ratio: " + profile.getMainStats()[1])
            await message.channel.send("Win%: " + profile.getMainStats()[2])
            return



    if user_message.lower() == '!usable':
        await message.channel.send('Chopper is avaliable here!')
        return

client.run(TOKEN)
