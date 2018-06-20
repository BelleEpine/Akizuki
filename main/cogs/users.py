import discord
from discord.ext import commands

import datetime


class UserCog:
    """Cog meant to interact with the user data type in Discord. """

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def userinfo(self, ctx, member: discord.User = None):
        """Function meant to return information about a user, or if none is specified, the user who called the command."""

        if member is None:
            member = ctx.message.author

        userinfoembed = discord.Embed(color=member.color)

        userinfoembed.set_author(name="{0}#{1}".format(member.name, member.discriminator), icon_url=member.avatar_url)

        userinfoembed.set_thumbnail(url=member.avatar_url)

        userroles = ""
        for x in member.roles:
            userroles += x.name + "\n"

        # Personal note: inline defaults to true, if set to false will put the field on a separate line.
        userinfoembed.add_field(name="**Username:**", value="{0}#{1}".format(member.name, member.discriminator))
        userinfoembed.add_field(name="**Nickname:**", value=member.display_name)

        userinfoembed.add_field(name="**User ID:**", value=member.id)
        userinfoembed.add_field(name="**Status:**", value=member.status)

        userinfoembed.add_field(name="**Join Date:**", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S%Z"))  # can add .%f for microseconds but that messes up formatting :p
        userinfoembed.add_field(name="**Creation Date:**", value=str(member.created_at)[0:19])          # For ex, 2016-01-29 16:21:03.342000 will be cut down to 2016-01-29 16:21:03

        userinfoembed.add_field(name="**Game:**", value=member.game)
        userinfoembed.add_field(name="**Roles:**", value=userroles)

        userinfoembed.set_footer(text=datetime.datetime.now().strftime("Generated on: %Y-%m-%d, At: %H:%M:%S%Z"))

        await self.client.say(embed=userinfoembed)

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """Returns information on the server the command is called in."""

        serverinfoembed = discord.Embed(color=14434903)

        voicechannels = 0
        textchannels = 0

        for x in ctx.message.server.channels:
            if x.type == discord.ChannelType.text:
                textchannels += 1
            elif x.type == discord.ChannelType.voice:
                voicechannels += 1

        # Only prints up to 20, causes errors if too many roles or emojis.
        emojistring = ""
        for x in ctx.message.server.emojis[0:20]:
            emojistring += x.name + ": " + str(x) + "\n"

        rolestring = ""
        for x in ctx.message.server.roles[0:20]:
            rolestring += x.name + "\n"

        serverinfoembed.set_author(name="Server: {0}".format(ctx.message.server.name), icon_url=ctx.message.server.icon_url)

        serverinfoembed.set_thumbnail(url=ctx.message.server.icon_url)

        serverinfoembed.add_field(name="**Server Name:**", value=ctx.message.server.name)
        serverinfoembed.add_field(name="**Server Region:**", value=ctx.message.server.region)

        serverinfoembed.add_field(name="**Server ID:**", value=ctx.message.server.id)
        serverinfoembed.add_field(name="**Creation Date:**", value=str(ctx.message.server.created_at)[0:19])

        serverinfoembed.add_field(name="**Owner:**", value="{0}#{1}".format(ctx.message.server.owner.name, ctx.message.server.owner.discriminator))
        serverinfoembed.add_field(name="**Server Icon:**", value="[Click me!]({0})".format(ctx.message.server.icon_url))

        serverinfoembed.add_field(name="**Channels (Voice/Text)**", value="{0}/{1}".format(voicechannels, textchannels))
        serverinfoembed.add_field(name="**Member Count:**", value=str(len(ctx.message.server.members)))

        serverinfoembed.add_field(name="**Roles({0}) (This may not be the full list!):**".format(len(ctx.message.server.roles)), value=rolestring)
        serverinfoembed.add_field(name="**Emojis({0}) (This may not be the full list! Use the command !emojis to see all of them!):**".format(len(ctx.message.server.emojis)), value=emojistring)

        serverinfoembed.set_footer(text=datetime.datetime.now().strftime("Generated on: %Y-%m-%d, At: %H:%M:%S%Z"))

        await self.client.say(embed=serverinfoembed)

    @commands.command(pass_context=True)
    async def emojis(self, ctx):
        """Will return all of the emojis on the server, split into 1-25 and 26-50 to avoid the problem in !serverinfo."""

        emojistring1 = ""
        for x in ctx.message.server.emojis[0:25]:
            emojistring1 += x.name + ": " + str(x) + "\n"

        emojistring2 = ""
        for x in ctx.message.server.emojis[25:]:
            emojistring2 += x.name + ": " + str(x) + "\n"

        if emojistring1 is not "":
            await self.client.say("**Emojis 1-25:**" + "\n" + emojistring1)
        if emojistring2 is not "":
            await self.client.say("**Emojis 26-50:**" + "\n" + emojistring2)

    @commands.command(pass_context=True)
    async def profilepicture(self, ctx, member: discord.User = None):
        """Returns profile picture of the mentioned user, or the message author themself if none is specified."""

        if member is None:
            member = ctx.message.author

        await self.client.say(member.avatar_url)


def setup(client):
    client.add_cog(UserCog(client))