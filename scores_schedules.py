import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



page = requests.get("http://www.ucsdtritons.com/main/Schedule.dbml?DB_LANG=C&&DB_OEM_ID=5800")
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



#date = dataset.find(class_="team").get_text()
#print date
#for dataset in datasets:
#    for field in dataset:
        #print "{0:<16}: {1}".format(field[0], field[1])
#print headings



schedule = pd.DataFrame({
    "Date": date,
    "Team": team,
    "Opponent": opponent,
    "Location": location,
    "Time (PST)": time,
    "Results": results
})
print schedule
