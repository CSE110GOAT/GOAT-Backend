"""
The Header that Josh never made :(
Please comment me :( Jake, plz :( 
Date: 3/2/17
"""

import requests
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import io, json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



page = requests.get("http://www.ucsdtritons.com/main/Schedule.dbml?DB_OEM_ID=5800&PAGEMO=-1&PAGEDIR=1")
soup = BeautifulSoup(page.content, 'html.parser')
page.status_code

# Searching for the div that contains the schedule table
scores_schedule = soup.find("div", {"id":"site_container"})

# The first tr contains the field names. Used to find the headings
headings = [td.get_text().replace("\n", "").replace("\t","") for td in scores_schedule.find_all("th")]

datasets = []
for row in scores_schedule.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text().replace("\n", "").replace("\t","") for td in row.find_all("td")))
    dataset = dataset[:len(dataset)-1]
    datasets.append(dataset)

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
opponent = [str(ot.get_text().replace("\n", "").replace("\t", "").replace("*", "").decode('ascii', 'ignore')) for ot in opponent_tag]

#Debug statement
#print opponent

# Scraping the location
location_tag = scores_schedule.select(".location")
location = [str(lt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for lt in location_tag]

#Debug statement
#print location

# Scraping the time
time_tag = scores_schedule.select(".time")
time = [str(timet.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for timet in time_tag]
#Debug statement
#print time

# Scraping the results. Removed the Info - Schedule and Recap texts
results_tag = scores_schedule.select(".results")
results = [str(rt.get_text().replace("\n", "").replace("\t", "").replace("Schedule - Info", "").replace("Info - Schedule", "").replace("Recap", "").decode('ascii', 'ignore')) for rt in results_tag]

#Debug statement
#print results

# Scraping the recap
prefix = "www.ucsdtritons.com"
game_tag = scores_schedule.select(".gray-drop")
recap = []
notes = []
stats = []
for game in game_tag:
    #print ret.get_text()
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



date.pop(0)
team.pop(0)
opponent.pop(0)
location.pop(0)
time.pop(0)
results.pop(0)

# Grouping the information based on each game and not on date/team/opponent/location/time/results
games = []
for i in range (len(date)):
    games.append([date[i], team[i], opponent[i], location[i], time[i],
            results[i], recap[i], notes[i], stats[i]])

schedule = pd.DataFrame({
    "Games": games
})

'''
# Placing the data into a Pandas dataframe
schedule = pd.DataFrame({
    "Date": date,
    "Team": team,
    "Opponent": opponent,
    "Location": location,
    "Time (PST)": time,
    "Results": results
})
'''
#Debug statement
#print schedule

#Writing the data to a file
json_schedule = schedule.to_json()
with open('./static/schedule.json', 'w') as f:
    f.write(json_schedule)
