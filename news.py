# Joyce Fang
# Description: takes in a sports news archive url and grabs all the article 
# headlines and urls for each sport 

import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import json
from urls import news_urls

page = requests.get(news_urls[0])  # need to change that loops thru each news_urls
soup = BeautifulSoup(page.content, 'html.parser')

article_tags = soup.select(".oldheadline a")

article_urls = []
headlines = []

# stores the headlines and article urls
for a in article_tags:
    if a.has_attr('href'):
        article_urls.append(a['href'])
    headlines.append(a.get_text())

print '\n'.join(article_urls)
print '\n'.join(headlines)
