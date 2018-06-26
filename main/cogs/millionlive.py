"""Cog for a server I own. :)

Disabled for master build.
'"""

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


import datetime
import threading
import time

import discord
from discord.ext import commands

from random import choices
from collections import Counter



class millionCog():

    '''
    # Setup the Calendar API
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    store = file.Storage("cogs/millionlive/credentials.json")

    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("cogs/millionlive/credentials.json", SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()), cache_discovery=False)
    # cache_discovery set to false to prevent shitload of warnings from logging in the console.

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 3 events')
    events_result = service.events().list(calendarId='903olokiecut8b71q3gj90qhnhclle7q@import.calendar.google.com',
                                          timeMin=now,
                                          maxResults=3, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])



    class eventInstance():

        def __init__(self,event):

            self.event = event

            self.target_jp_start = event["start"]["date"]
            self.target_hawaii_end = event["end"]["date"]
            self.myeventname = event["summary"]
            self.eventname_split = self.myeventname.split(" ")

            self.fullname = str(self.eventname_split[0]) + " " + str(self.eventname_split[1][:-2])

        def main(self):

            self.target_jp_start = self.target_jp_start.split("-")

            self.target_jp_start = [int(x) for x in self.target_jp_start]

            self.target_jp_start = datetime.datetime(self.target_jp_start[0], self.target_jp_start[1],
                                                     self.target_jp_start[2])

            target_jp_start_str = self.target_jp_start.strftime("%Y-%m-%d %H:%M:%S")

            self.target_hawaii_end = self.target_hawaii_end.split("-")

            self.target_hawaii_end = [int(x) for x in self.target_hawaii_end]

            self.target_hawaii_end = datetime.datetime(self.target_hawaii_end[0], self.target_hawaii_end[1], self.target_hawaii_end[2])

            target_local_end = self.target_hawaii_end

            target_hawaii_end_str = self.target_hawaii_end.strftime("%Y-%m-%d %H:%M:%S")

            interval = 5

            print("------")

            def timenow_calc():

                interval = 1799.0

                timenow = datetime.datetime.now()

                timenow_jp = timenow + datetime.timedelta(hours=13)

                timenow_hawaii = timenow - datetime.timedelta(hours=6)

                timetostart = self.target_jp_start

                timetoend = self.target_hawaii_end - timenow_hawaii

                timetostart = self.target_jp_start - timenow_jp

                # Trace. TODO - Get rid of this maybe?

                # 1 day 16 hours 20 minutes
                # wait 1 day = 16 hr 20 min
                # wait 12 hours = 4 hr 20 min
                # wait 1 hour = 3 hr 20 min
                # wait 1 hour = 2 hr 20 min
                # wait 1 hour = 1 hr 20 min
                # wait 1 hour = 20 min
                # wait 15 min = 5 min
                # wait 3 min = 2 min
                # wait 3 min = 2 min + 1 min later

                # Only runs before event has triggered to prevent interval conflicts
                if timenow_jp < self.target_jp_start:
                    if timetostart >= datetime.timedelta(days=1):
                        interval = 86400
                    elif datetime.timedelta(hours=12) <= timetostart < datetime.timedelta(days=1):
                        interval = 43200
                    elif datetime.timedelta(hours=1) <= timetostart < datetime.timedelta(hours=12):
                        interval = 3600
                    elif datetime.timedelta(minutes=30) < timetostart < datetime.timedelta(hours=1):
                        interval = 1800
                    elif timetostart <= datetime.timedelta(minutes=30):
                        interval = 900
                    elif timetostart <= datetime.timedelta(minutes=15):
                        interval = 180

                # Only runs if event has triggered to prevent interval conflicts
                elif timenow_jp >= self.target_jp_start:
                    if timetoend >= datetime.timedelta(days=1):
                        interval = 86400
                    elif datetime.timedelta(hours=12) <= timetoend < datetime.timedelta(days=1):
                        interval = 43200
                    elif datetime.timedelta(hours=1) <= timetoend < datetime.timedelta(hours=12):
                        interval = 3600
                    elif datetime.timedelta(minutes=30) < timetoend < datetime.timedelta(hours=1):
                        interval = 1800
                    elif timetoend <= datetime.timedelta(minutes=30):
                        interval = 900
                    elif timetoend <= datetime.timedelta(minutes=15):
                        interval = 180

                timenow_str = timenow.strftime("%Y-%m-%d %H:%M:%S")

                timenow_jp_str = timenow_jp.strftime("%Y-%m-%d %H:%M:%S")

                timenow_hawaii_str = timenow_hawaii.strftime("%Y-%m-%d %H:%M:%S")

                time.sleep(5)


                print("Event being tracked:", self.myeventname)

                print("Time to start:", timetostart)
                print("Time to end:", timetoend)

                print("target jp time is:")
                print(self.target_jp_start)
                print("\n")

                print("local time is:")
                print(timenow_str)
                print("\n")

                print("local time in jp is:")
                print(timenow_jp_str)
                print("\n")

                print("target end time in local time is:")
                print(target_local_end)
                print("\n")

                # untilevent = datetime.timedelta()

                if self.target_jp_start > timenow_jp:
                    print("The event has not started yet.")
                elif self.target_jp_start <= timenow_jp:
                    print("The event has already started.")
                    # TODO - Change server picture, channel names. Distinguish between seiyuu & characters. Need good way to get and store nicknames/channel names/pictures w/ least amount of work preferrably

                if timenow >= self.target_hawaii_end:
                    print("It is past the event end time.")
                elif timenow < self.target_hawaii_end:
                    print("It is not past the event end time yet.")

                print("Current interval between checks is:", interval)
                print("------")
                print("\n")

                t = threading.Timer(interval, timenow_calc)
                t.start()
                time.sleep(5)

            t = threading.Timer(interval, timenow_calc)
            t.start()
            time.sleep(5)

    trackedevents = []

    counter = 0
    eventname = "event" + str(counter)

    for x in events:
        eventname = eventInstance(x)

        eventname.main()
        trackedevents.append(eventname)
        counter += 1
        eventname = "event" + str(counter)

    for x in trackedevents:
        print(x.fullname)

    '''

    def __init__(self,client):
        self.client = client

        # dictionary of cards that have a percentage value added to them?

        self.rarities=["R", "SR", "Limited SSR", "Permanent SSR"]
        self.normalweights=[.85, .12, .03]


        

'''
    @commands.command()
    async def gacha(self, rolls: int = None):

        if rolls is None:

            return currentgachapool

        if rolls >= 10 and rolls % 10 != 0:
            return "enter up to ten rolls or a multiple of ten."

        else:
            roll=choices(self.rarities, self.normalweights, rolls):

            condensedrolls = Counter(choices)

            countR = condensedrolls["R"]

            countSR = condensedrolls["SR"]

            countSSR = condensedrolls["SSR"]

            listR = []
            listSR = []
            listSSR = []

            for num in countR:
                listR.append(random.choice(masterlistR))

            for num in countSR:
                listSR.append(random.choice(masterlistSR))

            for num in countSSR:
                listSSR.append(random.choice(masterlistSSR))
'''





def setup(client):
    client.add_cog(millionCog(client))
