import discord
from discord.ext import commands
from discord.utils import get

import datetime
import json
import math

"""Personal note:  these are the limits for embeds: Number of fields = 25, field name = 256, value = 1024, description = 2048"""


class UserCog:
    """Cog meant to interact with the user data type in Discord. """

    def __init__(self, client):
        self.client = client

        self.server_id_list = []

        # Gathers all the servers the bot is in to create a dictionary out of the string values.
        for server in self.client.servers:
            self.server_id_list.append(server.id)

        # Gathers all the servers the bot is in, and creates a dictionary in the list. List contents: Server ID: [list of iam roles here], etc, etc
        self.roledicts = []

        for server in self.client.servers:
            try:
                with open("cogs/iam/{0}.json".format(server.id), "r") as mytags:
                    try:
                        data = json.load(mytags)
                    except ValueError:
                        data = []
                    self.roledicts.append({server.id: data})

            except FileNotFoundError:
                with open("cogs/iam/{0}.json".format(server.id), "a+") as mytags:
                    data = []
                    print("New iam file created: {0}".format(server.id))
                    self.roledicts.append({server.id: data})

            except Exception as e:
                print("An error has occured. {0}".format(e))
                continue

        print("Total of {0} role dictionaries loaded.".format(len(self.server_id_list)), self.server_id_list)

    @commands.command(pass_context=True)
    async def userinfo(self, ctx, member: discord.User = None):
        """Function meant to return information about a user, or if none is specified, the user who called the command."""

        if member is None:
            member = ctx.message.author

        userinfoembed = discord.Embed(color=member.color)

        userinfoembed.set_author(name="{0}#{1}".format(member.name, member.discriminator), icon_url=member.avatar_url)

        userinfoembed.set_thumbnail(url=member.avatar_url)

        role_list = []
        for x in member.roles:
            role_list.append(x)

        for x in role_list:
            if x.is_everyone:
                role_list.pop(role_list.index(x))

        userroles = ""
        for x in role_list:
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
        for x in ctx.message.server.emojis[0:10]:
            emojistring += x.name + ": " + str(x) + "\n"

        role_list = []
        for x in ctx.message.server.roles[0:11]:
            role_list.append(x)

        for x in role_list:
            if x.is_everyone:
                role_list.pop(role_list.index(x))

        rolestring = ""
        for x in role_list:
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

        serverinfoembed.add_field(name="**Roles:**", value="{0}".format(len(ctx.message.server.roles)))
        serverinfoembed.add_field(name="**Emojis:**", value="{0}".format(len(ctx.message.server.emojis)))

        serverinfoembed.set_footer(text=datetime.datetime.now().strftime("Generated on: %Y-%m-%d, At: %H:%M:%S%Z"))

        await self.client.say(embed=serverinfoembed)

    @commands.command(pass_context=True)
    async def emojis(self, ctx):
        """Will return all of the emojis on the server, split into 1-25 and 26-50 to avoid hitting the character limit."""

        emojistring1 = ""
        for x in ctx.message.server.emojis[0:25]:
            emojistring1 += x.name + " " + str(x) + "\n"

        emojistring2 = ""
        for x in ctx.message.server.emojis[25:50]:
            emojistring2 += x.name + " " + str(x) + "\n"

        emojistring3 = ""
        for x in ctx.message.server.emojis[50:75]:
            emojistring3 += x.name + " " + str(x) + "\n"

        emojistring4 = ""
        for x in ctx.message.server.emojis[75:]:
            emojistring4 = x.name + " " + str(x) + "\n"

        if emojistring1 is "" and emojistring2 is "":
            await self.client.say("No emojis currently exist on the server!")

        if emojistring1 is not "":
            await self.client.say("**Emojis 1-25:**\n{0}".format(emojistring1))
        if emojistring2 is not "":
            await self.client.say("**Emojis 25-50:**\n{0}".format(emojistring2))
        if emojistring3 is not "":
            await self.client.say("**Emojis 50-75:**\n{0}".format(emojistring3))
        if emojistring4 is not "":
            await self.client.say("**Emojis 75-100:**\n{0}".format(emojistring4))
        elif emojistring1 is "":
            await self.client.say("No emojis currently exist on the server!")

    @commands.command(pass_context=True)
    async def roles(self, ctx):
        """Will list all of the roles on the server."""

        # Function for dividing the roles into several shorter lists.
        def chunks(l, n):
            for i in range(0, len(l), n):
                yield l[i:i + n]

        rolenames = []
        for x in ctx.message.server.roles:
            if x.is_everyone:
                continue
            rolenames.append(x.name)

        rolenames_split = list(chunks(rolenames, 20))

        # Sends own embed for each set.
        for set in rolenames_split:
            rolestring = ""

            for role in set:
                rolestring += role + "\n"

            roleembed = discord.Embed(color=14434903)
            roleembed.add_field(name="**Roles:**", value=rolestring)

            roleembed.set_footer(text=datetime.datetime.now().strftime("Generated on: %Y-%m-%d, At: %H:%M:%S%Z"))
            await self.client.say(embed=roleembed)

    @commands.command(pass_context=True)
    async def profilepicture(self, ctx, member: discord.User = None):
        """Returns profile picture of the mentioned user, or the message author themself if none is specified."""

        if member is None:
            member = ctx.message.author

        await self.client.say(member.avatar_url)

    @commands.command(pass_context=True)
    async def iam(self, ctx, *, role: discord.Role = None):
        """Self-assignable roles."""

        if role is None:
            await self.client.say("You must enter a role!")
            return

        if role in ctx.message.author.roles:
            await self.client.say("You already have this role!")
            return

        # Enumerates over self.roledicts to look for the value which matches the ctx server ID

        workingdictionary = None
        for counter, value in enumerate(self.roledicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        if role.name in workingdictionary[workingid]:
            await self.client.add_roles(ctx.message.author, get(ctx.message.server.roles, name=role.name))
            await self.client.say("You now have the **{0}** role!".format(role.name))
        else:
            await self.client.say("You cannot assign yourself that role!")
            return

    @commands.command(pass_context=True)
    async def iamn(self, ctx, *, role: discord.Role = None):
        """Removes the role."""

        if role is None:
            await self.client.say("You must enter a role!")
            return

        if role not in ctx.message.author.roles:
            await self.client.say("You don't have this role!")
            return

        workingdictionary = None
        for counter, value in enumerate(self.roledicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        if role.name in workingdictionary[workingid]:
            await self.client.remove_roles(ctx.message.author, get(ctx.message.server.roles, name=role.name))
            await self.client.say("You now *don't* have the **{0}** role!".format(role.name))
        else:
            await self.client.say("That role is not assignable in the first place!")
            return

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def asar(self, ctx, *, role: discord.Role = None):
        """Adds role to list of SAR"""

        if role is None:
            await self.client.say("You must enter a role!")
            return
        elif role not in ctx.message.server.roles:
            await self.client.say("That roles does not exist!")
            return

        workingdictionary = None
        for counter, value in enumerate(self.roledicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        if role in workingdictionary[workingid]:
            await self.client.say("That role is already on the list!")
            return

        if role in ctx.message.server.roles:
            workingdictionary[workingid].append(role.name)
            await self.client.say("The **{0}** role has been added to the list.".format(role.name))

        with open("cogs/iam/{0}.json".format(ctx.message.server.id)) as f:
            try:
                data = json.load(f)
            except ValueError:
                data = []
            except Exception as e:
                print("An error has occurred - {0}".format(e))

        data.append(role.name)

        with open("cogs/iam/{0}.json".format(ctx.message.server.id), "w") as f:
            json.dump(data, f, indent=2)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def rsar(self, ctx, *, role: discord.Role = None):
        """Removes role from list of SAR"""

        workingdictionary = None
        for counter, value in enumerate(self.roledicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        if role in ctx.message.server.roles:
            workingdictionary[workingid].pop(workingdictionary[workingid].index(role.name))
            await self.client.say("The **{0}** role has been removed from the list.".format(role.name))

        with open("cogs/iam/{0}.json".format(ctx.message.server.id)) as f:
            try:
                data = json.load(f)
            except ValueError:
                data = []
            except Exception as e:
                print("An error has occurred - {0}".format(e))

        data.pop(data.index(role.name))

        with open("cogs/iam/{0}.json".format(ctx.message.server.id), "w") as f:
            json.dump(data, f, indent=2)

    @commands.command(pass_context=True)
    async def lsar(self, ctx):
        """Lists all the ASR"""

        workingdictionary = None
        for counter, value in enumerate(self.roledicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        def chunks(l, n):
            for i in range(0, len(l), n):
                yield l[i:i + n]

        split_lsar = list(chunks(workingdictionary[workingid], 20))

        for set in split_lsar:
            rolestring = ""

            for role in set:
                rolestring += role + "\n"

            roleembed = discord.Embed(color=14434903)

            if rolestring is "":
                rolestring = "None, currently!"

            roleembed.add_field(name="**Self Assignable Roles:**", value=rolestring)

            roleembed.set_footer(text=datetime.datetime.now().strftime("Generated on: %Y-%m-%d, At: %H:%M:%S%Z"))
            await self.client.say(embed=roleembed)

        if len(split_lsar) == 0:
            roleembed = discord.Embed(color=14434903)

            rolestring = "None, currently!"

            roleembed.add_field(name="**Self Assignable Roles:**", value=rolestring)

            roleembed.set_footer(text=datetime.datetime.now().strftime("Generated on: %Y-%m-%d, At: %H:%M:%S%Z"))
            await self.client.say(embed=roleembed)

    async def on_server_join(self, server):
        """Event trigger to deal with joined servers and created json files."""

        try:
            with open("cogs/iam/{0}.json".format(server.id)) as f:
                try:
                    data = json.load(f)
                except ValueError:
                    data = []
                self.roledicts.append( {server.id: data} )
                print("New server joined, but there's already an existing roles file. Role file {0} has been loaded.".format(server.id))

        except FileNotFoundError:
            with open("cogs/iam/{0}.json".format(server.id), "a+") as f:
                print("New roles file created on server join: {0}".format(server.id))
                data = []
                self.roledicts.append( {server.id: data} )

        except Exception as e:
            print("An error has occurred. {0}".format(e))


def setup(client):
    client.add_cog(UserCog(client))