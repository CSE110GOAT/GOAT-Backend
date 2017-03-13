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
news_urls = []
stats_urls = []
schedule_urls = []

# ROSTER

# 0 -- men's baseball
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?&DB_OEM_ID=5800&SPID=2331&SPSID=29814")
# 1 -- men's basketball
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2337&SPSID=29887&DB_OEM_ID=5800")
# 2 -- men's cross country
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?DB_OEM_ID=5800&SPID=11063&SPSID=93276&KEY=&Q_SEASON=2015")
# 3 -- men's fencing
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11061&SPSID=93259&DB_OEM_ID=5800")
# 4 -- men's golf
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2343&SPSID=29952&DB_OEM_ID=5800")
# 5 -- men's rowing
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2335&SPSID=29862&DB_OEM_ID=5800") 
# 6 -- men's soccer 
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2328&SPSID=29741&DB_OEM_ID=5800")
# 7 -- men's swimming and diving
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11062&SPSID=93268&DB_OEM_ID=5800")
# 8 -- men's tennis
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2345&SPSID=29969&DB_OEM_ID=5800")
# 9 -- men's track and field
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11064&SPSID=93289&DB_OEM_ID=5800")
# 10 -- men's volleyball
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2336&SPSID=29874&DB_OEM_ID=5800")
# 11 -- men's water polo
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2548&SPSID=31939&DB_OEM_ID=5800")

# 12 -- women's  basketball
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2338&SPSID=29897&DB_OEM_ID=5800")
# 13 -- women's cross country
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?DB_OEM_ID=5800&SPID=11063&SPSID=93276&KEY=&Q_SEASON=2015")
# 14 -- women's fencing
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11061&SPSID=93259&DB_OEM_ID=5800") 
# 15 -- women's rowing
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2327&SPSID=29722&DB_OEM_ID=5800")
# 16 -- women's soccer
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2339&SPSID=29910&DB_OEM_ID=5800")
# 17 -- women's softball
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2342&SPSID=29938&DB_OEM_ID=5800")
# 18 -- women's swimming and diving
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11062&SPSID=93268&DB_OEM_ID=5800")
# 19 -- women's tennis
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2332&SPSID=29818&DB_OEM_ID=5800")
# 20 -- women's track and field
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11064&SPSID=93289&DB_OEM_ID=5800")
# 21 -- women's volleyball
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2334&SPSID=31943&DB_OEM_ID=5800")
# 22 -- women's water polo
roster_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2549&SPSID=31947&DB_OEM_ID=5800")

# NEWS
# The link to the news for ALL sports, showing the first 50
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?ROWS_ACROSS=50")
'''
# 0 -- men's baseball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29805&SPID=2331&DB_LANG=C&DB_OEM_ID=5800")
# 1 -- men's basketball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29884&SPID=2337&DB_LANG=C&DB_OEM_ID=5800")
# 2 -- men's cross country
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93275&SPID=11063&DB_LANG=C&DB_OEM_ID=5800&Q_SEASON=2016&U_SPSID=N")
# 3 -- men's fencing
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93257&SPID=11061&DB_LANG=C&DB_OEM_ID=5800")
# 4 -- men's golf
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29950&SPID=2343&DB_LANG=C&DB_OEM_ID=5800")
# 5 -- men's rowing
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29864&SPID=2335&DB_LANG=C&DB_OEM_ID=5800")
# 6 -- men's soccer
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29738&SPID=2328&DB_LANG=C&DB_OEM_ID=5800")
# 7 -- men's swimming and diving
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93266&SPID=11062&DB_LANG=C&DB_OEM_ID=5800")
# 8 -- men's tennis
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29965&SPID=2345&DB_LANG=C&DB_OEM_ID=5800")
# 9 -- men's track and field
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93286&SPID=11064&DB_LANG=C&DB_OEM_ID=5800")
# 10 --men's volleyball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29871&SPID=2336&DB_LANG=C&DB_OEM_ID=5800")
# 11 -- men's water polo
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=31803&SPID=2548&DB_LANG=C&DB_OEM_ID=5800")

# 12 -- women's basketball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29894&SPID=2338&DB_LANG=C&DB_OEM_ID=5800")
# 13 -- women's cross country
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93275&SPID=11063&DB_LANG=C&DB_OEM_ID=5800&Q_SEASON=2016&U_SPSID=N")
# 14 -- women's fencing
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93257&SPID=11061&DB_LANG=C&DB_OEM_ID=5800")
# 15 -- women's rowing
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29716&SPID=2327&DB_LANG=C&DB_OEM_ID=5800")
# 16 -- women's soccer
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29908&SPID=2339&DB_LANG=C&DB_OEM_ID=5800")
# 17 -- women's softball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29935&SPID=2342&DB_LANG=C&DB_OEM_ID=5800")
# 18 -- women's swimming and diving
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93266&SPID=11062&DB_LANG=C&DB_OEM_ID=5800")
# 19 -- women's tennis
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=29816&SPID=2332&DB_LANG=C&DB_OEM_ID=5800")
# 20 -- women's track and field
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=93286&SPID=11064&DB_LANG=C&DB_OEM_ID=5800")
# 21 -- women's volleyball
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=31804&SPID=2334&DB_LANG=C&DB_OEM_ID=5800")
# 22 -- women's water polo
news_urls.append("http://www.ucsdtritons.com/SportArchives.dbml?SPSID=31805&SPID=2549&DB_LANG=C&DB_OEM_ID=5800")
'''
# STATS

# 0 -- men's baseball
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/baseball/2017/teamstat.htm?DB_OEM_ID=5800");
# 1 -- men's basketball
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/mbasketball/2016-17/teamstat.htm?DB_OEM_ID=5800");
# 2 -- men's cross country
stats_urls.append("");
# 3 -- men's fencing
stats_urls.append("");
# 4 -- men's golf
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/mgolf/2016-17/teamstat.htm?DB_OEM_ID=5800");
# 5 -- men's rowing
stats_urls.append("");
# 6 -- men's soccer
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/msoccer/2016/teamstat.htm?DB_OEM_ID=5800");
# 7 -- men's swimming and diving
stats_urls.append("");
# 8 -- men's tennis
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/mtennis/2017/teamstat.htm?&DB_OEM_ID=5800");
# 9 -- men's track and field
stats_urls.append("");
# 10 -- men's volleyball
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/mvolleyball/2017/teamstat.htm?DB_OEM_ID=5800");
# 11 -- men's water polo
stats_urls.append("http://www.ucsdtritons.com/ViewArticle.dbml?DB_OEM_ID=5800&ATCLID=205687919&DB_OEM_ID=5800");
# 12 -- women's basketball
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/wbasketball/2016-17/teamstat.htm?DB_OEM_ID=5800");
# 13 -- women's cross country
stats_urls.append("");
# 14 -- women's fencing
stats_urls.append("");
# 15 -- women's rowing
stats_urls.append("");
# 16 -- women's soccer
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/wsoccer/2016/teamstat.htm?DB_OEM_ID=5800");
# 17 -- women's softball
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/softball/2017/teamstat.htm?DB_OEM_ID=5800");
# 18 -- women's swimming and diving
stats_urls.append("");
# 19 -- women's tennis
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/wtennis/2017/teamstat.htm?DB_OEM_ID=5800");
# 20 -- women's track and field 
stats_urls.append("");
# 21 -- women's volleyball
stats_urls.append("http://www.ucsdtritons.com/fls/5800/stats/wvolleyball/2016/teamstat.htm?DB_OEM_ID=5800");
# 22 -- women's water polo
stats_urls.append("http://www.ucsdtritons.com/ViewArticle.dbml?&DB_OEM_ID=5800&ATCLID=211423801");

# SCHEDULE 

# 0 -- men's baseball
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2331&SPSID=29807&DB_OEM_ID=5800");
# 1 -- men's basketball
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2337&SPSID=29886&DB_OEM_ID=5800");
# 2 -- men's cross country
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPSID=93278&SPID=11063&DB_OEM_ID=5800&Q_SEASON=2016");
# 3 -- men's fencing
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11061&SPSID=93260&DB_OEM_ID=5800");
# 4 -- men's golf
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2343&SPSID=29945&DB_OEM_ID=5800");
# 5 -- men's rowing
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2335&SPSID=29861&DB_OEM_ID=5800");
# 6 -- men's soccer
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2328&SPSID=29740&DB_OEM_ID=5800");
# 7 -- men's swimming and diving
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11062&SPSID=93269&DB_OEM_ID=5800");
# 8 -- men's tennis
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2345&SPSID=29967&DB_OEM_ID=5800");
# 9 -- men's track and field
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11064&SPSID=93290&DB_OEM_ID=5800");
# 10 -- men's volleyball
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2336&SPSID=29875&DB_OEM_ID=5800");
# 11 -- men's water polo
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2548&SPSID=31940&DB_OEM_ID=5800");

# 12 -- women's basketball
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2338&SPSID=29896&DB_OEM_ID=5800");
# 13 -- women's cross country
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPSID=93278&SPID=11063&DB_OEM_ID=5800&Q_SEASON=2016");
# 14 -- women's fencing
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11061&SPSID=93260&DB_OEM_ID=5800");
# 15 -- women's rowing
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2327&SPSID=29721&DB_OEM_ID=5800");
# 16 -- women's soccer
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2339&SPSID=29909&DB_OEM_ID=5800");
# 17 -- women's softball
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2342&SPSID=29937&DB_OEM_ID=5800");
# 18 -- women's swimming and diving
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11062&SPSID=93269&DB_OEM_ID=5800");
# 19 -- women's tennis
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11062&SPSID=93269&DB_OEM_ID=5800");
# 20 -- women's track and field
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=11064&SPSID=93290&DB_OEM_ID=5800");
# 21 -- women's voleyball 
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2334&SPSID=31944&DB_OEM_ID=5800");
# 22 -- women's water polo
schedule_urls.append("http://www.ucsdtritons.com/SportSelect.dbml?SPID=2549&SPSID=31948&DB_OEM_ID=5800");
