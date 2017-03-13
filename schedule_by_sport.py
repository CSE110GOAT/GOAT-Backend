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
from urls import schedule_urls
by_sport = []
for u in xrange(len(schedule_urls)):
    url = schedule_urls[u]

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #page.status_code
    
    print "\nSports #" + str(u) + "\n"

    # Searching for the div that contains the schedule table
    scores_schedule = (soup.find("table", {"id":"schedule-table"})).find("tbody")


    # Scraping the dates
    date_tag = scores_schedule.select(".date")
    date = [str(dt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for dt in date_tag]

    #Debug statement
    #print date

    # Scraping the teams 
    #team_tag = scores_schedule.select(".team")
    #team = [str(tt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for tt in team_tag]
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
    

# TODO sdfhenl2dsafadfslfajdskafdkjla;dsfjfdsaksafj;sfajfasdk
    
#Debug statement
#print opponent

    # Scraping the location
    location_tag = scores_schedule.select(".location")
    location = [str(lt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for lt in location_tag]

    # Get Coordinates
    # remove location header

    # Scraping the time
    time_tag = scores_schedule.select(".time")
    time = [str(timet.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for timet in time_tag]

    # Scraping the results. Removed the Info - Schedule and Recap texts
    results_tag = scores_schedule.select(".results")
    results = [str(rt.get_text().replace("\n", "").replace("\t", "").replace("Schedule - Info", "").replace("Info - Schedule", "").replace("Recap", "").decode('ascii', 'ignore')) for rt in results_tag]
    
    games = []
    # remove headers of the table
    # Grouping the information based on each game and not on date/team/opponent/location/time/results
    for i in range (len(date)):
        if ("/" in opponent[i]) or ("," in opponent[i]) or ("vs." in opponent[i]):
            continue
        games.append([ date[i], opponent[i], location[i], time[i], results[i] ])
    
    by_sport.append(games)

schedule = pd.DataFrame({
    "Games": by_sport
})

#Writing the data to a file
json_schedule = schedule.to_json()
with open('./static/schedule_individual.json', 'w') as f:
    f.write(json_schedule)
