""" Discord Bot written by Tim in Python. GitHub :."""
# TODO MAKE SURE TO .GITIGNORE LOCAL CONFIG.PY MAKE BAT FILE OR GUI TO CREATE NEW CONFIG.PY
# OPTIONS - Upload config.py as empty, DO NOT STAGE LOCAL ONE and have the bat/python gui update it
# OR - have bat/python gui make the config.py file - but one con is the user is forced to do it that way, can't do it manually/


# TODO - Allow user to set up configurations (Enter own token, prefix, and user_id into a GUI or console and change them here
# TODO - More on-event responses
# TODO - Interact with other files More
# TODO - Require administrator perms for some commands
# TODO - **Make the project structure look better and make more sense**
# TODO - Make this a main file with cogs in other files?
# TODO - Make a class out of the bot setup and just make an instance of the bot?
# TODO - More nice looking help command. Maybe in an embed? Or just keep it simple in a code block or something.

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
with open("config.txt", "r") as my_file:

    if os.stat("config.txt").st_size == 0: # Will not use file if empty
        my_file.close()
    else:
        bot_token = my_file.readline().strip()
        bot_prefix = my_file.readline().strip()

# Creates client object to interact with the API
client = commands.Bot(command_prefix=bot_prefix)

# Defines the cogs to be loaded when the bot starts up.
bot_cogs = ["cogs.rng", "cogs.files", "cogs.math"]

# Loads all the cogs. What is a cog you may ask? Well, a cog is an extention to a bot that can be used to organize commands, or be shared with others! They're great.
for cog in bot_cogs:
    client.load_extension(cog)


@client.event
async def on_ready():
    """
     Returns info to the console when the bot is up and ready to run.

    :return: void function.
    """
    print("\nLogged in as")
    print(client.user.name)
    print(client.user.id)

# TODO - Make usable by bot owner only.
@client.command()
async def shutdown():
    """
    Shuts the bot down.

    :return: void function.
    """
    await client.say("Roger that. Shutting down.")
    await client.logout()

# TODO - Other statuses like streaming? Set away/do not disturb/etc.
@client.command()
async def changestatus(*, gamename: str):
    """
    Allows for the user to change the bot's "Playing: " status to whatever they choose.
    *, will invoke "consume rest" behavior and allow for strings with spaces in them to be used.

    :param gamename: Name of a game to set the bot's status as "playing".
    :return:  void function.
    """

    await client.change_presence(game=Game(name=gamename))


# TODO - Make it actually work.
@client.command()
async def profilepicture():
    """
    Will return the user's profile picture, or the profile picture of the user mentioned.

    :return: void function
    """

    await client.say("https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}"
                     ".png?size=1024".format(mention))



# TODO - Add more fields
@client.command()
async def info():
    """
    Returns a fancy embed with bot information.

    :return:  void function.
    """

    infoembed = discord.Embed(
        description="Bot information. Click here for [GitHub Repository](https://github.com/BelleEpine/Akizuki).", color = 0xBEA4FA)

    infoembed.title = "Akizuki"

    # noinspection PyTypeChecker
    infoembed.add_field(name="Server count", value=len(client.servers))

    infoembed.add_field(
        name="Invite link:", value="[Invite Me!](https://discordapp.com/oauth2/authorize?client_id=448598553493897216&permissions=0&scope=bot)", inline=False)

    await client.say(embed=infoembed)

@client.event
async def on_message_delete(message):
    """
    Will print deleted messages to the console.

    :param message: Message automatically passed to the function by the client.event
    :return:
    """
    print("Deleted message: ", message.content)




client.run(bot_token)
