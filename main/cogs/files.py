"""My first full blown cog that I wrote for this bot. Defines the filesCog class where all the commands are located. This cog revolves around file interaction, which is things like storing user tags,
    and hopefully soon, interacting with files and more.
"""
# TODO - Maybe just change filesCog to a tag cog if it gets too large?

import discord
from discord.ext import commands
from discord import Client
import json

class FilesCog:
    """Used to define commands that interact with files. Currently, it's focused on tags, allowing for users to make tags, delete them, edit them, get info on them, and list all the tags."""

    def __init__(self, client):
        """Initializes everything."""

        self.client = client

        with open("config.json", "r") as my_file:

            try:
                data = json.load(my_file)
                self.ownerid = data["Owner ID"]

            except Exception as e:
                print("An error has occured. {0}".format(e))
                my_file.close()

        self.server_id_list = []

        # Gathers all the servers the bot is in to create a dictionary out of the string values.
        for server in self.client.servers:

            self.server_id_list.append(server.id)

        self.tagdicts = []

        for server in self.client.servers:
            try:
                with open("cogs/tags/{0}.json".format(server.id), "r") as mytags:
                    try:
                        data = json.load(mytags)
                    except ValueError:
                        data = {}
                    self.tagdicts.append( {server.id: data} )

            except FileNotFoundError:
                with open("cogs/tags/{0}.json".format(server.id), "a+") as mytags:
                    print("New tags file created: {0}".format(server.id))
                    self.tagdicts.append( {server.id: None} )

            except Exception as e:
                print("An error has occured. {0}".format(e))
                continue

        print("Total of {0} tag dictionaries loaded.".format(len(self.server_id_list)), self.server_id_list)

    # pass_context allows for ctx to be used in functions
    # invoke_without_command allows for the tag command to be called by itself and not call itself when other subcommands are called.
    # @commands.group(pass_context=True, invoke_without_command=True)
    @commands.command(pass_context=True)
    async def tag(self, ctx, name):
            """
            Master command for the tag group of commands.
            Checks for a passed tag name value and subcommand. If a tag name is passed, it will print the tag.
            If a subcommand is passed, then nothing here will run.
            """

            workingdictionary = None
            for counter, value in enumerate(self.tagdicts):
                if ctx.message.server.id in value:
                    workingdictionary = value
                    workingid = ctx.message.server.id

            try:
                await self.client.say(workingdictionary[workingid][name]["content"])
            except KeyError:
                print("That tag does not exist!")

    # @tag.command(pass_context=True)
    @commands.command(pass_context=True)
    async def tagadd(self, ctx, name: str, *, contents: str):
        """Subcommand allowing for the user to add new tags."""

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        if workingdictionary[workingid] is None:
            data = {}
            workingdictionary[workingid] = {}

            newtag = {name: {"content": contents, "authorid": ctx.message.author.id,"authorname": "{0}#{1}".format(ctx.message.author.name, ctx.message.author.discriminator)}}
            data.update(newtag)

        elif name not in workingdictionary[workingid]:
            with open("cogs/tags/{0}.json".format(ctx.message.server.id)) as mytags:
                try:
                    data = json.load(mytags)
                except ValueError:
                    data = {}
                except Exception as e:
                    print("An error has occurred - {0}".format(e))

            newtag = {name: {"content": contents, "authorid": ctx.message.author.id, "authorname": "{0}#{1}".format(ctx.message.author.name, ctx.message.author.discriminator)}}
            data.update(newtag)

        with open("cogs/tags/{0}.json".format(ctx.message.server.id), "w") as mytags:
            json.dump(data, mytags, indent=2)

        workingdictionary[workingid][name] = {"content": contents, "authorid": ctx.message.author.id, "authorname": "{0}#{1}".format(ctx.message.author.name, ctx.message.author.discriminator)}

        await self.client.say("Tag with name **{0}** and content **{1}** has been created.".format(name, contents))

   # @tag.command(pass_context=True)
    @commands.command(pass_context=True)
    async def tagdelete(self, ctx, name: str):
        """Subcommand allowing for the user to delete their tags."""

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        if ctx.message.author.id != workingdictionary[workingid][name]["authorid"]:
            if ctx.message.author.id == self.ownerid:
                pass
            else:
                await self.client.say("Sorry, you don't have sufficient permissions to use this command! Only the owner, **{0}** can.".format(workingdictionary[workingid][name]["authorname"]))
                return

        try:
            with open("cogs/tags/{0}.json".format(ctx.message.server.id)) as mytags:
                try:
                    data = json.load(mytags)
                except ValueError:
                    data = {}

            data.pop(name, None)

            with open("cogs/tags/{0}.json".format(ctx.message.server.id), "w") as mytags:
                json.dump(data, mytags, indent=2)

            workingdictionary[workingid].pop(name, None)
            await self.client.say("Your tag **{0}** has been deleted.".format(name))

        except KeyError:
            await self.client.say("That tag does not exist!")

    # @tag.command(pass_context=True)
    @commands.command(pass_context=True)
    async def tagedit(self, ctx, name: str, *, newcontent: str):
        """Used to edit an existing tag."""

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        if ctx.message.author.id != workingdictionary[workingid][name]["authorid"]:
            if ctx.message.author.id == self.ownerid:
                pass
            else:
                await self.client.say("Sorry, you don't have sufficient permissions to use this command! Only the owner, **{0}** can.".format(workingdictionary[workingid][name]["authorname"]))
                return

        try:

            with open("cogs/tags/{0}.json".format(ctx.message.server.id)) as mytags:
                try:
                    data = json.load(mytags)
                except ValueError:
                    data = {}

            data[name]["content"] = newcontent

            with open("cogs/tags/{0}.json".format(ctx.message.server.id), "w") as mytags:
                json.dump(data, mytags, indent=2)

            workingdictionary[workingid][name]["content"] = newcontent

            await self.client.say("Your tag **{0}** has had its contents changed to **{1}**".format(name, newcontent))

        except KeyError:
            await self.client.say("That tag does not exist!")

    # @tag.command(pass_context=True)
    @commands.command(pass_context=True)
    async def taglist(self, ctx):
        """Lists all the current tags in a nice embed."""

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        # Basically, a giant string will be sent in the embed.
        keystring = ""

        if workingdictionary[workingid] is None:
            keystring = "No tags currently exist!"
        elif len(workingdictionary[workingid]) == 0:
            keystring = "No tags currently exist!"
        else:
            for key in workingdictionary[workingid]:
                keystring += key
                keystring += "\n"

        listembed = discord.Embed(
            description="List of the currently stored tags.",
            color=14434903)

        listembed.title = "Here Be Tags"

        listembed.add_field(name="Tag list:", value=keystring)

        await self.client.say(embed=listembed)

    # @tag.command(pass_context=True)
    @commands.command(pass_context=True)
    async def taginfo(self, ctx, name: str):
        """Provides the user with information about the tag they pass in an embed"""

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            if ctx.message.server.id in value:
                workingdictionary = value
                workingid = ctx.message.server.id

        try:
            if name in workingdictionary[workingid]:
                infoembed = discord.Embed(color=14434903)

                infoembed.title = "Information for tag: **{0}**".format(name)

                infoembed.add_field(name="**Tag:**", value=name)
                infoembed.add_field(name="**Contents:**", value=workingdictionary[workingid][name]["content"], inline=False)
                infoembed.add_field(name="**Author:**", value=workingdictionary[workingid][name]["authorname"])

                await self.client.say(embed=infoembed)

        except KeyError:
            await self.client.say("That tag does not exist!")

    async def on_server_join(self, server):
        """Event trigger to help with the bug of tags not working when the bot joins a server while running."""

        try:
            with open("cogs/tags/{0}.json".format(server.id)) as f:
                try:
                    data = json.load(f)
                except ValueError:
                    data = {}
                self.tagdicts.append( {server.id: data} )
                print("New server joined, but there's already an existing tag file. Tag file {0} has been loaded.".format(server.id))

        except FileNotFoundError:
            with open("cogs/tags/{0}.json".format(server.id), "a+") as f:
                print("New tags file created on server join: {0}".format(server.id))
                self.tagdicts.append( {server.id: None} )

        except Exception as e:
            print("An error has occurred. {0}".format(e))



def setup(client):
    client.add_cog(FilesCog(client))
