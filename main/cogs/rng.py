# TODO - Implement more commands.

import discord
from discord.ext import commands
import random


class RNGCog:
    """RNG Cog that has commands tailored for RNG operations."""

    def __init__(self, client):
        """
        Initializes class

        :param client: Discord bot client
        """
        self.client = client


    @commands.command()
    async def randomnumber(self):
        """Uses randint to return a random integer to the user."""

        randominteger = random.randint(1,100)

        await self.client.say(randominteger)


def setup(client):
    client.add_cog(RNGCog(client))
