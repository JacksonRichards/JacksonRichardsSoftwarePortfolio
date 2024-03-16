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
    
    
    alpaca_keys_data = pd.read_csv('alpaca_api_information_trading.csv')
    #paper_tf = pd.read_csv('paper_true_false.csv')
    # keys required for stock historical data client
    data_client = StockHistoricalDataClient(alpaca_keys_data['API KEY'][0], alpaca_keys_data['API SECRET KEY'][0])
    trading_client = TradingClient(alpaca_keys_data['API KEY'][0], alpaca_keys_data['API SECRET KEY'][0], paper=alpaca_keys_data['Portfolio Type'][0])
    "@chia11981198@gmail.com"

    
    #print("STOCK TRADING BOT COMMENCING") 
    

    pd.set_option('display.max_columns', 10000)
    ticker_grades_csv = pd.read_csv("ticker_parameter_grades.csv")
    #print(ticker_grades_csv)
    
    
    ticker_csv_data = ticker_grades_csv['Ticker'].to_numpy().tolist()
    print("Ticker List Today:", ticker_csv_data)
    
    exchange_csv_data = ticker_grades_csv['Exchange'].to_numpy().tolist()
    print("Exchange Data:", exchange_csv_data)
    
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
    
    print('------------------------------------------------')
    

    while True:
        
        for ticker, Multiplier_ATR_items, Length_Tillson_items, T3a1_Tillson_Volume_items, Period_ATR_items, rsi_length_items, exchange_market, trend_percentage_data_items, stop_loss_perc in zip(tickers, Multiplier_ATR_arrays, Length_Tillson_arrays, T3a1_Tillson_Volume_arrays, Period_ATR_arrays, rsi_length_arrays, exchange, trend_percentage_data, stop_loss):
            #print("Trend Percentage Value:", trend_percentage_data_items)
            print(ticker)
            
            try:
                
                start = timer()
                
                df_new = pd.read_csv('today_'+ticker+'_data.csv')
                if('Unnamed: 0' in df_new.columns):
                    df_new = df_new.drop(columns=['Unnamed: 0']) 
                    
                
                #csv_PMAX = 'PMAX_'+ticker+'_alert_source_tradingview_data.csv'
                #df_new = pd.read_csv('today_'+ticker+'_data.csv')
                #if('Unnamed: 0' in df_new.columns):
                    #df_new = df_new.drop(columns=['Unnamed: 0'])
                
                
                
                
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
                    schedule.run_pending()
                    #start = timeit.default_timer()
                    
              
                
              
                    e = date.today()
                    ##current = ("%s:%s" % (e.hour, e.minute))
                    
                    current = e.strftime('%H: %M: %S')
                    #target_time = '06: 35: 00'
                    
                    ##target_time = '6:35'
                    #print("Current Time:", current)
                    #print("Target Time:", target_time)
                    #print(current.lower() == target_time.lower())
                    #print(current > target_time)

                    #if(target_time < current):
                        #minutes_analysis_period = 5
                    #else:
                        #minutes_analysis_period = 0
                        
                      
                          
                    minutes_analysis_period = len(df_new)
                    ##print("Length Analysis Period:", minutes_analysis_period)
                    
                    #print(df_new[0:minutes_analysis_period])
                    
                    
                    #qq = []
                    portfolio = trading_client.get_all_positions()
                                           
                    array_1 = []
                    for ticker_array_1 in portfolio:
                        array_1.append(ticker_array_1.symbol)
                    #print(array_1)
                    
                    if(ticker in array_1):
                        #qq.append(ticker)
                        
                        #for stuff in qq:
                            
                        #print(stuff)
                        #position = api.get_position(stuff)
                        #print(position.qty)
                        training_csv = pd.read_csv('tradingview_'+ticker+'_data.csv')
                        training_csv_length = len(training_csv) 
                        
                        
                        csv = 'new_alpaca_tv_data_'+ticker+'.csv'
                        data_lag = pd.read_csv(csv)
                        stock_data_csv_length = len(data_lag)          
                        #print("Lagged Ticker:", lagged_processing_tickers_symbols)                       
                   
                        #print("Length of Missing TV Data:", length_of_missing_tv_data)
                        ####print("Stock Data CSV Length:", stock_data_csv_length)
                        ##print("Lagged Ticker:", ticker)                  
                        ####print("Processing Lagged Trades...")
                        #analyze_period_for_lag = stock_data_csv_length-length_of_missing_tv_data
                        #print("Analysis Length for Lagged Data:", analyze_period_for_lag)
                                                  
                        PMAX_posistion_signal_lag = pd.read_csv('PMAX_'+ticker+'_alert_source_tradingview_data.csv')
                        length_of_PMAX_trade_alerts_lag = len(PMAX_posistion_signal_lag['Trade_Alerts'])-1
                        #print("Length of PMax Alert DF:", length_of_PMAX_trade_alerts_lag)
                        
                        lag_period = PMAX_posistion_signal_lag['Trade_Alerts'][training_csv_length:]
                        #print(lag_period)
                        
                        #lag_position_price = PMAX_posistion_signal_lag['Source_Data'][length_of_PMAX_trade_alerts_lag]
                        pd.set_option('display.max_rows', 100000)
                        #print(lag_period)
                        PMAX_posistion_price = PMAX_posistion_signal_lag['Source_Data'][length_of_PMAX_trade_alerts_lag]

                        #length_of_PMAX_trade_alerts_lag = len(PMAX_posistion_signal_lag['Trade_Alerts'])-length_of_missing_tv_data
                        #PMAX_posistion_signal_final_input_lag = PMAX_posistion_signal_lag['Trade_Alerts'][length_of_PMAX_trade_alerts_lag]
                        lag_period_vectorization = lag_period.to_numpy()
                        #print(lag_period_vectorization)
                        #print(type(lag_period_vectorization))
                  
                        all_lag = np.array(lag_period_vectorization)
                        ####print(all_lag)
                        #print(type(all_lag))
                        buy_lag_index = np.where(all_lag == 'BUY')[0]
                        ####print("BUY Location", buy_lag_index)
                        sell_lag_index = np.where(all_lag == 'SELL')[0]
                        ####print("SELL Location", sell_lag_index)
                        hold_lag_index = np.where(all_lag == 'HOLD')[0]                                                    
                       
                        length_sell_lag = len(sell_lag_index)-1                                        
                        length_buy_lag = len(buy_lag_index)-1                                                                          
                        ####print("Position Sell Occur:", length_sell_lag)        
                        ####print("Position Buy Occur:", length_buy_lag)                         
                       
                        if(length_sell_lag == -1):
                            last_value_sell = 0
                            ####print("Last Sell Value:", last_value_sell)
                        else:                    
                            last_value_sell = sell_lag_index[length_sell_lag]
                            ####print("Last Sell Value:", last_value_sell)
                           
                        if(length_buy_lag == -1):
                            last_value_buy = 0
                            ####print("Last Buy Value:", last_value_buy)
                        else:                    
                            last_value_buy = buy_lag_index[length_buy_lag]
                            ####print("Last Buy Value:", last_value_buy)                           
           
            
           
                        check_all_position = trading_client.get_all_positions()
                        #print(position)
                        for position in check_all_position:
                            if(ticker == position.symbol):
                                #print(position)
                                ticker = position.symbol
                                #print("Ticker:", ticker)
                                quantity = abs(float(position.qty))
                                ####print("Quantity:", quantity)
                                current_price_per_share = float(position.current_price)
                                break
                        
                       
                        
                       
                        if(position.side == 'long'):
                            if(last_value_sell > last_value_buy):
                                ####print("SELL LAG POSITION")                                   
                                market_order_data = MarketOrderRequest(symbol=ticker,
                                                    qty=quantity,
                                                    side=OrderSide.SELL,
                                                    type='market',
                                                    time_in_force=TimeInForce.DAY
                                                    )
                                
                                short = trading_client.submit_order(
                                                order_data=market_order_data
                                               )     
                                ####print("Quantity Requested:", short.qty)
                                
                                
                                while True:
                                    
                                    current_positions_after_close = trading_client.get_all_positions() 
                                    
                                    array_2 = []
                                    for ticker_array_2 in current_positions_after_close:
                                        array_2.append(ticker_array_2.symbol)    
                                        
                                    if(ticker in array_2):
                                        skip = 0
                                        #time.sleep(0.5)
                                        #print('Ticker:', ticker)
                                        #print("CLOSING SHORT POSITION PROCCESSING")
                                    else:
                                        
                                        #print("ORDER SHORT CLOSED")
                                        break
                                    
                                
                                
                                
                                
                            
                    else:  
                        
                        training_csv = pd.read_csv('tradingview_'+ticker+'_data.csv')
                        training_csv_length = len(training_csv) 
                        #print(training_csv_length)
                                                   
                        csv = 'new_alpaca_tv_data_'+ticker+'.csv'
                        data_lag = pd.read_csv(csv)
                        stock_data_csv_length = len(data_lag) 
                        #print(stock_data_csv_length)
                        #print("Lagged Ticker:", lagged_processing_tickers_symbols)                       
                   
                        #print("Length of Missing TV Data:", length_of_missing_tv_data)
                        ####print("Stock Data CSV Length:", stock_data_csv_length)
                        ##print("Lagged Ticker:", ticker)                  
                        ####print("Processing Lagged Trades...")
                        #analyze_period_for_lag = stock_data_csv_length-length_of_missing_tv_data
                        #print("Analysis Length for Lagged Data:", analyze_period_for_lag)
                                                  
                        PMAX_posistion_signal_lag = pd.read_csv('PMAX_'+ticker+'_alert_source_tradingview_data.csv')
                        length_of_PMAX_trade_alerts_lag = len(PMAX_posistion_signal_lag['Trade_Alerts'])-1
                        ####print("Length of PMax Alert DF:", length_of_PMAX_trade_alerts_lag)
                        
                        lag_period = PMAX_posistion_signal_lag['Trade_Alerts'][training_csv_length:]
                        #print(lag_period)
                        
                        #lag_position_price = PMAX_posistion_signal_lag['Source_Data'][length_of_PMAX_trade_alerts_lag]
                        pd.set_option('display.max_rows', 100000)
                        #print(lag_period)
                        PMAX_posistion_price = PMAX_posistion_signal_lag['Source_Data'][length_of_PMAX_trade_alerts_lag]

                        #length_of_PMAX_trade_alerts_lag = len(PMAX_posistion_signal_lag['Trade_Alerts'])-length_of_missing_tv_data
                        #PMAX_posistion_signal_final_input_lag = PMAX_posistion_signal_lag['Trade_Alerts'][length_of_PMAX_trade_alerts_lag]
                        lag_period_vectorization = lag_period.to_numpy()
                        #print(lag_period_vectorization)
                        #print(type(lag_period_vectorization))
                  
                        all_lag = np.array(lag_period_vectorization)
                        ####print(all_lag)
                        #print(type(all_lag))
                        buy_lag_index = np.where(all_lag == 'BUY')[0]
                        ####print("BUY Location", buy_lag_index)
                        sell_lag_index = np.where(all_lag == 'SELL')[0]
                        ####print("SELL Location", sell_lag_index)
                        hold_lag_index = np.where(all_lag == 'HOLD')[0]                                                    
                       
                        length_sell_lag = len(sell_lag_index)-1                                        
                        length_buy_lag = len(buy_lag_index)-1                                                                          
                        ####print("Position Sell Occur:", length_sell_lag)        
                        ####print("Position Buy Occur:", length_buy_lag)                         
                       
                        if(length_sell_lag == -1):
                            last_value_sell = 0
                            ####print("Last Sell Value:", last_value_sell)
                        else:                    
                            last_value_sell = sell_lag_index[length_sell_lag]
                            ####print("Last Sell Value:", last_value_sell)
                           
                        if(length_buy_lag == -1):
                            last_value_buy = 0
                            ####print("Last Buy Value:", last_value_buy)
                        else:                    
                            last_value_buy = buy_lag_index[length_buy_lag]
                            ####print("Last Buy Value:", last_value_buy)                           
           
                        
                        
                        
                        
                        
                        if(last_value_sell < last_value_buy):
                            
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
                            ####print("Length of Original Proccessing List:", length_ticker_list)
                            #print('----------------')                                 
                            #time.sleep(3)
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
                            
                            
                            
                            
                            
                                                                                                
                            market_order_data = MarketOrderRequest(symbol=ticker,
                                                qty=int(money/PMAX_posistion_price),
                                                side=OrderSide.BUY,
                                                type='market',
                                                time_in_force=TimeInForce.DAY
                                                )
                            
                            buy = trading_client.submit_order(
                                            order_data=market_order_data
                                           )
                            
                            
                            
                            ####print("Quantity Requested:", buy.qty)
                            #time.sleep(time_between_trades)
                            
                            while True:
                                
                                current_orders_position = trading_client.get_all_positions()
                                
                                array_8 = []
                                for ticker_array_8 in current_orders_position:
                                    array_8.append(ticker_array_8.symbol)  
                                    
                                if(ticker in array_8):
                                             
                                    #print("INITIAL LONG POSITION OPENING COMPLETE")
                                    break
                                else:
                                    nothing = 0
                                    #skip_process = 0
                                    #print(ticker, "Open Order")
                                    #print('Order Already Open')
                                    #time.sleep(0.5)
                                    #print('Ticker:', ticker)
                                    #print("INITIAL LONG POSITION OPENING STILL PROCCESSING")
                        
                        
                        
                        
   
                        
                     
                #time.sleep(0.85)              
                print("without GPU:", timer()-start)   
                                    
                                    
            
             
                #print('------------------------------')  
            
            
            
            
            
            except:
        
                
                try:
                    
                    urllib.request.urlopen('http://google.com') #Python 3.x            
                    print("Other Error")
                    
                     
    
                        
                    platform.node()
                    socket.gethostname()
                    computer_name = os.environ['COMPUTERNAME']
                    #print(computer_name)
                    
                    
                    account_sid = "ACf6c7e9b914fd128bfbb9aa40d3137ad5"
                    auth_token = "d05ab69c1fd6ae8eacc508637b150d34"
                    client = Client(account_sid, auth_token)
        
                    ##message = client.messages.create(
                      ##body= computer_name+" Is Offline",
                      ##from_="+13608543684",
                      ##to="+15097033070"
                    ##)
                    
        
                    ##print("SMS Sent")
                    
                    ##frequency = 2500  # Set Frequency To 2500 Hertz
                    ##duration = 1000  # Set Duration To 1000 ms == 1 second
                    ##winsound.Beep(frequency, duration)
                    
    
                    
                    
                    
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
                    
                    pass
                    
                    
            
                except:
                    
                    print('Network Error')
                    
                    ##frequency = 2500  # Set Frequency To 2500 Hertz
                    ##duration = 1000  # Set Duration To 1000 ms == 1 second
                    ##winsound.Beep(frequency, duration)
        
                            
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
                    
                    pass
                        
                        
     
            
            #break
        #break
    
        e = datetime.now()
        current_time = e.strftime("%H:%M")
        #print("Current Time =", current_time)

        target_time = '13:00'
        #print(target_time)
        
        #print(current_time.lower() == target_time.lower())
        
        
        
        

        
        
        # Creating the low level functional client
        #client = boto3.client(
            #'s3',
            #aws_access_key_id = '',
            #aws_secret_access_key = '',
            #region_name = ''
        #)
        
        #client.download_file(
            #Filename=r"C:\Users\jacks\Desktop\PMax Algorithm Software - L\company_wide_stop_loss_indicator.csv",
            #Bucket='stoplossindicator',
            #Key='company_wide_stop_loss_indicator.csv'
        #)
        #company_wide_liquidation_kill_code = pd.read_csv('company_wide_stop_loss_indicator.csv')
        #company_wide_liquidation_kill_code_decision = company_wide_liquidation_kill_code['All Portfolio Liquidation'][0]
        
        
        
  
        
        if(current_time.lower() == target_time.lower()):
            ##close_pos = trading_client.close_all_positions(cancel_orders=True)
            #print("TRUE - TRADING FINISHED")
            #print('------------------------------')
            exit_market_time = pd.DataFrame([current_time])
            exit_market_time.to_csv('market_exit_time.csv')
            exit_market_time.columns = ['Market Exit Time']
            #print("STOCK TRADING BOT COMPLETE FOR THE DAY")
            break
        
        ##elif(prev_day_perc_change <= -0.0020):
            ##close_pos = trading_client.close_all_positions(cancel_orders=True)
            ##print("STOP LOSS FUNCTION INITIATED")
            ##stop_loss_variable = pd.DataFrame([1])
            ##stop_loss_variable.columns = ['Stop Loss Variable']
            ##stop_loss_variable.to_csv('stop_loss_variable.csv')
            ##exit_market_time = pd.DataFrame([current_time])
            ##exit_market_time.columns = ['Market Exit Time']
            ##exit_market_time.to_csv('market_exit_time.csv')
            ##break
        ##elif(company_wide_liquidation_kill_code_decision == True):
            ##close_pos = trading_client.close_all_positions(cancel_orders=True)
            ##print("FORCED LIQUIDATION INITIATED")
            ##forced_liquidation = pd.DataFrame([1])
            ##forced_liquidation.columns = ['Forced Liquidation']
            ##forced_liquidation.to_csv('forced_liquidation_variable.csv')
            ##exit_market_time = pd.DataFrame([current_time])
            ##exit_market_time.columns = ['Market Exit Time']
           ##exit_market_time.to_csv('market_exit_time.csv')
            ##break
        else:
            account = trading_client.get_account()
            last_equity = float(account.last_equity)
            current_equity = float(account.equity)
            prev_day_perc_change = (current_equity-last_equity)/last_equity
            specific_time = datetime.now()
            current_time = specific_time.strftime("%H:%M:%S")
            time_data_df = pd.DataFrame([current_time.lower()])
            percentage_data_df = pd.DataFrame([prev_day_perc_change])
            final_port_history_concat = pd.concat([time_data_df,percentage_data_df], axis=1)
            final_port_history_concat.to_csv('portfolio_data.csv', mode='a', header=False) 
            #print("Not Time Yet "+current_time.lower())
            #print("Current Percentage Value:", prev_day_perc_change)
            #print('-------------------------')
            #time.sleep(0)
            #break
            #print("FALSE - TRADING NOT FINISHED")
            #print('------------------------------')
            #break
            
            
        
        

Algorithm()








