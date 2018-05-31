""" Discord Bot written by Tim in Python."""
# TODO MAKE SURE TO .GITIGNORE LOCAL CONFIG.PY MAKE BAT FILE OR GUI TO CREATE NEW CONFIG.PY
# OPTIONS - Upload config.py as empty, DO NOT STAGE LOCAL ONE and have the bat/python gui update it
# OR - have bat/python gui make the config.py file - but one con is the user is forced to do it that way, can't do it manually/


# TODO - Allow user to set up configurations (Enter own token, prefix, and user_id into a GUI or console and change them here
# - More on-event responses
# - Interact with other files More
# - Require administrator perms for some commands
# - **Make the project structure look better and make more sense**
# - Make this a main file with cogs in other files? 
# - Make a class out of the bot setup and just make an instance of the bot?


# Imports dependencies.
import logging
import discord
from discord import Game
from discord.ext import commands

import os


# Sets up logging in the console.
logging.basicConfig(level=logging.INFO)


# ENTER BOT TOKEN AND PREFIXES HERE (Manual set up)
bot_token = ""

bot_prefix = ""

# Obtains bot token and prefix from the config file. TODO - Can and will be expanded to include the bot owner's ID and more if needed.
# The if statement is meant to not retrieve values from the file if it's empty (It should be empty with a manual installation.)
with open("config.txt", "r") as my_file:

    if os.stat("config.txt").st_size == 0:
        my_file.close()
    else:
        bot_token = my_file.readline().strip()
        bot_prefix = my_file.readline().strip()


# Creates client object to interact with the API using command_prefix of !.
client = commands.Bot(command_prefix=bot_prefix)
# Use http://discordpy.readthedocs.io/en/latest/api.html#client


# Returns info to the console when the bot is up and ready to run.

@client.event
async def on_ready():
    print("\nLogged in as")
    print(client.user.name)
    print(client.user.id)


# Simple command for adding two numbers. TODO - VERY specific syntax, need to fix that.
@client.command()
async def add(number1: int, number2: int):

    await client.say(number1 + number2)

# Command to shut down the bot. TODO - Make usable by bot owner only.


@client.command()
async def shutdown():

    await client.say("Roger that. Shutting down.")
    await client.logout()


# *, will invoke "consume rest" behavior and allow for
# strings with spaces in them to be used.
@client.command()
async def changestatus(*, gamename: str):

    await client.change_presence(game=Game(name=gamename))


# Will return the user's profile picture, or the profile picture of the user mentioned. TODO - Make it actually work.
@client.command()
async def profilepicture():

    await client.say("https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}"
                     ".png?size=1024".format(mention))


# Returns a fancy embed with bot information. TODO - Add more fields and figure out colors
@client.command()
async def info():

    infoembed = discord.Embed(
        description="Bot information. Click here for [GitHub Repository](https://github.com/BelleEpine/Akizuki).")

    infoembed.title = "Akizuki"

    infoembed.add_field(name="Server count", value=len(client.servers))

    infoembed.add_field(
        name="Invite link:", value="[Invite Me!](https://discordapp.com/oauth2/authorize?client_id=448598553493897216&permissions=0&scope=bot)", inline=False)

    await client.say(embed=infoembed)

# Prints deleted messages to the console.


@client.event
async def on_message_delete(message):
    print("Deleted message: ", message.content)


# Runs the bot using the token provided.
client.run(bot_token)
