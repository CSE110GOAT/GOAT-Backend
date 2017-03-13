"""
The Header that Josh never made :(
Please comment me :( Jake, plz :(
This class returns a list of games, each game being a list containing
the following in ascending order:
0:date
1:team
2:opponent
3:location
4:time
5:results
6:recap
7:notes
8:stats
9:lat
10: lon

Date: 3/12/17
"""

import sys
import requests
#import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
#requests_toolbelt.adapters.appengine.monkeypatch()
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import io, json
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

page = requests.get("http://www.ucsdtritons.com/main/Schedule.dbml?DB_OEM_ID=5800&PAGEMO=-1&PAGEDIR=1")
soup = BeautifulSoup(page.content, 'html.parser')
page.status_code

# Searching for the div that contains the schedule table
scores_schedule = soup.find("div", {"id":"site_container"})

# Scraping the dates
date_tag = scores_schedule.select(".date")
date = [str(dt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for dt in date_tag]
#Debug statement
#print date

# Scraping the teams 
team_tag = scores_schedule.select(".team")
team = [str(tt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for tt in team_tag]

#Debug statement
#print team

# Scraping the opponents. Removed the '*' which means that it is a conference game
opponent_tag = scores_schedule.select(".opponent")
#print opponent_tag[0].parent.parent
opponent = [re.sub(r'\([^)]*\)', '', str(ot.get_text().replace("\n", "").replace("*", "").replace("\t", "").replace("*", "").decode('ascii', 'ignore'))) for ot in opponent_tag]


# TODO sdfhenl2dsafadfslfajdskafdkjla;dsfjfdsaksafj;sfajfasdk
tournament = ""
strings = ["Day One", "Day Two", "Day Three", "Day Four", "Day Five"]

# goes through all the opponent tags, checks if it has any of the "Day" strings
# then finds the first instance with the opponent's parent's id 
for o in xrange(len(opponent_tag)):
    oppo = opponent_tag[o]
    if opponent[o] in strings:
        key = oppo.parent['schedule-id']
        # find returns an object (the whole chunk) -- we only want the name
        tournament = scores_schedule.find("tr",{'schedule-id':
                key}).get_text().replace("\n","").replace("\t","")
        # temp store old name and then append tournament/invitational in front
        opponent[o] = tournament + " " + opponent[o]
    


"""
for o in opponent:
game_tag = scores_schedule.select(".gray-drop")
for game in game_tag:
    a_recap = ""
    a_note = ""
    a_stat = ""
    for i in game:
        if type(i) is bs4.element.NavigableString:
            continue
        if i.has_attr('href') and 'Recap' in i.get_text():
            a_recap = prefix + i['href']
        if i.has_attr('href') and 'Notes' in i.get_text():
            a_note = prefix + i['href']
        if i.has_attr('href') and 'Stats' in i.get_text() and 'Live' not in \
            i.get_text():
            a_stat = prefix + i['href']
    recap.append(a_recap)
    notes.append(a_note)
    stats.append(a_stat)
            """
# TODO sdfhenl2dsafadfslfajdskafdkjla;dsfjfdsaksafj;sfajfasdk
    
#Debug statement
#print opponent

# Scraping the location
location_tag = scores_schedule.select(".location")
location = [str(lt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for lt in location_tag]

# Get Coordinates

#from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeocoderServiceError
#locator = Nominatim()
locator = GoogleV3()
def getGeo( address ):
    try:
        return locator.geocode( address )
    except GeocoderTimedOut:
        return getGeo( address )
    except GeocoderServiceError:
        return getGeo( address )

# open coords file to read/write coordinates
import csv
coordsIn = open('coords.csv', 'r+')
coordsOut = open('coords.csv', 'a+')
reader = csv.reader(coordsIn)
writer = csv.writer(coordsOut) 

# remove location header
location.pop(0)

# store latitude and longitude for games
lat = []
lon = []
count = 0
for l in location : 
    oneLat = ""
    oneLon = ""
    found = False

# print l
    for row in reader : 
        if row and l == row[0]:
            oneLat = row[1]
            oneLon = row[2]
            found = True
            break
    if found :
        lat.append( oneLat )
        lon.append( oneLon )
        continue

    quit()
    geo = getGeo( l )
    oneLat = geo.latitude
    oneLon = geo.longitude
    row = [ l, oneLat, oneLon ] 
    writer.writerow( row )

    lat.append( oneLat )
    lon.append( oneLon )
    """
    if geo is None: 
        l = re.sub(r'\([^)]*\)', '', l ) 
        geo = getGeo( l )

    if geo is not None:
        oneLat = geo.latitude
        oneLon = geo.longitude
    """
    

# close file
coordsIn.close()
coordsOut.close()

# Scraping the time
time_tag = scores_schedule.select(".time")
time = [str(timet.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for timet in time_tag]

# Scraping the results. Removed the Info - Schedule and Recap texts
results_tag = scores_schedule.select(".results")
results = [str(rt.get_text().replace("\n", "").replace("\t", "").replace("Schedule - Info", "").replace("Info - Schedule", "").replace("Recap", "").decode('ascii', 'ignore')) for rt in results_tag]

# Scraping the recap
prefix = "https://www.ucsdtritons.com"
game_tag = scores_schedule.select(".gray-drop")
recap = []
notes = []
stats = []
for game in game_tag:
    a_recap = ""
    a_note = ""
    a_stat = ""
    for i in game:
        if type(i) is bs4.element.NavigableString:
            continue
        if i.has_attr('href') and 'Recap' in i.get_text():
            a_recap = prefix + i['href']
        if i.has_attr('href') and 'Notes' in i.get_text():
            a_note = prefix + i['href']
        if i.has_attr('href') and 'Stats' in i.get_text() and 'Live' not in \
            i.get_text():
            a_stat = i['href']
    recap.append(a_recap)
    notes.append(a_note)
    stats.append(a_stat)

# remove headers of the table
date.pop(0)
team.pop(0)
opponent.pop(0)
time.pop(0)
results.pop(0)

# Grouping the information based on each game and not on date/team/opponent/location/time/results
games = []
for i in range (len(date)):
    if ("/" in opponent[i]) or ("," in opponent[i]) or ("vs." in opponent[i]):
        continue
    games.append([ date[i], team[i], opponent[i], location[i], time[i], results[i],
                 recap[i], notes[i], stats[i], lat[i],lon[i] ])

schedule = pd.DataFrame({
    "Games": games
})

#Writing the data to a file
json_schedule = schedule.to_json()
with open('./static/schedule.json', 'w') as f:
    f.write(json_schedule)
