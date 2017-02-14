# individual bios

import requests  # makes a request to web servers to download HTML contents
from bs4 import BeautifulSoup
import pandas as pd  # library that gives you access to data frames

import roster.py

reload(sys)  # allows encoding in something not ASCII
sys.setdefaultencoding('utf-8')

page =
requests.get("http://www.ucsdtritons.com/ViewArticle.dbml?ATCLID=205824389&DB_OEM_ID=5800")
soup = BeautifulSoup(page.content, 'html.parser')
page.status_code


print(soup.prettify())
