# Joyce Fang
# 
# Description: takes in a sports news archive url and grabs all the article 
# headlines and urls for each sport 
# 
# Structure: [ [ [article_urls], [headlines], [article_dates] ], ...]
# Each slot in the over all array is a sport
# Each sport has 2 arrays

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import io
import json
from urls import news_urls
import urllib2

news = []
dataframes = []

articles_by_sport = []

for u in xrange(len(news_urls)): 
    url = news_urls[u]
    print "Sport #" + str(u) + "\n"

    page = requests.get(url)  # need to change that loops thru each news_urls
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # get the .oldheadline tag 
    article_tags = soup.select(".oldheadline")
    article_tags2 = soup.select(".oldheadline a")

    
    article_urls = []
    headlines = []
    article_dates = []

    # stores the headlines and article urls
    for i in xrange(len(article_tags)):
        
        children = article_tags[i].findChildren();
        link = ''
        for child in children:
            if child.has_attr('href'):
                link = 'www.ucsdtritons.com/' +  child['href']
        cont = True 
        if  link == '' :
            cont = False

        if cont : 
            print link
            # parse urls -- there are 6 oldheadline sections per <TR> tag -- which is how the articles are divided
            # gets the article direct url
            if len(article_urls) != 0  and link == article_urls[len(article_urls)-1]:
                continue

            # download image corresponding to article as [index].jpg
            #with article_tags[i]['href'] as at:
            aPage = requests.get( 'http://' + link )
            aSoup = BeautifulSoup(aPage.content, 'html.parser')

            try :
                imgLink = [ j for j in aSoup.select('#GlobalArticleContainer img') if j.has_attr('title') ][0]['src']
            except IndexError:
                continue

            article_urls.append(link)
            headlines.append(article_tags[i].get_text())

            print imgLink
            #imgLink = [ j['src'] for j in aSoup.select('#GlobalArticleContainer img') if '.jpg' in j['src']][0]

            # for example, the first baseball article would be at ./news/0/0.jpg , 'wb' means write in binary 
            with open( "./news/"+ str(u) + "/" + str(len(article_urls)-1) +".jpg", 'wb' ) as out_file:
                img = urllib2.urlopen(imgLink)
                out_file.write( img.read() )
                out_file.close()

        # parse dates -- there are 6 sections per <TR> tag -- which is how the articles are divided
        if i % 7 == 1 and len(article_urls) == len(article_dates) :
            article_dates.append(article_tags[i].get_text().replace("\t","").replace("\n",""))


        



    per_sport = []
    per_sport.append(article_urls)
    per_sport.append(headlines)
    per_sport.append(article_dates)

    news.append(per_sport)

    print len(article_urls)
    print len(headlines)
    print len(article_dates)

    temp = []
    for index in xrange(len(article_urls)) :
        temp.append( [ article_urls[index], headlines[index].replace('\n',''), article_dates[index].replace('\r','') ] ) 

    articles_by_sport.append(temp)

# Placing the data into a Pandas dataframe
articles = pd.DataFrame({
    "articles": articles_by_sport
})

#print schedule

#Writing the data to a file
json_articles = articles.to_json()
with open('./news/' + '/articles.json', 'w') as f:
    f.write(json_articles)
