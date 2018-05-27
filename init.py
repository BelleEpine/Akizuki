import logging
import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO)


bot_token = "ENTER BOT TOKEN HERE."


bot = commands.Bot(command_prefix="!", description="Temp,.")


@bot.event
async def on_ready():
    print("\nLogged in as")
    print(bot.user.name)
    print(bot.user.id)


@bot.command()
async def add(number1: int, number2: int):

    await bot.say(number1 + number2)


@bot.command()
async def shutdown():

    await bot.say("Roger that. Shutting down.")
    await bot.logout()


# problematic.
@bot.command()
async def profilepicture(mention):

    print(mention)

    await bot.say("https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?"
                  "size=1024".format(mention))




@bot.event
async def on_message_delete(message):
    print("Deleted message: ", message.content)


bot.run(bot_token)
