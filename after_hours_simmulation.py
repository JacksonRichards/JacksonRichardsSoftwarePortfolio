# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:43:08 2022

@author: jacks
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 23:59:41 2022

@author: jacks
"""

import pandas as pd
import math
import csv
from array import *
import time
import matplotlib.pyplot as mp
from numpy import inf
import numpy as np
from timeit import default_timer as timer
import decimal
import random
import statistics
import matplotlib.pyplot as plt
import warnings
from datetime import date
from datetime import timedelta
from datetime import date
import urllib.request
from alpaca.trading.client import TradingClient
import os


alpaca_keys = pd.read_csv('alpaca_api_information_trading.csv')

      
last_equity = 100000


ticker_parameters = pd.read_csv('ticker_parameter_grades.csv')
if('Unnamed: 0' in ticker_parameters.columns):
    ticker_parameters = ticker_parameters.drop(columns=['Unnamed: 0']) 


list_of_trades = pd.read_csv('one_day_2_percentage_movements.csv')
if('Unnamed: 0' in list_of_trades.columns):
    list_of_trades = list_of_trades.drop(columns=['Unnamed: 0']) 
    
    
keep_open_trades_first_stock = list_of_trades.drop(list_of_trades[list_of_trades.Ticker != ticker_parameters['Ticker'][0]].index)
#keep_open_trades_first_stock.drop(keep_open_trades_first_stock.tail(1).index,inplace = True)
#print(keep_open_trades_first_stock)
#print(keep_open_trades_first_stock[-1:].to_numpy().tolist()[0])
keep_open_trades_second_stock = list_of_trades.drop(list_of_trades[list_of_trades.Ticker != ticker_parameters['Ticker'][1]].index)
#print(keep_open_trades_second_stock)
#print(keep_open_trades_second_stock[-1:].to_numpy().tolist()[0])
keep_open_trades_third_stock = list_of_trades.drop(list_of_trades[list_of_trades.Ticker != ticker_parameters['Ticker'][2]].index)
#print(keep_open_trades_third_stock)
#print(keep_open_trades_third_stock[-1:].to_numpy().tolist()[0])
keep_open_trades_fourth_stock = list_of_trades.drop(list_of_trades[list_of_trades.Ticker != ticker_parameters['Ticker'][3]].index)
#print(keep_open_trades_fourth_stock)
#print(keep_open_trades_fourth_stock.iloc[-1:].to_numpy().tolist()[0])

position_after_hours = [keep_open_trades_first_stock[-1:].to_numpy().tolist()[0][-2],
                        keep_open_trades_second_stock[-1:].to_numpy().tolist()[0][-2],
                        keep_open_trades_third_stock[-1:].to_numpy().tolist()[0][-2],
                        keep_open_trades_fourth_stock[-1:].to_numpy().tolist()[0][-2]]
#print(position_after_hours)

port_after_hours = [keep_open_trades_first_stock[-1:].to_numpy().tolist()[0][2],
                        keep_open_trades_second_stock[-1:].to_numpy().tolist()[0][2],
                        keep_open_trades_third_stock[-1:].to_numpy().tolist()[0][2],
                        keep_open_trades_fourth_stock[-1:].to_numpy().tolist()[0][2]]
#print(port_after_hours)

times = [keep_open_trades_first_stock[-1:].to_numpy().tolist()[0][-1],
                        keep_open_trades_second_stock[-1:].to_numpy().tolist()[0][-1],
                        keep_open_trades_third_stock[-1:].to_numpy().tolist()[0][-1],
                        keep_open_trades_fourth_stock[-1:].to_numpy().tolist()[0][-1]]
#print(times)

#print('--------------------')
#print('--------------------')
      
percentage_gains_append = []
port_total_append = []
for items_tickers, items_positions_ah, items_port_total, items_times in zip(ticker_parameters['Ticker'],position_after_hours,port_after_hours,times):
    #print(items_tickers)
    
    after_hours_data = pd.read_csv('after_hours_'+items_tickers+'_data.csv')
    if('Unnamed: 0' in after_hours_data.columns):
        after_hours_data = after_hours_data.drop(columns=['Unnamed: 0']) 
        
       
    indices = np.where(after_hours_data == items_times)
    # Extracting row and column indices
    row_indices = indices[0]
    #print(row_indices-1)
    
    opening_price = after_hours_data['close'][row_indices-1].to_numpy().tolist()[0]
    #print(opening_price)
    
    closing_price = after_hours_data['close'].to_numpy().tolist()[-1]
    #print(closing_price)
    
    if(items_positions_ah == 0):
        #print('SHORT')
        #print(items_tickers, items_positions_ah)
        percentage_change_after_hours = (opening_price-closing_price)/opening_price
        #print(percentage_change_after_hours)
        percentage_gains_append.append(percentage_change_after_hours)
    elif(items_positions_ah == 1):
        #print('LONG')
        #print(items_tickers, items_positions_ah)
        percentage_change_after_hours = (closing_price-opening_price)/opening_price
        #print(percentage_change_after_hours)
        percentage_gains_append.append(percentage_change_after_hours)
    
    port_total_append.append(items_port_total*percentage_change_after_hours)
    
    
    #print('------')
    
#print('--------------------')
#print('--------------------') 
    
#print(percentage_gains_append)  


percentage_gains_df = pd.DataFrame(percentage_gains_append) 
percentage_gains_df.columns = ['Percentage']

portfolio_df = pd.DataFrame(port_total_append) 
portfolio_df.columns = ['Portfolio Total']

position_df = pd.DataFrame(position_after_hours) 
position_df.columns = ['Position']
    
final_concat = pd.concat([ticker_parameters['Ticker'],portfolio_df,percentage_gains_df,position_df], axis=1)  
final_concat.to_csv('last_position_value_after_hours.csv')
#print(final_concat) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    