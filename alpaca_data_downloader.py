

from timeit import default_timer as timer 
import time
#from datetime import datetime
import pandas as pd
import csv
import numpy as np
import talib as ta
import math
import csv
import time
import matplotlib.pyplot as mp
from numpy import inf
import numpy as np
from timeit import default_timer as timer
import decimal
import random
import schedule
import timeit
from csv import writer
from itertools import zip_longest
#from datetime import date
from datetime import timedelta
from datetime import date
import calendar
import warnings
#from datetime import datetime
import datetime 
import urllib.request
from statistics import mean
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from twilio.rest import Client
from os import environ
from win32gui import SetWindowPos
import tkinter as tk
import winsound
import platform
import socket
import os
from datetime import datetime


warnings.filterwarnings('ignore')

alpaca_keys = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

# keys required for stock historical data client
data_client = StockHistoricalDataClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0])
trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])





def alpaca_data_downloader():

    print("Portfolio Trading Mode:", alpaca_keys['Portfolio Type'][0])
    
    print("ALPACA DATA DOWNLOADER COMMENCING")
    
    
    pd.set_option('display.max_columns', 10000)
    ticker_grades_csv = pd.read_csv("ticker_list_today.csv")
    #print(ticker_grades_csv)
    
    
    ticker_csv_data = ticker_grades_csv['Tickers'].to_numpy().tolist()
    #print("Ticker List Today:", ticker_csv_data)
    
    exchange_csv_data = ticker_grades_csv['Exchange'].to_numpy().tolist()
    #print("Exchange Data:", exchange_csv_data)
    
    
    tickers = ticker_csv_data
    
    ##exchange = ['NYSE','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ']
    exchange = exchange_csv_data
    
    
    
    #print("TREND FOLLOWING ONLY")
    
    
    
    
    
    #print("TRADING COMMENCING")
    
    #print('------------------------------------------------')
    
    
    while True:
        
        for ticker, exchange_market in zip(tickers, exchange):
            #print("Trend Percentage Value:", trend_percentage_data_items)
            #urllib.request.urlopen('http://google.com') #Python 3.x
            #print("Internet Connection Detected - Stock Trading Bot")
            #time.sleep(1)
            
            #e = datetime.datetime.now()
            #current = ("%s:%s:%s" % (e.hour, e.minute, e.second))
            #print("Current Time:", current)
        
            start = timer()
            
            #print('------------------------------------------------')
            #print("Ticker Symbol:", ticker)
       
          
            
            today = date.today()
            #print("Today is: ", today)           
            # Yesterday date
            curr_date = date.today()
            
            ####print(calendar.day_name[curr_date.weekday()])
            
            
            
            today_initial_data = date.today()
            y = today_initial_data.strftime("%Y-%m-%d")
            #y =  dt.strftime("%m-%d %H:%M")
            #print(x)
            #print(y)
            NY = 'America/los_angeles'
            end=pd.Timestamp(y, tz=NY)
            #print(end)       
            time_string_initial_data = y
            #print("Current Day:", time_string_initial_data)
            
            
            
            
            ##data = pd.read_csv(csv)          
            #print(data)
            next_day = today - timedelta(days = -1)
            #print("Yesterday was: ", yesterday)
            #dt = datetime.now()
            # Format datetime string
            z = next_day.strftime("%Y-%m-%d")
            #y =  dt.strftime("%m-%d %H:%M")
            #print(x)
            #print(y)
            NY = 'America/los_angeles'
            end=pd.Timestamp(z, tz=NY)
            #print(end)
            time_string_next_day = z
            ####print("Next Day:", time_string_next_day)
              
    
            
    
            start_time = pd.to_datetime(time_string_initial_data+' 07:30:00-07:00', utc=True)
            end_time = pd.to_datetime(time_string_initial_data+' 09:00:00-07:00', utc=True)
           
            
            
            
            request_params = StockBarsRequest(
                    symbol_or_symbols=ticker,
                    timeframe=TimeFrame.Minute,
                    start=start_time,
                    end=end_time,
                    adjustment = 'split',
                    feed = 'sip'
                    )
            #print(request_params)
            
            
            
            
            # Fetch the bars and format as a dataframe
            minute_bars = data_client.get_stock_bars(request_params).df
            minute_bars = minute_bars.reset_index()
            minute_bars = minute_bars.set_index('timestamp')
            minute_bars.drop(['symbol'], axis=1)
            #print(minute_bars)
            # Convert to market time for easier reading
            minute_bars = minute_bars.tz_convert('America/Los_angeles')
            # Resample the bars to get hourly bars for only market hours
            #print(minute_bars)
            #print("Length of Minute Bars:", len(minute_bars))
            if(len(minute_bars) == 0):
                nothing = 0
            else:
                agg_functions = {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum', }
                minute_bars_initial = minute_bars.resample('1Min', offset='30T').agg(agg_functions).between_time('6:30', '12:59')
                #print(minute_bars_initial)
                minute_bars_initial = minute_bars_initial.reset_index()
                minute_bars_initial.rename(columns={"timestamp":"time"}, inplace=True)
                minute_bars_initial.rename(columns={"volume":"Volume"}, inplace=True)
                #print(minute_bars_initial)
                minute_bars_initial = minute_bars_initial.dropna() 
                
            
       
                #data = 'testing123.csv'
                #colNames = data.columns
                ##print(colNames)                       
                df_new = pd.DataFrame(data=minute_bars_initial)
                df_new = df_new.dropna() 
                #print(df_new)                                             
                df_new.to_csv('tradingview_'+ticker+'_data.csv', index=False)
                
                #print('------------------------------')
    
                
        break
    
    print("ALPACA DATA DOWNLOADER COMPLETE")
    
    
    
alpaca_data_downloader()                    
                    
    
         










