#Author: Brian Han
# Date: 2/11/17
# My attempt to get the baseball roster list, the pics.

import requests
from bs4 import BeautifulSoup

page = requests.get ("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2331&SPSID=29814&DB_OEM_ID=5800")
soup = BeautifulSoup(page.content, 'html.parser')

#
#for roster in body:
#    print roster
#

#Important tags:
#class_= player-name
# in the "a" tag , you can get the name and the html link
# under the "a" tag is an img of the person


#players_string is a list of player names
players_object = soup.select (".player-name a")
players_string = [p.get_text() for p in players_object]
print '\n'.join(players_string)


#players_images is a list of player image links; note that there are
#13 images missing for baseball, they have a "no image available" image
players_images = []
for s in players_string:
    temp = soup.find("img", {"alt":s})
    players_images.append(temp["src"])
print '\n'.join(players_images)

#bio_links is a list of player bio links.
bio_links = []
prefix = "www.ucsdtritons.com"
for s in players_string:
    temp = soup.find("a", {"title":s})
    bio_links.append(prefix + temp["href"])
print '\n'.join(bio_links)

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
