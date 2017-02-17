import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import json
from urls import news_urls

sports = news_urls

for sport in sports:
    page = requests.get(sport)
    soup = BeautifulSoup(page.content, 'html.parser')

    date = soup.select (".oldheadline")
##############################################
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