#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import datetime
from datetime import date
import xlsxwriter
import sys

# credentials from https://apps.twitter.com/
consumerKey = "faihxPpmBp11xVJrNtf5tqekc"
consumerSecret = "BcRhLtrFrj2Mn7AAoKGcclT0JQ6qhSbUJI3A6VZE9xUpmFgB1f"
accessToken = "55815908-VhllSfYNV6pp5KNXWu9V7gAoOKPg6Ch8KoUHMU5cg"
accessTokenSecret = "oBq0iSZH1n6WjnxeGgECr7XXZwe7ta2MGi2nYfTdrVMOC"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

# sys.argv[1]
username = 'ShortThirdMan'
startDate = datetime.datetime(2009, 7, 11, 0, 0, 0)
endDate = date.today()

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)
try:
    while (tmpTweets[-1].created_at >= startDate):
        # print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
        tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
        for tweet in tmpTweets:
            if tweet.created_at < endDate and tweet.created_at > startDate:
                tweets.append(tweet)
except:
   variable='error'

workbook = xlsxwriter.Workbook(username + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Excel file ready")