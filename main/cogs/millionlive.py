"""Cog for a server I own. :)

You can use this on master build, but it'll be next to useless.
'"""

import os

import discord
from discord.ext import commands

import random
from random import choices
from collections import Counter


class millionCog():

    def __init__(self, cogclient):

        self.client = cogclient

        self.rarities = ["R", "SR", "Limited SSR", "Permanent SSR"]
        self.normalweights = [.85, .12, .03]

    @commands.command(pass_context=True)
    async def sticker(self, ctx, *, stickername: str = None):
        """Command for sending stickers. Random if none is specified."""

        if stickername is None:
            imagename = random.choice(os.listdir("cogs/millionlive/MLstickers"))
        else:
            valid = False
            for x in os.listdir("cogs/millionlive/MLstickers"):
                if stickername.lower() == x.split(".")[0].lower(): # Deals with case by ignoring any case.
                    imagename = x
                    valid = True

            if not valid:
                await self.client.say("That is not a valid sticker name!")


        with open("cogs/millionlive/MLstickers/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f)

    @commands.command()
    async def stickerlist(self):
        """Lists the avaliable stickers."""

        stickerembed = discord.Embed(color=14434903)

        namestring = ""

        for sticker in os.listdir("cogs/millionlive/MLstickers"):
            namestring += sticker.split(".")[0] + "\n"

        stickerembed.add_field(name="**Sticker List:**", value=namestring)

        await self.client.say(embed=stickerembed)



'''
    @commands.command()
    async def gacha(self, rolls: int = None):

        if rolls is None:

            return currentgachapool

        if rolls >= 10 and rolls % 10 != 0:
            return "enter up to ten rolls or a multiple of ten."

        else:
            roll=choices(self.rarities, self.normalweights, rolls):

            condensedrolls = Counter(choices)

            countR = condensedrolls["R"]

            countSR = condensedrolls["SR"]

            countSSR = condensedrolls["SSR"]

            listR = []
            listSR = []
            listSSR = []

            for num in countR:
                listR.append(random.choice(masterlistR))

            for num in countSR:
                listSR.append(random.choice(masterlistSR))

            for num in countSSR:
                listSSR.append(random.choice(masterlistSSR))
'''


def setup(client):
    client.add_cog(millionCog(client))





