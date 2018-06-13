"""Cog for a server I own. :)"""

import discord
from discord.ext import commands

class millionCog():

    def __init__(self,client):
        self.client = client



def setup(client):
    client.add_cog(millionCog(client))