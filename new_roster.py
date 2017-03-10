# Author: Brian Han
# Date: 3/9/17
# My attempt to parse all the rosters by gender
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

import sys
sys.path.insert(0, './lib')
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import os
import json
import urllib2
from urls import roster_urls


#list of all the sports urls
sports = []
sports = roster_urls

#Index of sport being accessed
sportIndex = 0

#The index of men, when doing a men/women roster search
menIndex = 0
menOffset = 3

#The actual list of rosters
rosters = []

#The indexes where there are men/women separation
# The indexes 2,3,7,9 are for men pages,
# The indexes 13,14,18,20 are for women pages.
MenWomen = [2, 3, 7, 9, 13, 14, 18, 20 ] 

for sport in xrange(len(sports)):

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

    #Now gets sports based on index instead of object
    page = requests.get(sports[sport])
    soup = BeautifulSoup(page.content, 'html.parser')

    # Logic to find the men/women index, IF required
    # Checks if the sport index is in MenWomen list
    if (sport in MenWomen):
        players_object = soup.find (id="roster-grid-layout")
        players = players_object.contents

        #Removes newline characters from the list
        while True:
            try:
                players.remove('\n')
            except ValueError:
                break

        for index in xrange(len(players)):
            if "Women" in players[index].get_text():
                menIndex = index - menOffset
                break

    #Players objects has all the list objects
    players_object = soup.select (".player-name a")

    #players_string holds the strings for this specific sport on this iteration
    temp_strings = []
    for s in xrange(len(players_object)):
        if (sport in MenWomen):
            if (sport < 10 and s <= menIndex):
                players_strings.append (players_object[s].get_text())
                temp_strings.append(players_object[s].get_text())
            elif (sport > 10 and s > menIndex): 
                players_strings.append (players_object[s].get_text())
                temp_strings.append(players_object[s].get_text())
        else:
            players_strings.append (players_object[s].get_text())
            temp_strings.append(players_object[s].get_text())

    #hAndw_string is a list of player heights AND weights
    hAndw_object = soup.select (".height")
    if len (hAndw_object) != 0:
        for h in xrange(len(hAndw_object)):
            if (sport in MenWomen):
                if (sport < 10 and h <= menIndex):
                    players_hAndws.append(hAndw_object[h].get_text())
                elif (sport > 10 and h > menIndex): 
                    players_hAndws.append(hAndw_object[h].get_text())
            else:
                players_hAndws.append(hAndw_object[h].get_text())
    else :
        for s in temp_strings:
            players_hAndws.append ("")
        
    #positions_string is a list of positions
    positions_object = soup.select (".position .data")
    if len (positions_object) != 0:
        for p in xrange(len(positions_object)):
            if (sport in MenWomen):
                if (sport < 10 and p <= menIndex):
                    players_positions.append(positions_object[p].get_text())
                elif (sport > 10 and p > menIndex): 
                    players_positions.append(positions_object[p].get_text())
            else:
                players_positions.append(positions_object[p].get_text())
    else :
        for s in temp_strings:
            players_positions.append ("")

    #player_years is a list of years
    years_object = soup.select (".year .data")
    if len (years_object) != 0:
        for y in xrange(len(years_object)):
            if (sport in MenWomen):
                if (sport < 10 and y <= menIndex):
                    players_years.append(years_object[y].get_text())
                elif (sport > 10 and y > menIndex): 
                    players_years.append(years_object[y].get_text())
            else:
                players_years.append(years_object[y].get_text())
    else :
        for s in temp_strings:
            players_years.append ("")

    #players_hometowns is a list of player hometowns
    hometowns_object = soup.select (".hometown .data")
    if len (hometowns_object) != 0:
        for h in xrange(len(hometowns_object)):
            if (sport in MenWomen):
                if (sport < 10 and h <= menIndex):
                    players_hometowns.append(hometowns_object[h].get_text())
                elif (sport > 10 and h > menIndex): 
                    players_hometowns.append(hometowns_object[h].get_text())
            else:
                players_hometowns.append(hometowns_object[h].get_text())
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

        # puts image into directory and downloads the image
        # for example, the first baseball player image  would be at
        # ./rosters/0/0.png , 'wb' means write in binary 
    	if not os.path.exists("./static/rosters/"+str(sportIndex)):
	        os.makedirs("./static/rosters/"+str(sportIndex)) 
        with open( "./static/rosters/"+ str(sportIndex) + "/" + str(index) +".png", 'wb+' ) as out_file:
            img = urllib2.urlopen(players_images[index])
            out_file.write( img.read() )
            out_file.close()
    rosters.append (temp)

    sportIndex += 1

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
with open( "./static/rosters/roster.json", 'w+') as f:
        f.write( players_json)
