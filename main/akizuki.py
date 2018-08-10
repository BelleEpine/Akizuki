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
from discord.ext.commands.cooldowns import BucketType

import json

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
with open("config.json", "r") as my_file:

    try:
        data = json.load(my_file)
        bot_token = data["Bot Token"]
        bot_prefix = data["Bot Prefix"]
        ownerid = data["Owner ID"]

    except Exception as e:
        print("An error has occured. {0}".format(e))
        my_file.close()

# Creates client object to interact with the API
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

# Defines the cogs to be loaded when the bot starts up.
bot_cogs = ["cogs.rng", "cogs.files", "cogs.math", "cogs.users", "cogs.action", "cogs.millionlive", "cogs.wows"]
loaded_bot_cogs = []
unloaded_bot_cogs = []


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
        try:
            client.load_extension(cog)
            loaded_bot_cogs.append(cog)
        except Exception as e:
            print("Error loading module {0}. - {1}".format(cog, e))
    for cog in bot_cogs:
        client.load_extension(cog)

    print("Total of {0} cogs loaded.".format(len(bot_cogs)))


    await client.change_presence(game=Game(name="{0}help | with DesDiv 61".format(bot_prefix)))

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


@client.command(pass_context=True, hidden=True)
async def shutdown(ctx):
    """Shuts the bot down."""

    if ctx.message.author.id == ownerid:
        await client.say("Roger that. Shutting down.")
        await client.logout()
    else:
        await client.say("Sorry, you don't have sufficient permissions to use this command!")


# TODO - Other statuses like streaming? Set away/do not disturb/etc.
@client.command(pass_context=True, hidden=True)
async def changepresence(ctx, status: str, *, gamename: str):
    """Allows for the user to change the bot's "Playing: " status to whatever they choose, as well as the online/idle/dnd status.
*, will invoke "consume rest" behavior and allow for strings with spaces in them to be used.
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
        description="Bot information. [GitHub Repository](https://github.com/Yuzu/Akizuki).", color=14434903)

    infoembed.title = "Akizuki"

    # noinspection PyTypeChecker
    infoembed.add_field(name="Server count", value=len(client.servers))

    infoembed.add_field(
        name="Invite link:", value="[Invite Me!](https://discordapp.com/oauth2/authorize?client_id=448598553493897216&permissions=0&scope=bot)", inline=False)

    await client.say(embed=infoembed)


@client.command()
async def cogs():

    loaded_cogstring = ""
    for x in loaded_bot_cogs:
        loaded_cogstring += x[5:] + "\n"

    if loaded_cogstring == "":
        loaded_cogstring = "Nothing!"

    unloaded_cogstring = ""
    for x in unloaded_bot_cogs:
        unloaded_cogstring += x[5:] + "\n"

    if unloaded_cogstring == "":
        unloaded_cogstring = "Nothing!"

    cogembed = discord.Embed(color=14434903)

    cogembed.set_footer(text="To get more info, do " + bot_prefix + "help [COGNAME]Cog.")

    cogembed.add_field(name="List of loaded cogs:", value=loaded_cogstring)

    cogembed.add_field(name="List of unloaded cogs:", value=unloaded_cogstring)

    await client.say(embed=cogembed)


@client.command(pass_context=True, hidden=True)
async def unloadcog(ctx, cog: str):

    if ctx.message.author.id == ownerid:
        try:
            client.unload_extension("cogs.{0}".format(cog))
            loaded_bot_cogs.pop(loaded_bot_cogs.index("cogs.{0}".format(cog)))
            unloaded_bot_cogs.append("cogs.{0}".format(cog))

            await client.say("The {0} cog has been unloaded.".format(cog))

        except Exception as e:
            print(e)
            await client.say("An error has occured: {0}".format(e))
    else:
        await client.say("Sorry, you don't have sufficient permissions to use this command!")


@client.command(pass_context=True, hidden=True)
async def loadcog(ctx, cog: str):

    if ctx.message.author.id == ownerid:
        try:
            client.load_extension("cogs.{0}".format(cog))
            unloaded_bot_cogs.pop(unloaded_bot_cogs.index("cogs.{0}".format(cog)))
            loaded_bot_cogs.append("cogs.{0}".format(cog))

            await client.say("The {0} cog has been loaded.".format(cog))
        except Exception as e:
            print(e)
            await client.say("An error has occured: {0}".format(e))
    else:
        await client.say("Sorry, you don't have sufficient permissions to use this command!")


@client.command(pass_context=True, hidden=True)
async def reloadcog(ctx, cog: str):

    if ctx.message.author.id == ownerid:
        try:
            client.unload_extension("cogs.{0}".format(cog))
            client.load_extension("cogs.{0}".format(cog))
            await client.say("The {0} cog has been reloaded.".format(cog))
        except Exception as e:
            print(e)
    else:
        await client.say("Sorry, you don't have sufficient permissions to use this command!")


@client.command(pass_context=True)
async def ping(ctx):
    """Determines the bot's ping."""

    resp = await client.say('Pong! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
	
    ping = diff.microseconds / 1000
    await client.edit_message(resp, "Pong! That took {0} ms.".format(ping))



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

# TODO - Respond to illegitimate channel param
@client.command(pass_context=True)
async def echo(ctx, channel: discord.Channel = None, *, content: str = None):
    """Bot will copy whatever you say in a given channel."""

    if ctx.message.author.id != ownerid:
        await client.say("Sorry, you don't have sufficient permissions to use this command!")
        return

    if content is None:
        await client.say("You must enter a message to send!")
        return

    if "@everyone" in content or "@here" in content:
        await client.say("You cannot mention everyone or here!")
        return

    await client.send_message(channel, content=content)

@client.command()
async def help():

    helpembed = discord.Embed(
        description="Bot information. [GitHub Repository](https://github.com/Yuzu/Akizuki).", color=14434903)

    helpembed.title = "Akizuki"

    # noinspection PyTypeChecker
    helpembed.add_field(name="Click me for help with commands!", value="[Click me!](https://yuzu.github.io/Akizuki/)")

    helpembed.set_footer(text="Need more help? Contact yuzu#7200")

    await client.say(embed=helpembed)

# TODO I don't know. Just make it better I guess. Currently turned off.
@client.event
async def on_message_delete(message):
    """Will print deleted messages to the console."""

    return  # Turned off for now.

    print("Deleted message: ", message.content)
    await client.process_commands(message)


@client.event
async def on_message(message):
    """Will make sure that the bot does not work in DMs, and cannot ping @everyone by accident."""
    '''
    if message.author.id == "142665321931603968":
        await client.add_reaction(message, "\N{snowflake}")
        '''

    if message.server is None:
        return

    if "@everyone" in message.content:
        return
    


    await client.process_commands(message)



client.run(bot_token)
