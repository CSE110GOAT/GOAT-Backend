#Author: Brian Han
# Date: 2/13/17
# My attempt to get the baseball roster list, the pics.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import json

sports = []

#players_images is a list of player image links; note that there are
players_images = []

#players_string is a list of player names
players_string = []

#bio_links is a list of player bio links.
bio_links = []

#Baseball page
sports.append ("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2331&SPSID=29814&DB_OEM_ID=5800")

#Basketball page
sports.append ("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2337&SPSID=29887&DB_OEM_ID=5800")

#Cross Country page
sports.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11063&SPSID=93276&DB_OEM_ID=5800")

#Men's Golf page
sports.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2343&SPSID=29952&DB_OEM_ID=5800")

#"Men's Rowing" page
sports.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2335&SPSID=29862&DB_OEM_ID=5800")

#Men's Soccer page
sports.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2335&SPSID=29862&DB_OEM_ID=5800")

for sport in sports:
    page = requests.get(sport)
    soup = BeautifulSoup(page.content, 'html.parser')

    players_object = soup.select (".player-name a")

    #Holds the strings for this specific sport on this iteration
    temp_string = []
    for s in players_object:
        players_string.append (s.get_text())
        temp_string.append(s.get_text())
#print '\n'.join(players_string)

    for s in temp_string:
        temp = soup.find("img", {"alt":s})
        players_images.append(temp["src"])
#print '\n'.join(players_images)

#bio_links is a list of player bio links.
    prefix = "www.ucsdtritons.com"
    for s in temp_string:
        temp = soup.find("a", {"title":s})
        bio_links.append(prefix + temp["href"])
#print '\n'.join(bio_links)

players = pd.DataFrame ({
        "player": players_string,
        "image" : players_images,
        "link to bio": bio_links
    })

print players

#Converting the dataframe to a json file
players_json = players.to_json()
with open( "roster.json", 'w') as f:
        f.write( players_json)

"""
#hAndw_string is a list of player heights AND weights
#NOTE: spacing of height and weight is off due to how it is entered 
# in the html file
hAndw_object = soup.select (".height")
hAndw_string = [h.get_text() for h in hAndw_object]
print '\n'.join(hAndw_string)
"""

"""
#positions_string is a list of positions
positions_object = soup.select (".position .data")
positions_string = [p.get_text() for p in positions_object]
print '\n'.join(positions_string)
"""

"""
#years_string is a list of years
years_object = soup.select (".year .data")
years_string = [y.get_text() for y in years_object]
print '\n'.join (years_string)
"""

"""
#hometowns_string is a list of player hometowns
hometowns_object = soup.select (".hometown .data")
hometowns_string = [h.get_text() for h in hometowns_object]
print '\n'.join(hometowns_string)
"""
