"""My first full blown cog that I wrote for this bot. Defines the filesCog class where all the commands are located. This cog revolves around file interaction, which is things like storing user tags,
    and hopefully soon, interacting with files and more.
"""

# TODO - Maybe implement more data stored in tags? Like date of creation, creater, etc. Look into this: https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-python-dictionary
# TODO - Maybe just change filesCog to a tag cog if it gets too large?
# TODO - Make delete function limited to tag creator or admin only

import discord
from discord.ext import commands


class filesCog:

    """
    Used to define commands that interact with files.
    Currently, it's focused on tags, allowing for users to make tags, delete them, edit them, get info on them, and list all the tags.
    """

    def __init__(self,client):
        """
        Initializes everything.

        :param client: The discord client passed to the class to run commands.
        """

        self.client = client
        self.tagdictionary = {}

        # personal note: Since cog is loaded in akizuki.py which is a directory down, tags.txt is not in that directory and will not load. So, must specify the directory.
        # For example, a tag stored as "HelloWorld HELLOTHEREIAMADIVIDER Hello, World!" will return a list of ['HelloWorld', 'Hello, World!']
        try:
            with open("cogs/tags.txt", "r") as mytags:
                for line in mytags:
                    currentline = line.rstrip().split(" HELLOTHEREIAMADIVIDER ")    #This is how the tags are stored. The giant divider is meant to prevent the .split() from unintentionally messing stuff up,
                    self.tagdictionary[currentline[0]] = currentline[1]
                    
        except FileNotFoundError:
            with open("cogs/tags.txt","a+") as mytags:
                print("New tags.txt file created.")

    # pass_context allows for ctx to be used in functions
    # invoke_without_command allows for the tag command to be called by itself and not call itself when other subcommands are called.
    @commands.group(pass_context = True, invoke_without_command = True)
    async def tag(self, ctx, name):
            """
            Master command for the tag group of commands.
            Checks for a passed tag name value and subcommand. If a tag name is passed, it will print the tag.
            If a subcommand is passed, then nothing here will run.

            :param self: Is self
            :param ctx: ctx is used for checking stuff such as whether a subcommand is used or not.
            :param name: Name of the tag to be returned. Can be None assuming the user enters a subcommand.
            :return: void function.
            """

            if ctx.invoked_subcommand is None:
                contentstring = self.tagdictionary.get(name)

                if contentstring is not None:
                    await self.client.say(contentstring)
                else:
                    await self.client.say("That tag does not exist!")



    @tag.command()
    async def add(self, name : str, *,contents : str):
        """
        Subcommand allowing for the user to add new tags.

        :param self:  is self.
        :param name: Name of the tag to be added. Must be one word.
        :param contents: Contents of the tag to be added. Can be multiple words.
        :return: void function.
        """

        if name not in self.tagdictionary:
            with open("cogs/tags.txt", "a") as mytags:
                mytags.write(name + " HELLOTHEREIAMADIVIDER " + contents + "\n")
            self.tagdictionary[name] = contents
        else:
            await self.client.say("This tag already exists! Use the subcommand edit to change existing tags.")

        await self.client.say("Tag with name **{0}** and content **{1}** has been created.".format(name,contents))

    @tag.command()
    async def delete(self, name : str):
        """
        Subcommand allowing for the user to delete their tags.

        :param self:  is self.
        :param name:  Name of the tag to be deleted.
        :return:  void function.
        """
        linetodelete = ""
        linestokeep = []

        if name in self.tagdictionary:

            with open("cogs/tags.txt","r+") as mytags:

                for line in mytags:
                    currentline = line.rstrip().split(" HELLOTHEREIAMADIVIDER ")
                    # Ensures right tag is being deleted by checking name AND content of the tag
                    # currentline right now is shown as [title , content].
                    if currentline[0] == name and currentline[1] == self.tagdictionary[name]:
                        linetodelete = line
                    else:
                        linestokeep.append(line)


            with open("cogs/tags.txt", "w") as mytags:
                for line in linestokeep:
                    if line != linetodelete:
                        mytags.write(line)

            self.tagdictionary.pop(name)
            await self.client.say("Your tag **{0}** has been deleted.".format(name))


    @tag.command()
    async def edit(self, name : str, newcontent : str):

        """
        Used to edit an existing tag.

        :param name:  Name of tag to edit
        :param newcontent:  New content to replace the old content.
        :return:  void function.
        """

        editedline = ""
        unchangedlines = []


        if name in self.tagdictionary:

            with open("cogs/tags.txt", "r") as mytags:

                for line in mytags:
                    currentline = line.rstrip().split(" HELLOTHEREIAMADIVIDER ")

                    # Again confirms it's the right tag being changed.
                    # currentline right now is shown as [title , content].
                    if currentline[0] == name and currentline[1] == self.tagdictionary[name]:
                        currentline[1] = newcontent
                        currentline.insert(1," HELLOTHEREIAMADIVIDER ")

                        editedline = "".join(currentline)
                    else:
                        unchangedlines.append(line)


            with open("cogs/tags.txt", "w") as mytags:

                for line in unchangedlines:
                    if line != editedline:
                        if "\n" in line: # In case one of the tags doesn't have a newline on it, to prevent it from being bunched up on a single line.
                            mytags.write(line)
                        else:
                            mytags.write(line + "\n")
                mytags.write(editedline)

            self.tagdictionary[name] = newcontent
            await self.client.say("Your tag **{0}** has had its contents changed to **{1}**".format(name, newcontent))

        else:
            await self.client.say("That tag does not exist!")


    @tag.command()
    async def list(self):

        """
        Lists all the current tags in a nice embed.

        :return: void function.
        """

        # Basically, a giant string will be sent in the embed.
        keystring  = ""

        if len(self.tagdictionary) == 0:
            keystring = "No tags currently exist!"
        else:
            for key in self.tagdictionary:
                keystring += key
                keystring += "\n"

        listembed = discord.Embed(
            description="List of the currently stored tags..",
            color = 0xBEA4FA)

        listembed.title = "Here Be Tags"

        listembed.add_field(name = "Tag list:", value = keystring )

        await self.client.say(embed=listembed)

    @tag.command()
    async def info(self, name : str):
        """
        Provides the user with information about the tag they pass.

        :param name: Tag that the user will get information about.
        :return: void function.
        """

        # uses .casefold() in case there are characters that .lower() may not be able to handle.
        if name.casefold() in self.tagdictionary:
            await self.client.say("**Tag:** {0}  \n**Contents:** {1} " .format(name.casefold(), self.tagdictionary.get(name.casefold())))
        else:
            await self.client.say("That tag does not exist.")

def setup(client):
    client.add_cog(filesCog(client))
