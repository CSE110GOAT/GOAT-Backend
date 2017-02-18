#Author: Brian Han
# Date: 2/17/17
# My attempt to parse all the rosters
# The code creates a list, rosters, that at each index is a list of lists
# that corresponds to the sport index.
# Breakdown:
#      rosters [0][0] = list of player names for that sport
#      rosters [0][1] = list of player images for that sport
#      rosters [0][2] = list of player biography links for that sport

import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import json
from urls import roster_urls


#list of all the sports urls
sports = []
sports = roster_urls

#The actual list of rosters
rosters = []

for sport in sports:
    #players_images is a list of player image links; note that there are
    players_images = []

    #players_string is a list of player names
    players_string = []

    #bio_links is a list of player bio links.
    bio_links = []

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

#I be tryin
    rosters.append ([players_string, players_images, bio_links])
    """
players = pd.DataFrame ({
        "player": players_string,
        "image" : players_images,
        "link to bio": bio_links
    })
"""

players = pd.DataFrame ({
        "rosters": rosters
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
for h in hAndw_object:
    hAndw_string.append(h.get_text())
print '\n'.join(hAndw_string)
"""

"""
#positions_string is a list of positions
positions_object = soup.select (".position .data")
for p in positions_object:
    positions_string.append(p.get_text())
print '\n'.join(positions_string)
"""

"""
#years_string is a list of years
years_object = soup.select (".year .data")
for y in years_object:
    years_string.append(y.get_text())
print '\n'.join (years_string)
"""

"""
#hometowns_string is a list of player hometowns
hometowns_object = soup.select (".hometown .data")
for h in hometowns_object:
    hometowns_string.append(h.get_text())
print '\n'.join(hometowns_string)
"""
