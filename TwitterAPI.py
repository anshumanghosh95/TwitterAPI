# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:55:42 2019

@author: anshu
"""

import tweepy
import pandas as pd
import plotly
from plotly import plotly as py
from plotly import graph_objs as go
#from IPython.display import HTML, display

plotly.tools.set_credentials_file(username='<plotly user_name>', api_key='<plotly api_key>') 
#create account in plotly to get username and key
#create app in twitter developer and obtain below for parameter
consumer_key = "<twitter consumer Key>"
consumer_secret = "<twitter consumer secret>"
access_key = "<twitter access key>"
access_secret = "<twitter access secret>"

# Function to extract tweets 
def get_tweets(username): 
		
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_key, access_secret) 
    api = tweepy.API(auth) 
    tweets = api.user_timeline(screen_name=username)
    
    tweet_list = []
    #print(dir(tweets[0]))
    
    for tweet in tweets:
        tweet_details = {}
        tweet_details['text'] =tweet.text
        tweet_details['retweet_count'] =tweet.retweet_count
        tweet_details['favorite_count'] = tweet.favorite_count
        tweet_details['truncated'] = tweet.truncated
        tweet_details['creation time'] =tweet.created_at
        tweet_list.append(tweet_details)
    
    data = pd.DataFrame(tweet_list)
    fav = go.Bar(
        x=data['text'],
        y=data['favorite_count'],
        name='Favorite Count'
        )
    retweet = go.Bar(
        x=data['text'],
        y=data['retweet_count'],
        name='Retweet Count'
            )

    data_vis = [fav, retweet]
    layout = go.Layout(
    barmode='group'
    )

    fig = go.Figure(data=data_vis, layout=layout)
    py.iplot(fig, filename='grouped-bar', fileopt = 'overwrite') #To plot charts online
    #display(HTML('<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plot.ly/~anshumanghosh95/0.embed"></iframe>'))
    
if __name__ == '__main__': 

	get_tweets("narendramodi") 
