"""My first full blown cog that I wrote for this bot. Defines the filesCog class where all the commands are located. This cog revolves around file interaction, which is things like storing user tags,
    and hopefully soon, interacting with files and more.
"""
# TODO - Maybe just change filesCog to a tag cog if it gets too large?

import discord
from discord.ext import commands


class FilesCog:

    """
    Used to define commands that interact with files.
    Currently, it's focused on tags, allowing for users to make tags, delete them, edit them, get info on them, and list all the tags.
    """

    def __init__(self, client):
        """
        Initializes everything.

        :param client: The discord client passed to the class to run commands.
        """

        self.client = client
        self.server_id_list = []

        # Gathers all the servers the bot is in to create a dictionary out of the string values.
        for server in self.client.servers:

            self.server_id_list.append(server.id)

        self.untouched_server_id = []

        # A bit confusing, so bear with me. I want a nested list with the first value being the server ID, and the second being the server's tags.
        # This is so I can search ctx for the server id and then see if it's in any of the nested lists. If it is, I'll use that tag list for that server.
        for server in self.client.servers:
            self.untouched_server_id.append(server.id)

        self.tagdicts = []

        # Gets ownerid if needed in the future.
        self.ownerid = ""

        with open("{0}/config.txt".format("."), "r") as myconfig:
            myconfig.readline()
            myconfig.readline()
            self.ownerid = myconfig.readline().strip()

        # personal note: Since cog is loaded in akizuki.py which is a directory down, tags.txt is not in that directory and will not load. So, must specify the directory.
        # Tag storing format: title, content, creatorID, creatorUsername+Discriminator
        counter = 0
        for x in self.server_id_list:
            try:
                with open("cogs/tags/{0}.txt".format(x), "r") as mytags:
                    x = {}
                    for line in mytags:
                        currentline = line.rstrip().split(" HELLOTHEREIAMADIVIDER ")    # This is how the tags are stored. The giant divider is meant to prevent the .split() from unintentionally messing stuff up,
                        x[currentline[0]] = [currentline[1], currentline[2], currentline[3]]
                    self.tagdicts.append([self.untouched_server_id[counter], x])
                    counter += 1

            except FileNotFoundError:
                with open("cogs/tags/{0}.txt".format(x), "a+") as mytags:
                    print("New tags.txt file created:" + x)
                    x = {}
                    try:
                        self.tagdicts.append([self.untouched_server_id[counter], x])
                        counter += 1
                    except IndexError:
                        continue

        print("Total of {0} tag dictionaries loaded.".format(len(self.server_id_list)), self.server_id_list)

    # pass_context allows for ctx to be used in functions
    # invoke_without_command allows for the tag command to be called by itself and not call itself when other subcommands are called.
    @commands.group(pass_context=True, invoke_without_command=True)
    async def tag(self, ctx, name):
            """
            Master command for the tag group of commands.
            Checks for a passed tag name value and subcommand. If a tag name is passed, it will print the tag.
            If a subcommand is passed, then nothing here will run.

            :param ctx: ctx is used for checking stuff such as whether a subcommand is used or not.
            :param name: Name of the tag to be returned. Can be None assuming the user enters a subcommand.
            """

            workingdictionary = None
            # Searches the aforementioned nested lists for the ctx server. If it's there, it'll use that server as the current working dictionary.
            for counter, value in enumerate(self.tagdicts):
                try:
                    if ctx.message.server.id in value:
                        workingdictionary = value[1]
                except ValueError:
                    continue

            if ctx.invoked_subcommand is None:
                contentstring = workingdictionary.get(name)[0]

                if contentstring is not None:
                    await self.client.say(contentstring)
                else:
                    await self.client.say("That tag does not exist!")

    @tag.command(pass_context=True)
    async def add(self, ctx, name: str, *, contents: str):
        """
        Subcommand allowing for the user to add new tags.

        :param ctx: Command context
        :param name: Name of the tag to be added. Must be one word.
        :param contents: Contents of the tag to be added. Can be multiple words.
        """

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            try:
                if ctx.message.server.id in value:
                    workingdictionary = value[1]
            except ValueError:
                continue

        if name not in workingdictionary:
            with open("cogs/tags/{0}.txt".format(ctx.message.server.id), "a") as mytags:
                mytags.write(name + " HELLOTHEREIAMADIVIDER " + contents + " HELLOTHEREIAMADIVIDER " + ctx.message.author.id + " HELLOTHEREIAMADIVIDER " + ctx.message.author.name + "#" + ctx.message.author.discriminator + "\n")
            workingdictionary[name] = contents
        else:
            await self.client.say("This tag already exists! Use the subcommand edit to change existing tags.")

        await self.client.say("Tag with name **{0}** and content **{1}** has been created.".format(name, contents))

    @tag.command(pass_context=True)
    async def delete(self, ctx, name: str):
        """
        Subcommand allowing for the user to delete their tags.

        :param ctx: Command context
        :param name:  Name of the tag to be deleted.
        """

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            try:
                if ctx.message.server.id in value:
                    workingdictionary = value[1]
            except ValueError:
                continue

        if ctx.message.author.id != workingdictionary[name][1] or ctx.message.author.id != self.ownerid:
            await self.client.say("Sorry, you don't have sufficient permissions to use this command! Only the owner, **{0}** can.".format(workingdictionary.get(name)[2]))
            return

        linetodelete = ""
        linestokeep = []

        if name in workingdictionary:

            with open("cogs/tags/{0}.txt".format(ctx.message.server.id), "r+") as mytags:

                for line in mytags:
                    currentline = line.rstrip().split(" HELLOTHEREIAMADIVIDER ")
                    # Ensures right tag is being deleted by checking name AND content of the tag
                    # currentline right now is shown as [title , content].
                    if currentline[0] == name and currentline[1] == workingdictionary[name]:
                        linetodelete = line
                    else:
                        linestokeep.append(line)

            with open("cogs/tags/{0}.txt".format(ctx.message.server.id), "w") as mytags:
                for line in linestokeep:
                    if line != linetodelete:
                        mytags.write(line)

            workingdictionary.pop(name)
            await self.client.say("Your tag **{0}** has been deleted.".format(name))

    @tag.command(pass_context=True)
    async def edit(self, ctx, name: str, *, newcontent: str):

        """
        Used to edit an existing tag.

        :param ctx: Passes context
        :param name:  Name of tag to edit
        :param newcontent:  New content to replace the old content.
        """

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            try:
                if ctx.message.server.id in value:
                    workingdictionary = value[1]
            except ValueError:
                continue

        if ctx.message.author.id != workingdictionary[name][1] or ctx.message.author.id != self.ownerid:
            await self.client.say("Sorry, you don't have sufficient permissions to use this command! Only the owner, **{0}** can.".format(workingdictionary.get(name)[2]))
            return

        editedline = ""
        unchangedlines = []

        if name in workingdictionary:

            with open("cogs/tags/{0}.txt".format(ctx.message.server.id), "r") as mytags:

                for line in mytags:
                    currentline = line.rstrip().split(" HELLOTHEREIAMADIVIDER ")

                    # Again confirms it's the right tag being changed.
                    # currentline right now is shown as [title , content].
                    if currentline[0] == name and currentline[1] == workingdictionary[name]:
                        currentline[1] = newcontent
                        currentline.insert(1, " HELLOTHEREIAMADIVIDER ")

                        editedline = "".join(currentline)
                    else:
                        unchangedlines.append(line)

            with open("cogs/tags/{0}.txt".format(ctx.message.server.id), "w") as mytags:

                for line in unchangedlines:
                    if line != editedline:
                        if "\n" in line:  # In case one of the tags doesn't have a newline on it, to prevent it from being bunched up on a single line.
                            mytags.write(line)
                        else:
                            mytags.write(line + "\n")
                mytags.write(editedline)

            workingdictionary[name] = newcontent
            await self.client.say("Your tag **{0}** has had its contents changed to **{1}**".format(name, newcontent))

        else:
            await self.client.say("That tag does not exist!")

    @tag.command(pass_context=True)
    async def list(self, ctx):

        """Lists all the current tags in a nice embed."""

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            try:
                if ctx.message.server.id in value:
                    workingdictionary = value[1]
            except ValueError:
                continue

        # Basically, a giant string will be sent in the embed.
        keystring = ""

        if len(workingdictionary) == 0:
            keystring = "No tags currently exist!"
        else:
            for key in workingdictionary:
                keystring += key
                keystring += "\n"

        listembed = discord.Embed(
            description="List of the currently stored tags..",
            color=14434903)

        listembed.title = "Here Be Tags"

        listembed.add_field(name="Tag list:", value=keystring)

        await self.client.say(embed=listembed)

    @tag.command(pass_context=True)
    async def info(self, ctx, name: str):
        """
        Provides the user with information about the tag they pass in an embed!

        :param ctx: Command context
        :param name: Tag that the user will get information about.
        """

        workingdictionary = None

        for counter, value in enumerate(self.tagdicts):
            try:
                if ctx.message.server.id in value:
                    workingdictionary = value[1]
            except ValueError:
                continue

        if name in workingdictionary:
            infoembed = discord.Embed(color=14434903)

            infoembed.title = "Information for tag: **{0}**".format(name)

            infoembed.add_field(name="**Tag:**", value=name)
            infoembed.add_field(name="**Contents:**", value=workingdictionary.get(name)[0], inline=False)
            infoembed.add_field(name="**Author:**", value=workingdictionary.get(name)[2])

            await self.client.say(embed=infoembed)

        else:
            await self.client.say("That tag does not exist!")


def setup(client):
    client.add_cog(FilesCog(client))
