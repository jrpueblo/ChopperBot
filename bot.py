# Starter Discord Bot
# Author: Jan Rylan Pueblo
# Version 1.2 Added Tutorial, help and chopper gif functions
# January 25th, 2022


import valorantProfile
import discord
import random

client = discord.Client()

# NOTE: This Token has been changed and will not work until bot made public
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


    if user_message.lower() == "~hello" or user_message.lower() == "!hello":
        await message.channel.send(f"Hello {username}!")
        return
    elif user_message.lower() == "~bye" or user_message.lower() == "!bye":
        await message.channel.send(f'See you later {username}!')
        return
    elif user_message.lower() == "~goodnight" or user_message.lower() == "!goodnight":
        await message.channel.send(f"Goodnight {username}!")
        return
    elif user_message.lower() == "~chopper" or user_message.lower() == "!chopper":
        await message.channel.send(file=discord.File('anime-chopper.gif'))
        return
    elif user_message.lower() == "~random" or user_message.lower() == "!random":
        response = f'Your random number is: {random.randrange(100)}'
        await message.channel.send(response)
        return
    elif user_message.lower() == '~coin flip' or user_message.lower() == "!coin flip":
        flip = "Tails"
        if(random.randrange(100) > 50):
            flip = "Heads"
        response = f'It is {flip}'
        await message.channel.send(response)
        return

    if message.channel.name == "valorant-bot" or message.channel.name == "discord-bot-test":
        #looking up valorant rank
        if user_message.startswith("!lookup"):
            try:
                response = user_message.split(' ')
                player = []
                for i in range(1, len(response) - 1):
                    player.append(response[i])
                tag = response[len(response) - 1]
                profile = valorantProfile.valorantProfile(player, tag)
                if (profile.immortalPlus):
                    await message.channel.send("Current Rank: " + profile.getMainStats()[0])
                    await message.channel.send("Leaderboard Rank: " + profile.getMainStats()[1])
                    await message.channel.send("K/D Ratio: " + profile.getMainStats()[2])
                    await message.channel.send("Win%: " + profile.getMainStats()[3])
                else:
                    await message.channel.send("Current Rank: " + profile.getMainStats()[0])
                    await message.channel.send("K/D Ratio: " + profile.getMainStats()[1])
                    await message.channel.send("Win%: " + profile.getMainStats()[2])
            except:
                await message.channel.send("This user is private or has not played valorant!")
            return

        if user_message.lower() == "!tutorial":
            await message.channel.send("Hello " + str(message.author) + "! My name is Tony Tony Chopper")
            await message.channel.send("I can perform simple functions like respond to greetings, coin flips or random number generating")
            await message.channel.send("To lookup your Valorant stats, type !lookup username tag")
            await message.channel.send("More functional to come in the future!")
            await message.channel.send("- Tony Tony Chopper")

        if user_message.lower() == "!help":
            await message.channel.send("Hello " + str(message.author) + "!")
            await message.channel.send("To lookup your valorant stats, type !lookup username tag")
            await message.channel.send("Please note that this is an alpha version and the command will not work if you are immortal+")
            await message.channel.send("Sorry for the inconvenience!")

        if user_message.lower() == '!usable':
            await message.channel.send('Chopper is avaliable here!')
            return

    if message.channel.name == "chess":
        # looking up valorant rank
        if user_message.startswith("~lookup"):
            try:
                response = user_message.split(" ")
                username = response[1]
                tag = response[2].replace("#", "")
                profile = valorantProfile.valorantProfile(username, tag)
                if(profile.immortalPlus):
                    await message.channel.send("Current Rank: " + profile.getMainStats()[0])
                    await message.channel.send("Leaderboard Rank: " + profile.getMainStats()[1])
                    await message.channel.send("K/D Ratio: " + profile.getMainStats()[2])
                    await message.channel.send("Win%: " + profile.getMainStats()[3])
                else:
                    await message.channel.send("Current Rank: " + profile.getMainStats()[0])
                    await message.channel.send("K/D Ratio: " + profile.getMainStats()[1])
                    await message.channel.send("Win%: " + profile.getMainStats()[2])
            except:
                await message.channel.send("This user is private or has not played valorant!")
            return

        if user_message.lower() == "~help":
            await message.channel.send("Hello " + str(message.author) + "!")
            await message.channel.send("To lookup your valorant stats, type !lookup username tag")
            await message.channel.send(
                "Please note that this is an alpha version and the command will not work if you are immortal+")
            await message.channel.send("Sorry for the inconvenience!")

        if user_message.lower() == "~tutorial":
            await message.channel.send("Hello " + str(message.author) + "! My name is Tony Tony Chopper")
            await message.channel.send(
                "I can perform simple functions like respond to greetings, coin flips or random number generating")
            await message.channel.send("To lookup your Valorant stats, type !lookup username tag")
            await message.channel.send("More functional to come in the future!")
            await message.channel.send("- Tony Tony Chopper")

        if user_message.lower() == '~usable':
            await message.channel.send('Chopper is avaliable here!')
            return


client.run(TOKEN)
