import discord
from discord.ext import commands
import os
import random

# TODO - More shrug pictures.


class ActionCog:
    """ Cog centered around interacting with users by allowing for them to use a variety of action commands. """

    def __init__(self, client):

        self.client = client

    @commands.command(pass_context=True)
    async def angry(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/angry"))

        if member is None:
            imagestring = "**{0} is angry!**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} is angry at {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/angry/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def blush(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/blush"))

        if member is None:
            imagestring = "**{0} is blushing.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} blushes at {1}.**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/blush/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def cry(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/cry"))

        if member is None:
            imagestring = "**{0} is crying.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} cries to {1}.**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/cry/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def dance(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/dance"))

        if member is None:
            imagestring = "**{0} is dancing!**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} dances for {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/dance/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def hug(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/hug"))

        if member is None:
            imagestring = "**{0} wants a hug. Here's a hug.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} gives a hug to {1}.**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/hug/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def idol(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/idol"))

        if member is None:
            imagestring = "**{0} puts on a performance!**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} puts on a performance for {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/idol/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def kiss(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/kiss"))

        if member is None:
            imagestring = "**{0} wants a kiss. Here's a kiss.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} kisses {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/kiss/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def laugh(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/laugh"))

        if member is None:
            imagestring = "**{0} laughs uncontrollably!**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} breaks out laughting at {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/laugh/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def pat(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/pat"))

        if member is None:
            imagestring = "**{0} wants a pat. Here's a pat.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} pats {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/pat/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def pout(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/pout"))

        if member is None:
            imagestring = "**{0} starts pouting!**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} pouts at {1}.**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/pout/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def shrug(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/shrug"))

        if member is None:
            imagestring = "**{0} shrugs.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} shrugs at {1}.**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/shrug/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def slap(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/slap"))

        if member is None:
            imagestring = "**{0} slaps themselves.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} slaps {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/slap/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def smile(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/smile"))

        if member is None:
            imagestring = "**{0} smiles.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} smiles at {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/smile/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def squeal(self, ctx, member: discord.User = None):
        """For when there's just too much sweetness."""

        imagename = random.choice(os.listdir("cogs/action/several/squeal"))

        if member is None:
            imagestring = "**{0} is squealing in happiness!**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} is squealing in happiness at {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/squeal/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)

    @commands.command(pass_context=True)
    async def wink(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/wink"))

        if member is None:
            imagestring = "**{0} winks.**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} winks at {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/wink/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)


    ''' 
    Template
    @commands.command(pass_context=True)
    async def ACTIONNAMEHERE(self, ctx, member: discord.User = None):

        imagename = random.choice(os.listdir("cogs/action/several/ACTIONFOLDERHERE"))

        if member is None:
            imagestring = "**{0} DOES SOMETHING**".format(ctx.message.author.mention)
        else:
            imagestring = "**{0} DOES SOMETHING for {1}!**".format(ctx.message.author.mention, member.name)

        with open("cogs/action/several/ACTIONFOLDERHERE/{0}".format(imagename), "rb") as f:
            await self.client.send_file(ctx.message.channel, f, content=imagestring)
    '''

def setup(client):
    client.add_cog(ActionCog(client))