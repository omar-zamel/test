#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ntscraper import Nitter
scraper = Nitter(0)

#Your loops starts here
tweets = scraper.get_tweets("Crypto_Miniime", mode = 'user', instance = 'https://nitter.esmailelbob.xyz') #Loop the desired handles


final_tweets = []
for x in tweets['tweets']:
    data = [x['link'], x['text'],x['date'],x['stats']['likes'],x['stats']['comments']]
    final_tweets.append(data)


import pandas as pd
dat = pd.DataFrame(final_tweets, columns =['twitter_link','text','date','likes','comments'])

dat

