import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import json
from urls import news_urls

page = requests.get(news_urls[0])
soup = BeautifulSoup(page.content, 'html.parser')

article_tags = soup.select(".oldheadline a")

article_urls = []
headlines = []

for a in article_tags:
    if a.has_attr('href'):
        article_urls.append(a['href'])
    headlines.append(a.get_text())

print '\n'.join(article_urls)
print '\n'.join(headlines)
