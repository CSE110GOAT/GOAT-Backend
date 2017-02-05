import requests
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



page = requests.get("http://www.ucsdtritons.com/main/Schedule.dbml?DB_LANG=C&&DB_OEM_ID=5800")
soup = BeautifulSoup(page.content, 'html.parser')

div = soup.find("div", {"id":"site_container"})

# The first tr contains the field names.
headings = [td.get_text().replace("\n", "").replace("\t","") for td in div.find_all("td", {"class":"subhdr"})]
del headings[0] # deleting the first title header of the table




datasets = []
for row in div.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text().replace("\n", "").replace("\t","") for td in row.find_all("td")))
    dataset = dataset[:len(dataset)-1]
    datasets.append(dataset)

datasets = datasets[:len(datasets)-5]


#for dataset in datasets:
#    dataset = [for field in dataset]

#datasets = datasets[:len(datasets)-150]

for dataset in datasets:
    for field in dataset:
        print "{0:<16}: {1}".format(field[0], field[1][1:])
#print headings



#import pandas as pd
#schedule = pd.DataFrame({
#    "Date":
#    "Team":
#    "Opponent":
#    "Location":
#    "Time (PST)":
#    "Score":
#    "Media":
#})