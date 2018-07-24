# Command Help

## *Core Commands*
> Bot's core.

|Command| Purpose
|--|--|
|changepresence **[status] [gamename]**|Changes the bot's status. **Bot Owner Only**
|echo **[channel] [message]** | Echos the given message in the specified channel. **Bot Owner Only**
|help|Returns help for commands. You should've been directed here.
|info| Returns information about the bot.
|ping | Returns the bot's latency.
|shutdown|Turns the bot off. **Bot Owner Only** |
|cogs| Returns a list of cogs.
|loadcog **[cog]** | Loads the specified cog. **Bot Owner Only**
|unloadcog **[cog]**| Unloads the specified cog. **Bot Owner Only**
|reloadcog **[cog]** | Reloads the specified cog. **Bot Owner Only**


## *RNG Cog*

> RNG Cog that has commands tailored for RNG operations

|Command| Purpose
|--|--|
|randomnumber|Returns a random integer between 1 and 100.

## *Files Cog*
> Used to define commands that interact with files. Currently, it's focused on tags, allowing for users to make tags, delete them, edit them, get info on them, and list all the tags.

|Command| Purpose
|--|--|
|tag **[tagname]**|Returns the specified tag.
|tag add **[name] [contents]**| Adds a new tag with the specified name and contents.
|tag delete **[name]**| Deletes the specified tag. **Limited to the Bot Owner and tag creator.**
|tag edit **[name] [newcontent]**| Edits the specified tag with new content. **Limited to the Bot Owner and tag creator.**
|tag list| Lists all the tags currently on the server.
|tag info **[tag]**| Returns information about the specified tag.


## *Math Cog*
> Used for math functions such as adding, subtracting, multiplying, and dividing. Uses regexes for more friendly interaction. **Currently very buggy, and is low priority.**

|Command| Purpose
|--|--|
|expression **[expression]**|Evaluates a given expression.
|add **[arg1] [arg2] [arg3] . . .**| Adds the given terms. *(Does not require an addition sign.)*
|subtract **[arg1] [arg2] [arg3] . . .**| Subtracts the given terms. *(Does not require a subtraction sign.)*
|multiply **[arg1] [arg2] [arg3] . . .**| Multiplies the given terms. *(Does not require multiplication sign.)*
|divide **[arg1] [arg2] [arg3] . . .**| Divides the given terms. *(Does not require a division sign.)*

## *Users Cog*
> Cog meant to interact with the user data type in Discord.
>
|Command| Purpose
|--|--|
|emojis| Lists all of the current server's emojis.
|roles| Lists all of the current server's roles.
|profilepicture **[user]**| Returns the specified user's profile picture. **Will return the author's if none is specified.**
|serverinfo| Returns the information of the server this command is called in.
|userinfo **[user]**|Returns information on a specified user. **Will return the author's information if none is specified.**
|iam **[role]**| Assigns the specified role if it's on the list of self assignable roles (SAR).
|iamn **[role]**| Removes the specified role if it's on the list of SAR.
|lsar| Lists all of the SAR.
|asar **[role]**| Adds a role to the list of SAR. **Requires the user to have "Manage Roles" permission.**
|rsar **[Role]**| Removes a role from the list of SAR. **Requires the user to have"Manage Roles" permission.**


## *Action Cog*
> Cog centered around interacting with users by allowing for them to use a variety of action commands.
> These commands can be used without a mention, or with a mention to promote interaction with people.
>  **Each command will send its respective reaction gif, with dialogue dependent on whether a user is mentioned or not.**

|Command| Purpose
|--|--|
|angry **[user]**|For when you're angry.
|blush **[user]**|For when you want to blush.
|cry **[user]**|Today's a bad day for rain.
|dance **[user]**|For when you feel like moving around IRL but don't want to.
|hug **[user]**|Happy hug? Sad hug? Well too bad, the gif is randomly chosen.
|idol **[user]**|For when you're just a tad bit too deep in idol hell.
|kiss **[user]**| For when you just absolutely need to show your affection.
|laugh **[user]**| The best medicine.
|pat **[user]**| For real. Who doesn't like anime headpats?
|pout **[user]**| Ditto. ^^
|shrug **[user]**| ¯\_(ツ)_/¯
|slap **[user]**| B-Baka!
|smile **[user]**| The most precious thing in this world.
|squeal **[user]**| For when you just can't handle the sweetness.
|wink **[user]**| For that flirtatious desire of yours.



## *Million Live Cog*
> Cog for a server I own. :)

|Command| Purpose
|--|--|
|sticker **[stickername]**|Returns the specified sticker. **Will return a random one if none is specified.**
| stickerlist| Returns the list of stickers.

## *WOWS Cog*
> Cog for World of Warships commands.

|Command| Purpose
|--|--|
|stats **[user]**|Returns the stats of a given player.
