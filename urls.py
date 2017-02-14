#arrays for urls

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
<<<<<<< HEAD

# men's baseball
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?&DB_OEM_ID=5800&SPID=2331&SPSID=29814")

# men's basketball
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2337&SPSID=29887&DB_OEM_ID=5800")

# men's cross country
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11063&SPSID=93276&DB_OEM_ID=5800")

# men's fencing
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11061&SPSID=93259&DB_OEM_ID=5800")

# men's golf
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2343&SPSID=29952&DB_OEM_ID=5800")

# men's rowing
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2335&SPSID=29862&DB_OEM_ID=5800") 

# men's soccer 
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2328&SPSID=29741&DB_OEM_ID=5800")

news_urls = []
=======


news_urls = []

# men's baseball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29805&SPID=2331&DB_LANG=C&DB_OEM_ID=5800")

# men's basketball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29884&SPID=2337&DB_LANG=C&DB_OEM_ID=5800")

# men's cross country
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93275&SPID=11063&DB_LANG=C&DB_OEM_ID=5800")

# men's fencing
news_urls.append(




>>>>>>> f3a37f773abdf0fa5c81e0107207aff53f8ceba1
