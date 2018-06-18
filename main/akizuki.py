""" Discord Bot written by Tim in Python. GitHub : https://github.com/BelleEpine/Akizuki"""

# TODO - More on-event responses
# TODO - Interact with other files More
# TODO - **Make the project structure look better and make more sense**
# TODO - Make a class out of the bot setup and just make an instance of the bot?
# TODO - More nice looking help command. Maybe in an embed? Or just keep it simple in a code block or something.

# TODO - Fix info command w/ invite link for bot.

import logging
import discord
from discord import Game
from discord.ext import commands

import os

"""
Personal Notes:
-Akizuki red is 14434903
"""

# Sets up logging in the console.

logging.basicConfig(level=logging.INFO)
logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)


# ENTER BOT TOKEN AND PREFIXES HERE (Manual set up)
bot_token = ""

bot_prefix = ""

ownerid = ""

# Obtains bot token and prefix from the config file. TODO - Can and will be expanded to include the bot owner's ID and more if needed.
with open("config.txt", "r") as my_file:

    if os.stat("config.txt").st_size == 0:  # Will not use file if empty
        my_file.close()
    else:
        bot_token = my_file.readline().strip()
        bot_prefix = my_file.readline().strip()
        ownerid = my_file.readline().strip()

# Creates client object to interact with the API
client = commands.Bot(command_prefix=bot_prefix)

# Defines the cogs to be loaded when the bot starts up.
bot_cogs = ["cogs.rng", "cogs.files", "cogs.math", "cogs.users", "cogs.millionlive.millionlive"]



@client.event
async def on_ready():
    """Returns info to the console when the bot is up and ready to run."""
    print("\nLogged in as")
    print(client.user.name)
    print(client.user.id)
    print("\n")
    print("------")
    print("\n")

    for cog in bot_cogs:
        client.load_extension(cog)

    print("Total of {0} cogs loaded.".format(len(bot_cogs)))



'''
@client.command(pass_context = True)
async def test(ctx):
    await client.say(type(ctx.message.author.id))
    await client.say(ctx.message.author.id)
    await client.say(ctx.message.author.id == ownerid)
    await client.say(ctx.message.author)

    if ctx.message.author.id == ownerid:
        await client.say("Hello!")
    else:
        await client.say("No..")

    await client.logout()
    '''


@client.command(pass_context=True)
async def shutdown(ctx):
    """
    Shuts the bot down.

    :param ctx: Passes command context.
    """

    if ctx.message.author.id == ownerid:
        await client.say("Roger that. Shutting down.")
        await client.logout()
    else:
        await client.say("Sorry, you don't have sufficient permissions to use this command!")


# TODO - Other statuses like streaming? Set away/do not disturb/etc.
@client.command(pass_context=True)
async def changepresence(ctx, status: str, *, gamename: str):
    """
    Allows for the user to change the bot's "Playing: " status to whatever they choose, as well as the online/idle/dnd status.
    *, will invoke "consume rest" behavior and allow for strings with spaces in them to be used.

    :param ctx: Passes command context.
    :param status: Status to set the bot to.
    :param gamename: Name of a game to set the bot's status as "playing".
    """
    if ctx.message.author.id == ownerid:
        await client.change_presence(game=Game(name=gamename), status=status)
    else:
        await client.say("Sorry, you don't have sufficient permissions to use this command!")


# TODO - Add more fields
@client.command()
async def info():
    """Returns a fancy embed with bot information."""

    # NEED TO USE RGB INT INSTEAD OF HEX
    infoembed = discord.Embed(
        description="Bot information. Click here for [GitHub Repository](https://github.com/BelleEpine/Akizuki).", color=14434903)

    infoembed.title = "Akizuki"

    # noinspection PyTypeChecker
    infoembed.add_field(name="Server count", value=len(client.servers))

    infoembed.add_field(
        name="Invite link:", value="[Invite Me!](https://discordapp.com/oauth2/authorize?client_id=448598553493897216&permissions=0&scope=bot)", inline=False)

    await client.say(embed=infoembed)


@client.command()
async def cogs():

    cogstring = ""
    for x in bot_cogs:
        cogstring += x[5:] + "\n"

    cogembed = discord.Embed(color=14434903)

    cogembed.set_footer(text="To get more info, do " + bot_prefix + "help [COGNAME]Cog.")

    cogembed.add_field(name="List of cogs:", value=cogstring)

    await client.say(embed=cogembed)


@client.command(pass_context=True)
async def ping(ctx):
    """
    Determines the bot's ping.

    :param ctx: Passes command context
    """
    resp = await client.say('Pong! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
    await client.edit_message(resp, f'Pong! That took {1000*diff.total_seconds():.1f}ms.')

"""
async: 
@bot.command(pass_context=True)
async def ping(ctx):
    resp = await bot.say('Pong! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
    await bot.edit_message(resp, f'Pong! That took {1000*diff.total_seconds():.1f}ms.')

rewrite:
@bot.command()
async def ping(ctx):
    resp = await ctx.send('Pong! Loading...')
    diff = resp.created_at - ctx.message.created_at
    await resp.edit(content=f'Pong! That took {1000*diff.total_seconds():.1f}ms.')
    """


# TODO I don't know. Just make it better I guess. Currently turned off.
@client.event
async def on_message_delete(message):
    """
    Will print deleted messages to the console.

    :param message: Message automatically passed to the function by the client.event
    """
    return  # Turned off for now.

    print("Deleted message: ", message.content)
    await client.process_commands(message)


@client.event
async def on_message(message):
    """
    Will make sure that the bot does not work in DMs, and cannot ping @everyone by accident.

    :param message: Message passed to the event call
    """

    if message.server is None:
        return

    if "@everyone" in message.content:
        return

    await client.process_commands(message)

client.run(bot_token)
