# pip install feedparser
# pip install notify2
# [Python Desktop News Notifier in 20 lines](http://geeksforgeeks.org/python-desktop-news-notifier-in-20-lines/)
# [Desktop Notifier in Python](https://www.geeksforgeeks.org/desktop-notifier-python/)

import feedparser
import notify2
import os
import time

# https://www.espncricinfo.com/ci/content/rss/feeds_rss_cricket.html

LIVE_SCORES_RSS = 'http://static.cricinfo.com/rss/livescores.xml'

GLOBAL_NEWS_RSS = 'https://www.espncricinfo.com/rss/content/story/feeds/0.xml'

def parseFeed(): 
    f = feedparser.parse(LIVE_SCORES_RSS) 
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('News Notify') 
    for item in f['items']:  
        n = notify2.Notification(item['title'], item['summary'], icon=ICON_PATH) 

    n.set_urgency(notify2.URGENCY_NORMAL) 
    n.show() 
    n.set_timeout(15000) 
    time.sleep(1200) 
      
if __name__ == '__main__': 
    parseFeed() 
