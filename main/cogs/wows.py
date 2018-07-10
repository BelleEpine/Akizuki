import discord
from discord.ext import commands
import json

from aiohttp import ClientSession
from wowspy import WowsAsync

class WOWSCog:

    def __init__(self, client):

        self.client = client

        with open("config.json", "r") as f:
            try:
                data = json.load(f)

                self.apikey = data["WOWS API Key"]

            except Exception as e:
                print(e)

    @commands.command()
    async def stats(self, user: str = None):

        session = ClientSession()
        my_api = WowsAsync(self.apikey, session)

        if user is None:
            await self.client.say("You must enter a username!")
            return

        player_name = user
        player_id_response = await my_api.players(my_api.region.NA, player_name, fields='account_id', limit=1)

        if player_id_response["status"] is "error":
            await self.client.say("That is not a valid username!")
            return
        else:
            pass

        player_id = player_id_response['data'][0]['account_id']
        player_stats_response = await my_api.player_personal_data(my_api.region.NA, player_id, fields='statistics.pvp')

        if player_stats_response["meta"]["hidden"] is None:
            await self.client.say("This profile is hidden.")


        #statsembed = discord.Embed(color=14434903)



def setup(client):
    client.add_cog(WOWSCog(client))