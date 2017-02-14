# arrays for urls

import requests
from bs4 import BeautifulSoup
import pandas as pd

from imp import reload
import sys
import io
import json

reload(sys)
sys.setdefaultencoding('utf-8')


# sport = men's and women's are separated
# 23 sports (indices 0 thru 22)
# 0 -- men's baseball
# 1 -- men's basketball
# 2 -- men's cross country
# 3 -- men's fencing
# 4 -- men's golf
# 5 -- men's rowing
# 6 -- men's soccer
# 7 -- men's swimming and diving
# 8 -- men's tennis
# 9 -- men's track and field
# 10 -- men's volleyball
# 11 -- men's water polo
# 12 -- women's basketball
# 13 -- women's cross country
# 14 -- women's fencing
# 15 -- women's rowing
# 16 -- women's soccer
# 17 -- women's softball
# 18 -- women's swimming and diving
# 19 -- women's tennis
# 20 -- women's track and field 
# 21 -- women's volleyball
# 22 -- women's water polo

roster_urls = []


news_urls = []

# men's baseball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29805&SPID=2331&DB_LANG=C&DB_OEM_ID=5800")

# men's basketball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29884&SPID=2337&DB_LANG=C&DB_OEM_ID=5800")

# men's cross country
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93275&SPID=11063&DB_LANG=C&DB_OEM_ID=5800")

# men's fencing
news_urls.append(




