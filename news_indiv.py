# TEAM BACKEND
# 
# Descriptin: takes in a sports news archive url and grabs all the article 
# headlines and urls for each sport 
# 
# Structure: [ [ [article_urls], [headlines], [article_dates] ], ...]
# Each slot in the over all array is a sport
# Each sport has 2 arrays

import sys
#sys.path.insert(0, './lib')
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import io
import json
from urls import news_urls
import urllib2
import datetime

news = []
dataframes = []

articles_by_sport = []

article_urls = []
headlines = []
article_dates = []
for u in xrange(len(news_urls)-20): 
    url = news_urls[u]
    print "\nSport #" + str(u) + "\n"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # gets all oldheadline
    article_tags = soup.select(".oldheadline")
    
    article_info = []
    # for every article archive, it stores all the individual article links,
    # headlines, and article dates
    for i in xrange(len(article_tags)):
                
        # parse dates -- there are 6 sections per <TR> tag -- which is how the articles are divided
        if i % 7 == 1 :
            print "date"
            article_info.append(article_tags[i].get_text().replace("\t","").replace("\n",""))
            article_dates.append(article_tags[i].get_text().replace("\t","").replace("\n",""))
        
        # links are in a subtag of oldheadline
        # we search through the children to find if there's an href attribute
        children = article_tags[i].findChildren()
        link = ''
        for child in children:
            if child.has_attr('href'):
                link = 'www.ucsdtritons.com/' +  child['href']
        cont = True 
        if  link == '' :
            cont = False
        
        if cont : 
            
            if len(article_urls) != 0  and link == article_urls[len(article_urls)-1]:
                continue
            
            # goes into the article link to download/store the image
            # download image corresponding to article as [index].jpg
            aPage = requests.get( 'http://' + link )
            aSoup = BeautifulSoup(aPage.content, 'html.parser')
            
            print "link: " + link
            print "art: " + article_tags[i].get_text()
            
            # appends article url and headlines per sport
            article_urls.append(link)
            headlines.append(article_tags[i].get_text())
            
            article_info.append(link)
            article_info.append(article_tags[i].get_text())
            article_urls.append(link)
             
            # finds image url
            try :
                imgLink = [ j for j in aSoup.select('#GlobalArticleContainer img') if j.has_attr('title') ][0]['src']
                article_info.append(imgLink)
            except IndexError:
                continue
            
            news.append(article_info)
             
            article_info = []
sorted(news, key=lambda x: datetime.datetime.strptime(x[0], '\r%m/%d/%Y\r'))

# puts image into directory and downloads the image
# for example, the first baseball article will be at ./news/0/0.jpg , 'wb' means write in binary
if not os.path.exists("./static/news_images/"):
    os.makedirs("./static/news_images")
i = 0
for element in news :
    with open( "./static/news_images/" + str(i) +".png", 'w+b' ) as out_file:
        img = urllib2.urlopen(element[3])
        out_file.write( img.read() )
        out_file.close()
        print "image" + str(i)
    i = i + 1

# used to add to data frame (panda)

# Placing the data into a Pandas dataframe
temp = []
for index in xrange(len(news)) :
    temp.append( [ news[index], news[index+1].replace('\n',''), news[index+3].replace('\r','') ] )
    index = index + 4

articles = pd.DataFrame(temp)

#Writing the data to a file
json_articles = articles.to_json()
with open('./static/news.json', 'w+') as f:
    f.write(json_articles)
