

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
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling environ prompt
from win32gui import SetWindowPos
import tkinter as tk
import winsound
import platform
import socket
import os
from datetime import datetime





def terminal_wide_stop_loss_manager():

    while True:
        
        e = datetime.now()
        current_time = e.strftime("%H:%M")
        #print("Current Time =", current_time)

        target_time = '12:59'
        #print(target_time)
        
        if(current_time.lower() != target_time.lower()):
        
            terminals = ['terminal_1','terminal_2','terminal_3','terminal_4','terminal_5','terminal_6']
            
            terminal_wide_SL_logic = []
            for items_terminal in terminals:
                #print(items_terminal)
                
                terminal_x = pd.read_csv('alpaca_api_information_'+items_terminal+'.csv')
                
    
                
                trading_client_SL = TradingClient(terminal_x['API KEY'][0], terminal_x['API SECRET KEY'][0], paper=terminal_x['Portfolio Type'][0])
                
                
                account = trading_client_SL.get_account()
                last_equity = float(account.last_equity)
                #print("Last Equity:", last_equity)
                current_equity = float(account.equity)
                #print("Current Equity:", current_equity)
                
                prev_day_perc_change = (current_equity-last_equity)/last_equity
                #print("Current Percentage Value:", prev_day_perc_change)
                
                
                if(prev_day_perc_change <= -0.0055):                       
                    terminal_wide_SL_logic.append(prev_day_perc_change)
            #print(terminal_wide_SL_logic)    
            if(len(terminal_wide_SL_logic) >= 3):
                
                terminal_x_closing_all_terminals = ['terminal_1','terminal_2','terminal_3','terminal_4','terminal_5','terminal_6']
                
                for items_closing_all_teminals in terminal_x_closing_all_terminals:
                
                    terminal_x = pd.read_csv('alpaca_api_information_'+items_closing_all_teminals+'.csv')
                    
                    
                    trading_client_execute_SL = TradingClient(terminal_x['API KEY'][0], terminal_x['API SECRET KEY'][0], paper=terminal_x['Portfolio Type'][0])
                    
                    
                    close_pos = trading_client_execute_SL.close_all_positions(cancel_orders=True)
                    
                print("ALL TERMINALS LIQUIDATED")
                return()
            else:
                print("TERMINAL WIDE LIQUIDATION NOT ACTIVATED")
                #print(terminal_wide_SL_logic)   
                terminal_wide_SL_logic.clear()
                    
                
            #break
        
        else:
            #print("Not Time Yet")
            nothing = 0
    
terminal_wide_stop_loss_manager()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    