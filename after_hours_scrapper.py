# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 00:23:19 2022

@author: jacks
"""


from timeit import default_timer as timer
import time
import pandas as pd
import csv
import ta
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
from datetime import timedelta
from datetime import date
import calendar
import warnings
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
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto3
from botocore.errorfactory import ClientError
import boto


warnings.filterwarnings('ignore')



def Algorithm():
    
    alpaca_keys_data = pd.read_csv('alpaca_api_information_data.csv')
    #paper_tf = pd.read_csv('paper_true_false.csv')
    # keys required for stock historical data client
    data_client = StockHistoricalDataClient(alpaca_keys_data['API KEY'][0], alpaca_keys_data['API SECRET KEY'][0])
    trading_client = TradingClient(alpaca_keys_data['API KEY'][0], alpaca_keys_data['API SECRET KEY'][0], paper=alpaca_keys_data['Portfolio Type'][0])
    "@jacksonw911@gmail.com"

    
    #print("STOCK TRADING BOT COMMENCING") 
    

    pd.set_option('display.max_columns', 10000)
    ticker_grades_csv = pd.read_csv("ticker_parameter_grades.csv")
    #print(ticker_grades_csv)
    
    
    ticker_csv_data = ticker_grades_csv['Ticker'].to_numpy().tolist()
    #print("Ticker List Today:", ticker_csv_data)
    
    exchange_csv_data = ticker_grades_csv['Exchange'].to_numpy().tolist()
    #print("Exchange Data:", exchange_csv_data)
    
    trend_percentage_data = ticker_grades_csv['Trend Percentage'].to_numpy().tolist()
    #print("Trend Percentage Data:", trend_percentage_data)
    
    stop_loss_data = ticker_grades_csv['Stop Loss Percentage'].to_numpy().tolist()
    #print("Stop Loss Percentage:", stop_loss_data)
    
    
    #'AAPL','MSFT' be,
    ##tickers = ['BA','NVDA','PTON','SABR','AAPL','MSFT','AMD','COST','MAR','PYPL']
    tickers = ticker_csv_data
    
    ##exchange = ['NYSE','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ']
    exchange = exchange_csv_data
    
    
    stop_loss = stop_loss_data
    
 
    
    Multiplier_ATR_parameter_grade = ticker_grades_csv['ATR Multiplier'].to_numpy().tolist()
    #print(Multiplier_ATR_parameter_grade)
    
    Length_Tillson_parameter_grade = ticker_grades_csv['Tillson T3 Length'].to_numpy().tolist()
    #print(Multiplier_ATR_parameter_grade)
    
    T3a1_Tillson_Volume_parameter_grade = ticker_grades_csv['T3a1 Tillson Volume'].to_numpy().tolist()
    #print(Multiplier_ATR_parameter_grade)
    
    Period_ATR_parameter_grade = ticker_grades_csv['ATR Length'].to_numpy().tolist()
    #print(Multiplier_ATR_parameter_grade)
    
    rsi_length_parameter_grade = ticker_grades_csv['RSI Length'].to_numpy().tolist()
    #print(Multiplier_ATR_parameter_grade)
    
    
    
    
    Multiplier_ATR_arrays = Multiplier_ATR_parameter_grade
    #print(Multiplier_ATR_arrays)
        
    Length_Tillson_arrays = Length_Tillson_parameter_grade
    #print(Length_Tillson_arrays)
        
    T3a1_Tillson_Volume_arrays = T3a1_Tillson_Volume_parameter_grade
    #print(T3a1_Tillson_Volume_arrays)
        
    Period_ATR_arrays = Period_ATR_parameter_grade
    #print(Period_ATR_arrays)
        
    rsi_length_arrays = rsi_length_parameter_grade
    #print(rsi_length_arrays)
    
    #print('------------------------------')
    ##total_point_average = mean(ticker_grades_csv['Total Points'].to_numpy().tolist())
    #print("Total Point Average:", total_point_average)
    ##total_number_closed_trades_average = mean(ticker_grades_csv['Number of Closed Trades'].to_numpy().tolist())
    #print("Total Closed Trades Average:", total_number_closed_trades_average)
    #print('------------------------------')
    #total_number_profit_factor = mean(ticker_grades_csv['Profit Factor'].to_numpy().tolist())
    #print("Profit Factor Average:", total_number_profit_factor)
    
    #total_number_net_profit_all = mean(ticker_grades_csv['Net Profit All'].to_numpy().tolist())
    #print("Net Profit All Average:", total_number_net_profit_all)
    
    #vix_previous_open = pd.read_csv('vix_amounts.csv')
    #print("VIX Number:", vix_previous_open['Open'][len(vix_previous_open['Open'])-1])
    
    
    #print("TRADING COMMENCING")
    
    #print('------------------------------------------------')
    

    while True:
        
        for ticker, Multiplier_ATR_items, Length_Tillson_items, T3a1_Tillson_Volume_items, Period_ATR_items, rsi_length_items, exchange_market, trend_percentage_data_items, stop_loss_perc in zip(tickers, Multiplier_ATR_arrays, Length_Tillson_arrays, T3a1_Tillson_Volume_arrays, Period_ATR_arrays, rsi_length_arrays, exchange, trend_percentage_data, stop_loss):
            #print("Trend Percentage Value:", trend_percentage_data_items)
            print(ticker)
            
            try:
                
                #urllib.request.urlopen('http://google.com') #Python 3.x
                #print("Internet Connection Detected - Stock Trading Bot")
                #time.sleep(1)
                
                #e = datetime.datetime.now()
                #current = ("%s:%s:%s" % (e.hour, e.minute, e.second))
                #print("Current Time:", current)
            
                start = timer()
                
                #print('------------------------------------------------')
                #print("Ticker Symbol:", ticker)
                csv = "tradingview_"+ticker+"_data.csv"
              
                
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
                  
    
                sim_date = pd.read_csv("sim_date.csv")
                
                
    
                start_time = pd.to_datetime('2024-03-11'+' 06:30:00-07:00', utc=True)
                end_time = pd.to_datetime('2024-03-11'+' 16:59:00-07:00', utc=True)
               
                
                
                
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
                    continue
                else:
                    agg_functions = {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum', }
                    minute_bars_initial = minute_bars.resample('1Min', offset='30T').agg(agg_functions).between_time('6:30', '16:59')
                    #print(minute_bars_initial)
                    minute_bars_initial = minute_bars_initial.reset_index()
                    minute_bars_initial.rename(columns={"timestamp":"time"}, inplace=True)
                    minute_bars_initial.rename(columns={"volume":"Volume"}, inplace=True)
                    #print(minute_bars_initial)
                    minute_bars_initial = minute_bars_initial.dropna() 
                    #print(minute_bars_initial)
                
                    data = pd.read_csv(csv) 
                    #print(data)
                    df_new = pd.DataFrame(data=minute_bars_initial)
                    df_new.to_csv('after_hours_'+ticker+'_data.csv')
                    #print(df_new)

                    #print('-----------------')
                    
                    #print('------------------------------')
                    
                    
    
         
                if(len(minute_bars) == 0):
                    nothing = 0
                    ####print("STOCK NOT REPORTING DATA")
                    ####print('–––––––––––––––––––––––––––––––––––––––––––––––––')
                    ####print('–––––––––––––––––––––––––––––––––––––––––––––––––')
                    
                
                    
                
             
                
            except:
                pass
            
        break
            
        
        

Algorithm()








