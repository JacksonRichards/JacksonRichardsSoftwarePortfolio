

import alpaca_trade_api as api
from timeit import default_timer as timer 
import time
from datetime import datetime
import pandas as pd
import csv
import numpy as np
import math
import time
from numpy import inf
import numpy as np
from timeit import default_timer as timer
import decimal
import random
import schedule
from alpaca_trade_api.stream import Stream
from alpaca_trade_api.common import URL
from alpaca_trade_api.rest import REST
import alpaca_trade_api as tradeapi
import timeit
from itertools import zip_longest
from datetime import date
from datetime import timedelta
from datetime import date
import calendar
import warnings
import datetime
import urllib.request


warnings.filterwarnings('ignore')

api_keys_csv = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

if(api_keys_csv['Portfolio Type'][0] == True):

    BASE_URL = "https://paper-api.alpaca.markets"
    API_KEY = api_keys_csv['API KEY'][0]
    API_SECRET = api_keys_csv['API SECRET KEY'][0]
    alpaca = api.REST(API_KEY, API_SECRET)
    api = tradeapi.REST(key_id=API_KEY, secret_key=API_SECRET, 
                        base_url=BASE_URL, api_version='v2')
    "@jacksonw911@gmail.com"

elif(api_keys_csv['Portfolio Type'][0] == False):

    BASE_URL = "https://api.alpaca.markets"
    API_KEY = api_keys_csv['API KEY'][0]
    API_SECRET = api_keys_csv['API SECRET KEY'][0]
    alpaca = api.REST(API_KEY, API_SECRET)
    api = tradeapi.REST(key_id=API_KEY, secret_key=API_SECRET, 
                        base_url=BASE_URL, api_version='v2')
    "@jacksonw911@gmail.com"


def portfolio_data_scrapper():


    print("PORTFOLIO SCRAPING COMMENCING")
    
    while True:
    
        try:
        
            today_initial_data = date.today()
            y = today_initial_data.strftime("%Y-%m-%d")
            #y =  dt.strftime("%m-%d %H:%M")
            #print(x)
            #print(y)
            NY = 'America/los_angeles'
            end=pd.Timestamp(y, tz=NY)
            #print(end)       
            record_date = y
            #record_date = time_string_initial_data.replace('0', '')
            ####print("Current Day:", record_date)
            
            
            trade_history = api.get_portfolio_history(date_start=record_date, date_end=record_date, extended_hours=True).df.tz_convert('US/Pacific')
            pd.set_option('display.max_rows', 100)
            #print(trade_history)
            #print(trade_history.df)
            trade_history.to_csv('portfolio_data.csv')

            
            print("PORTFOLIO SCRAPING COMPLETE")
            
            break
            
        except:
            print("No Internet Connection, Attempting Reconnection... - Stock Trading Bot")
            time.sleep(0.5)


portfolio_data_scrapper()




















