# TEAM BACKEND
# 
# Description: takes in a sports news archive url and grabs all the article 
# headlines and urls for each sport 
# 
# Structure: [ [ [article_urls], [headlines], [article_dates] ], ...]
# Each slot in the over all array is a sport
# Each sport has 2 arrays

import sys
sys.path.insert(0, './lib')
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import io
import json
from urls import news_urls
import urllib2

news = []
dataframes = []

articles_by_sport = []

for u in xrange(len(news_urls)): 
    url = news_urls[u]
    #print "\nSport #" + str(u) + "\n"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # gets all oldheadline
    article_tags = soup.select(".oldheadline")
    
    article_urls = []
    headlines = []
    article_dates = []

    # for every article archive, it stores all the individual article links,
    # headlines, and article dates
    for i in xrange(len(article_tags)):
        
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
            #print link
            if len(article_urls) != 0  and link == article_urls[len(article_urls)-1]:
                continue
            
            # goes into the article link to download/store the image
            # download image corresponding to article as [index].jpg
            aPage = requests.get( 'http://' + link )
            aSoup = BeautifulSoup(aPage.content, 'html.parser')
            
            # finds image url
            try :
                imgLink = [ j for j in aSoup.select('#GlobalArticleContainer img') if j.has_attr('title') ][0]['src']
            except IndexError:
                continue
            
            # puts image into directory and downloads the image
            # for example, the first baseball article w ul be at ./news/0/0.jpg , 'wb' means write in binary 
	    if not os.path.exists("./static/news/"):
    	        os.makedirs("./static/news/") 
            with open( "./static/news/" + str(len(article_urls)) +".png", 'w+b' ) as out_file:
                img = urllib2.urlopen(imgLink)
                out_file.write( img.read() )
                out_file.close()
            
            # appends article url and headlines per sport
            article_urls.append(link)
            headlines.append(article_tags[i].get_text())


        # parse dates -- there are 6 sections per <TR> tag -- which is how the articles are divided
        if i % 7 == 1 and len(article_urls) == len(article_dates) :
            article_dates.append(article_tags[i].get_text().replace("\t","").replace("\n",""))

    
    # append all the lists into a single list
    per_sport = []
    per_sport.append(article_urls)
    per_sport.append(headlines)
    per_sport.append(article_dates)

    news.append(per_sport)

    # used to add to data frame (panda)
    temp = []
    for index in xrange(len(article_urls)) :
        temp.append( [ article_urls[index], headlines[index].replace('\n',''), article_dates[index].replace('\r','') ] ) 

    articles_by_sport.append(temp)

# Placing the data into a Pandas dataframe
articles = pd.DataFrame({
    "articles": articles_by_sport
})

#Writing the data to a file
json_articles = articles.to_json()
with open('./static/news.json', 'w+') as f:
    f.write(json_articles)
