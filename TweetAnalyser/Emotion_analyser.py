# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:53:44 2019

@author: anshu
"""
import pandas as pd
import nltk
import string

#nltk.download('punkt') # to tokenize word
#nltk.download('averaged_perceptron_tagger') # for pos_tag to tag tokenied word
#nltk.download('stopwords')
class emtion_analyser:
    required_data = pd.DataFrame()
    
    def __init__(self, required_data):
        self.required_data = required_data
    
    def analyse(self):
        try:
            all_text = ''
            for index, text in self.required_data.iterrows():
                if text['lang'] == 'en':
                    all_text += str(text['text'])
            
            token = nltk.tokenize.word_tokenize(all_text)
            sp_list = []
            for i in string.punctuation:
                sp_list.append(i)
            stop_words = []
            stop_words = nltk.corpus.stopwords.words("english")
            stop_words += ['https', '’', '‘'] + sp_list
            filtered_token = []
            for i in token:
                if i not in stop_words:
                    filtered_token.append(i)
            print(filtered_token)
            print((nltk.probability.FreqDist(filtered_token)).most_common(6))
        except Exception as e:
            print('error: ', e)
               