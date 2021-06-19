# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:48:39 2021

@author: padma
"""

import os
import time
import requests
import sys

def retrieve_html():
    for year in range(2009,2020):
        for month in range(1,13):
            if (month < 10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-724050.html'.format(month, year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-724050.html'.format(month, year)
            print('url = ',url)
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8') 
            
            if not os.path.exists("data/html/{}".format(year)):
                os.makedirs("data/html/{}".format(year))
            with open('Data/html/{}/{}.html'.format(year,month), 'wb') as output:
                output.write(text_utf)
        sys.stdout.flush()


if __name__=='__main__':
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    
    print('Time taken {}'.format(stop_time-start_time))