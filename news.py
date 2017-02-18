# Joyce Fang
# 
# Description: takes in a sports news archive url and grabs all the article 
# headlines and urls for each sport 
# 
# Structure: [ [ [article_urls], [headlines] ],  ...]
# Each slot in the over all array is a sport
# Each sport has 2 arrays

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import io
import json
from urls import news_urls

news = []

for url in news_urls: 
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

    per_sport = []
    per_sport.append(article_urls)
    per_sport.append(headlines)

    news.append(per_sport);
