
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
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling environ prompt
from win32gui import SetWindowPos
import tkinter as tk
import winsound
import platform
import socket
import os


warnings.filterwarnings('ignore')

alpaca_keys = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

# keys required for stock historical data client
data_client = StockHistoricalDataClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0])
trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])




def Algorithm():
    
    print("STOCK TRADING BOT COMMENCING") 
    
    ticker_grades_csv = pd.read_csv("ticker_list_today.csv")
    #print(ticker_grades_csv)
    
    ticker_csv_data = ticker_grades_csv['Tickers'].to_numpy().tolist()
    print("Ticker List Today:", ticker_csv_data)
    
    exchange_csv_data = ticker_grades_csv['Exchange'].to_numpy().tolist()
    print("Exchange Data:", exchange_csv_data)
    
    position_setting = ticker_grades_csv['Position Setting'].to_numpy().tolist()
    print("Position Setting:", position_setting)
    
    tickers = ticker_csv_data
    
    ##exchange = ['NYSE','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ','NASDAQ']
    exchange = exchange_csv_data
    
    sms_array = []
    while True:
        
        for ticker in tickers:
            
            try:

                sms_array.clear()
                
                
                #current = date.today()
                #current = ("%s:%s:%s" % (e.hour, e.minute, e.second))
                #print("Current Time:", current)
            
                start = timer()
                
                #print('------------------------------------------------')
                #print("Ticker Symbol:", ticker)
                #csv = "tradingview_"+ticker+"_data.csv"
              
                
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
                  
    
                
    
                start_time = pd.to_datetime(time_string_initial_data, utc=True)
                end_time = pd.to_datetime(time_string_next_day, utc=True)
               
                
                
                
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
                    
                
                    #data = pd.read_csv(csv)
                    #data = 'testing123.csv'
                    #colNames = data.columns
                    ##print(colNames)                       
                    df_new = pd.DataFrame(data=minute_bars_initial)
                    df_new = df_new.dropna() 
                    #print(df_new)                                             
                    df_complete = pd.concat([df_new], axis = 0)
                    ##print(df_complete)
                    df_complete = df_complete.dropna() 
                    df_complete.to_csv('new_alpaca_tv_data_'+ticker+'.csv', index=False)
                    
                    
                    
                    
                current_price_data = pd.read_csv('new_alpaca_tv_data_'+ticker+'.csv')
                
                
                request_params = GetOrdersRequest(status='open')
                open_orders_empty = []
                open_orders = trading_client.get_orders(filter=request_params)
                for items_open_orders in open_orders:
                    open_orders_empty.append(items_open_orders.symbol)
                #print(open_orders_empty)       
                if(ticker in open_orders_empty):
                    skip_process = 0
                    #print(ticker, "Open Order")
                    #print('Order Already Open')
                else:
                    ####print("STARTING OPENING PROCESS...")
                    
                    #time_between_trades = 3
                
                    #print('----------------')  
                    
                    portfolio = trading_client.get_all_positions()
                                           
                    array_1 = []
                    for ticker_array_1 in portfolio:
                        array_1.append(ticker_array_1.symbol)
                    #print(array_1)
                    
                    if(ticker in array_1):
                        
                        skip_process = 0
                        
                    else:
                        
                        ticker_list = []
                        ##data = ['NVDA','MSFT','BA','AAPL']
                        data = tickers
                        #data = []
                        #print(data)
                        count_list = len(data)
                        #print(count_list-1)
                        ####print("Processing Ticker List::", data)
                        ticker_list = data                               
                        length_ticker_list = len(ticker_list)
                        
                        ss = []
                        portfolio = trading_client.get_all_positions()
                        for tickerz in portfolio:
                            ticker_symbols = tickerz.symbol
                            ss.append(ticker_symbols)
                        ####print("Current Positions:", ss)
                        ####print('-------------------------------------------------')                                                                                                         
                        for stuff_in_between in ticker_list:
                            one = 1
                            #print(stuff)
                            #print('-----------')
                            for objects in ss:
                                two = 2
                                #print(objects)
                                if(stuff_in_between == objects):
                                   #print(stuff,objects)
                                   ticker_list = [x for x in ticker_list if x!=stuff_in_between]
                                   #print('-----------')
                        length_of_tl = len(ticker_list)       
                        ####print("Starting Ticker List:", ticker_list)                          
                        account = trading_client.get_account()
                        #print(account.cash)
                        # Print Account Details
                        #print("Account ID:", account.id, "||", "Account Equity:", account.equity, "||", "Account Status:", account.status)                                   
                        long_value = float(account.long_market_value)
                        ####print("Long Value:", long_value)
                        short_value = float(account.short_market_value)
                        ####print("Short Value:", short_value)
                        long_short_value = (long_value+abs(short_value))
                        ####print("Long Short Value:", long_short_value)
                        portfolio_value = float(account.portfolio_value)
                        ####print("Portfolio Value:", portfolio_value)                                  
                        cash_unused = portfolio_value - (long_value+abs(short_value))
                        ####print("Cash Unused:", cash_unused)                                   
                        if(length_of_tl != 0):
                            money = cash_unused/length_of_tl
                        elif(length_of_tl == 0):
                            money = 0
                        ####print("Cash Available Per Stock:", money)
                        
                        
                        length_of_PMAX_trade_alerts_lag = len(current_price_data['close'])-1
                        PMAX_posistion_price = current_price_data['close'][length_of_PMAX_trade_alerts_lag]
                        
                        if(position_setting[0] == 'Long'):
                            market_order_data = MarketOrderRequest(symbol=ticker,
                                                qty=int(money/PMAX_posistion_price),
                                                side=OrderSide.BUY,
                                                type='market',
                                                time_in_force=TimeInForce.DAY
                                                )
                            
                            buy = trading_client.submit_order(
                                            order_data=market_order_data
                                           )
                            
                        elif(position_setting[0] == 'Short'):
                            market_order_data = MarketOrderRequest(symbol=ticker,
                                                qty=int(money/PMAX_posistion_price),
                                                side=OrderSide.SELL,
                                                type='market',
                                                time_in_force=TimeInForce.DAY
                                                )
                            
                            buy = trading_client.submit_order(
                                            order_data=market_order_data
                                           )
                
                
                
                    
                    
            except:
             
                try:
                    
                    urllib.request.urlopen('http://google.com') #Python 3.x            
                    print("Other Error")
                    
                     
                    if(len(sms_array) == 0):
                        
                        platform.node()
                        socket.gethostname()
                        computer_name = os.environ['COMPUTERNAME']
                        #print(computer_name)
                        
                        
                        account_sid = "ACf6c7e9b914fd128bfbb9aa40d3137ad5"
                        auth_token = "d05ab69c1fd6ae8eacc508637b150d34"
                        client = Client(account_sid, auth_token)

                        message = client.messages.create(
                          body= computer_name+" Is Offline",
                          from_="+13608543684",
                          to="+15097033070"
                        )
                        

                        print("SMS Sent")
                        
                        frequency = 2500  # Set Frequency To 2500 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                        winsound.Beep(frequency, duration)
                        #time.sleep(0.5)
                    
                    sms_array.append(1)
                    
                    
                    
                    today_initial_data = datetime.now()
                    LA = 'America/los_angeles'

                    error_time=[pd.Timestamp(today_initial_data, tz=LA)]
                    #print(error_time)
                    error_type = ['Non-Network Error']
                    #print(error_type)
                    
                    error_time_df = pd.DataFrame(error_time)
                    #error_time_df.columns = ['Error Time']
                    error_type_df = pd.DataFrame(error_type)
                    #error_type_df.columns = ['Error Time']

                    error_concat = pd.concat([error_time_df,error_type_df], axis = 1)
                    #print(error_concat)

                    error_concat.to_csv('error_records.csv', mode='a', header=False)
                    
                    
                    
                    time.sleep(0.5)
                    

                except:
                    
                    print('Network Error')
                    
                    
                    root = tk.Tk()  # create only one instance for Tk()
                    root.withdraw()  # keep the root window from appearing
                
                    screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
                    win_w = 250
                    win_h = 300
                
                    x = round((screen_w - win_w) / 2)
                    y = round((screen_h - win_h) / 2 * 0.8)  # 80 % of the actual height
                
                    # pygame screen parameter for further use in code
                    screen = pygame.display.set_mode((win_w, win_h))
                
                    # Set window position center-screen and on top of other windows
                    # Here 2nd parameter (-1) is essential for putting window on top
                    SetWindowPos(pygame.display.get_wm_info()['window'], -1, x, y, 0, 0, 1)
                
                    # regular pygame loop
                    WHITE =     (255, 255, 255)
                    RED =       (255,   0,   0)
                    (width, height) = (500, 500)
                
                    background_color = WHITE
                
                    pygame.init()
                    screen = pygame.display.set_mode((width, height))
                    pygame.display.set_caption("ALERT - SOFTWARE STOPPED WORKING")
                    screen.fill(background_color)
                    pygame.display.update()
                    

                    i = 0
                    while True:
                        
                        pygame.draw.circle(screen, RED, (250, 250), 250)
                        pygame.display.update()
                        time.sleep(0.25)
                        pygame.draw.circle(screen, WHITE, (250, 250), 250)
                        pygame.display.update()
                        time.sleep(0.25)
                        
                        frequency = 2500  # Set Frequency To 2500 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                        winsound.Beep(frequency, duration)
                        #time.sleep(0.5)
                        
                        try:
                            urllib.request.urlopen('http://google.com')
                            break
                        except: 
                            print("Internet Not Back Online")
                            time.sleep(0.5)
                            
                            
                    today_initial_data = datetime.now()
                    LA = 'America/los_angeles'

                    error_time=[pd.Timestamp(today_initial_data, tz=LA)]
                    #print(error_time)
                    error_type = ['Internet Error']
                    #print(error_type)
                    
                    error_time_df = pd.DataFrame(error_time)
                    #error_time_df.columns = ['Error Time']
                    error_type_df = pd.DataFrame(error_type)
                    #error_type_df.columns = ['Error Time']

                    error_concat = pd.concat([error_time_df,error_type_df], axis = 1)
                    #print(error_concat)

                    error_concat.to_csv('error_records.csv', mode='a', header=False)
                    
                
                    time.sleep(0.5)
                    
                    
                    
        e = datetime.datetime.now()
        current = ("%s:%s" % (e.hour, e.minute))
        target_time = '12:59'
        #print("Current Time:", current)
        #print(current.lower() == target_time.lower())
        
        account = trading_client.get_account()
        last_equity = float(account.last_equity)
        #print("Last Equity:", last_equity)
        current_equity = float(account.equity)
        #print("Current Equity:", current_equity)
        
        prev_day_perc_change = (current_equity-last_equity)/last_equity
        #print("Current Percentage Value:", prev_day_perc_change)
        
        if(current.lower() == target_time.lower()):
            close_pos = trading_client.close_all_positions(cancel_orders=True)
            #print("TRUE - TRADING FINISHED")
            #print('------------------------------')
            exit_market_time = pd.DataFrame([current])
            exit_market_time.to_csv('market_exit_time.csv')
            exit_market_time.columns = ['Market Exit Time']
            print("STOCK TRADING BOT COMPLETE")
            break
        
        elif(prev_day_perc_change <= -0.0055):
            close_pos = trading_client.close_all_positions(cancel_orders=True)
            print("STOP LOSS FUNCTION INITIATED")
            stop_loss_variable = pd.DataFrame([1])
            stop_loss_variable.columns = ['Stop Loss Variable']
            stop_loss_variable.to_csv('stop_loss_variable.csv')
            exit_market_time = pd.DataFrame([current])
            exit_market_time.columns = ['Market Exit Time']
            exit_market_time.to_csv('market_exit_time.csv')
            break
        elif(prev_day_perc_change >= 0.0025):
            close_pos = trading_client.close_all_positions(cancel_orders=True)
            print("GAIN CAP FUNCTION INITIATED")
            stop_loss_variable = pd.DataFrame([1])
            stop_loss_variable.columns = ['Cap Gain Variable']
            stop_loss_variable.to_csv('cap_gain_variable.csv')
            exit_market_time = pd.DataFrame([current])
            exit_market_time.columns = ['Market Exit Time']
            exit_market_time.to_csv('market_exit_time.csv')
            break
        else:
            nothing = 0
            #print("FALSE - TRADING NOT FINISHED")
            #print('------------------------------')
            #break
            
        time.sleep(0.85)
                        
                
                    
                    
            
        

Algorithm()








