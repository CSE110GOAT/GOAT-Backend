import requests
from bs4 import BeautifulSoup
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
#print date

# Scraping the teams 
team_tag = scores_schedule.select(".team")
team = [str(tt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for tt in team_tag]

#print team

# Scraping the opponents. Removed the '*' which means that it is a conference game
opponent_tag = scores_schedule.select(".opponent")
opponent = [str(ot.get_text().replace("\n", "").replace("\t", "").replace("*", "").decode('ascii', 'ignore')) for ot in opponent_tag]

#print opponent

# Scraping the location
location_tag = scores_schedule.select(".location")
location = [str(lt.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for lt in location_tag]

#print location

# Scraping the time
time_tag = scores_schedule.select(".time")
time = [str(timet.get_text().replace("\n", "").replace("\t", "").decode('ascii', 'ignore')) for timet in time_tag]

#print time

# Scraping the results. Removed the Info - Schedule and Recap texts
results_tag = scores_schedule.select(".results")
results = [str(rt.get_text().replace("\n", "").replace("\t", "").replace("Schedule - Info", "").replace("Info - Schedule", "").replace("Recap", "").decode('ascii', 'ignore')) for rt in results_tag]

#print results

# Scraping the recap
prefix = "www.ucsdtritons.com"
recap_tag = scores_schedule.select(".gray-drop a")
recap = []
#print recap_tag
for ret in recap_tag:
    #print ret.get_text()
    #print ret
    if ret.has_attr('href') and 'Recap' in ret.get_text():
        recap.append(prefix + ret['href'])
        print recap[len(recap)-1]




date.pop(0)
team.pop(0)
opponent.pop(0)
location.pop(0)
time.pop(0)
results.pop(0)

# Grouping the information based on each game and not on date/team/opponent/location/time/results
games = []
for i in range (len(date)):
    games.append([date[i], team[i], opponent[i], location[i], time[i], results[i]])

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
#print schedule

#Writing the data to a file
json_schedule = schedule.to_json()
with open('schedule.json', 'w') as f:
    f.write(json_schedule)