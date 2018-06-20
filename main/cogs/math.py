# TODO - Fix expression command, and interaction with negative numbers.
# TODO - Add more commands!

import discord
from discord.ext import commands
import math
import re


class MathCog:
    """
        Used for math functions such as adding, subtracting, multiplying, and dividing.
        Uses regexes for more friendly interaction.
        I currently have an expression command utilizing Python's built in parser, but doesn't work too well currently.
        It has quite a few problems, like interacting with negative numbers will mess up sometimes. I'll have to look into that.
    """

    def __init__(self, client):

        self.client = client
        self.simpleRegex = re.compile(r'''
                                                    ([-]?   # Checks for negative number
                                                    [0-9]*  # Integer part of number
                                                    \.?[0-9]+)+ #Decimal part of number
                                                    ''', re.VERBOSE)

    @commands.command()
    async def expression(self, expression: str):
        """Uses a parser to solve more complicated equations. With the built in Python one, it's not that good."""

        # Will use parser for more complicated equations.
        compiledequation = compile(expression, "math.py", "eval")

        await self.client.say(eval(compiledequation))

    @commands.command()
    async def add(self, *args):
        """Adds numbers."""

        if len(list(args)) == 0:
            await self.client.say("0")
            return

        # String to be passed to regex, will include all the user parameters.
        regexstring = ""

        for x in list(args):
            regexstring += str(x) + " "

        mo = self.simpleRegex.findall(regexstring)

        for x in mo:
            x.strip()

        total = float(mo[0])

        for x in mo[1:]:
            total += float(x)

        await self.client.say(total)

    @commands.command()
    async def subtract(self, *args):
        """Subtracts numbers."""

        if len(list(args)) == 0:
            await self.client.say("0")
            return

        regexstring = ""
        for x in list(args):
            regexstring += str(x) + " "

        mo = self.simpleRegex.findall(regexstring)

        for x in mo:
            x.strip()

        total = float(mo[0])

        for x in mo[1:]:
            total -= float(x)

        await self.client.say(total)

    @commands.command()
    async def multiply(self, *args):
        """Multiplies numbers."""

        if len(list(args)) == 0:
            await self.client.say("0")
            return

        regexstring = ""
        for x in list(args):
            regexstring += str(x) + " "

        mo = self.simpleRegex.findall(regexstring)

        for x in mo:
            x.strip()

        total = float(mo[0])

        for x in mo[1:]:
            total *= float(x)

        await self.client.say(total)

    @commands.command()
    async def divide(self, *args):
        """Divides numbers."""

        if len(list(args)) == 0:
            await self.client.say("0")
            return

        regexstring = ""
        for x in list(args):
            regexstring += str(x) + " "

        mo = self.simpleRegex.findall(regexstring)

        for x in mo:
            x.strip()

        total = float(mo[0])

        for x in mo[1:]:
            total /= float(x)

        await self.client.say(total)


def setup(client):
    client.add_cog(MathCog(client))
