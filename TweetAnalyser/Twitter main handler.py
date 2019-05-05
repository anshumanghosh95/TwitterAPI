# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:48:37 2019

@author: anshu
"""

import pandas as pd
from TwitterAPI import get_tweets
from Emotion_analyser import emtion_analyser

try:
    ta = get_tweets()
    userid = str(input('Please provide a twitter handle: '))
    getdata = pd.DataFrame()
    getdata = ta.tweetdetails(userid)
    ea = emtion_analyser(getdata[['text','lang','truncated']])
    ea.analyse()
except Exception as e:
    print('Error Occured: ', e)
#print(dataload[['text','lang']])