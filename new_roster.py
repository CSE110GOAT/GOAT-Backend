import sys
sys.path.insert(0, './lib')
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import json
import urllib2
from urls import roster_urls


#list of all the sports urls
sports = []
sports = roster_urls

#Index of sport being accessed
sportIndex = 0


#The actual list of rosters
rosters = []

#for sport in sports:

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


page = requests.get(sports[2])
soup = BeautifulSoup(page.content, 'html.parser')

players_object = soup.select ("#roster-grid-layout")
players = players_object[0].contents
print players[1]
prefix = "www.ucsdtritons.com"
#In the case we are scrapping men...
for i in xrange(2, len(players)):
    print players[i]
    print type(players[i])
    """
    if players[i].has_attr('class'):
        if tag['class'] == 'gender':
            break;
    temp = players[i].find_children()
    for thingy in temp:
        if (thingy.has_attr('href')):
            bio_links.append(prefix + temp["href"])
        """
print bio_links    
        
    
