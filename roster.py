#Author: Brian Han
# Date: 2/26/17
# My attempt to parse all the rosters
# The code creates a list, rosters, that at each index has a sublist of 
# lists, where each list element in the sublist has a:
# player name, player height and weight, player position, player year, player
# hometown, player image link, and player bio link
#
# Breakdown:
#      rosters [0] = list of [player name, player height and weight,
#                             player position, player year, player hometown,
#                             player image link, player bio link]'s
#      rosters [0][0] = first [player name, player height and weight,
#                             player position, player year, player hometown,
#                             player image link, player bio link] at ID 0
#      rosters [0][0][0] = first player name at ID 0 
#      rosters [0][0][1] = first player height and weight at ID 0 
#      rosters [0][0][2] = first player position at ID 0 
#      rosters [0][0][3] = first player year at ID 0 
#      rosters [0][0][4] = first player hometown at ID 0 
#      rosters [0][0][5] = first image link at ID 0
#      rosters [0][0][6] = first article link at ID 0

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

    #players_string is a list of player names
    players_strings = []

    #players_hAndw is a list of player height and weight
    players_hAndws = []

    #players_position is a list of player positions
    players_positions = []

    #players_years is a list of player years
    players_years = []

    #players_hometowns is a list of player hometowns
    players_hometowns = []

    #players_images is a list of player image links; note that there are
    players_images = []

    #bio_links is a list of player bio links.
    bio_links = []


    page = requests.get(sport)
    soup = BeautifulSoup(page.content, 'html.parser')

    players_object = soup.select (".player-name a")

    #players_string holds the strings for this specific sport on this iteration
    temp_strings = []
    for s in players_object:
        players_strings.append (s.get_text())
        temp_strings.append(s.get_text())

    #hAndw_string is a list of player heights AND weights
    hAndw_object = soup.select (".height")
    if len (hAndw_object) != 0:
        for h in hAndw_object:
            players_hAndws.append(h.get_text())
    else :
        for s in temp_strings:
            players_hAndws.append ("")
        
    #positions_string is a list of positions
    positions_object = soup.select (".position .data")
    if len (positions_object) != 0:
        for p in positions_object:
            players_positions.append(p.get_text())
    else :
        for s in temp_strings:
            players_positions.append ("")

    #player_years is a list of years
    years_object = soup.select (".year .data")
    if len (years_object) != 0:
        for y in years_object:
            players_years.append(y.get_text())
    else :
        for s in temp_strings:
            players_years.append ("")

    #players_hometowns is a list of player hometowns
    hometowns_object = soup.select (".hometown .data")
    if len (hometowns_object) != 0:
        for h in hometowns_object:
            players_hometowns.append(h.get_text())
    else :
        for s in temp_strings:
            players_hometowns.append ("")

    #players_images is a list of player images
    for s in temp_strings:
        temp = soup.find("img", {"alt":s})
        players_images.append(temp["src"])


    #bio_links is a list of player bio links.
    prefix = "www.ucsdtritons.com"
    for s in temp_strings:
        temp = soup.find("a", {"title":s})
        bio_links.append(prefix + temp["href"])

    #Creates a temp list of player names, player images, bio links
    # for each sport, and then adds it to the player ID index
    temp = []
    for index in xrange (len(players_strings)):
        temp.append([
                players_strings[index],
                players_hAndws[index].replace("\n","").replace("\t","").replace("\\", ""),
                players_positions [index],
                players_years[index],
                players_hometowns[index].replace("\n","").replace("\t",""),
                players_images [index],
                bio_links[index]])
    rosters.append (temp)

#Formats the Dataframe in Panda
players = pd.DataFrame ({
        "rosters": rosters
    })

#Debug statements
"""
print players
print rosters[0][0]
print rosters[0][0][0]
print rosters[0][0][1]
print rosters[0][0][2]
"""

#Converting the dataframe to a json file
players_json = players.to_json()
with open( "roster.json", 'w') as f:
        f.write( players_json)
