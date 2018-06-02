"""Python file that acts as a cog for Akizuki. Defines the cog in a class called rngCog, and contains various commands that involve RNG, or a random number generator.

"""
# TODO - Implement more commands.

import discord
from discord.ext import commands
import random

class rngCog:
    """RNG Cog that has commands tailored for RNG operations."""

    def __init__(self, client):
        """
        Initializes class

        :param client: Discord bot client
        """
        self.client = client


    @commands.command()
    async def randomnumber(self):
        """
        Uses randint to return a random integer to the user.

        :return: void function.
        """

        randominteger = random.randint(1,100)

        await self.client.say(randominteger)


def setup(client):
    client.add_cog(rngCog(client))
