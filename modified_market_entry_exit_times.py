

import numpy as np
import pandas as pd
import talib as ta
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
import datetime
import urllib.request
from alpaca.trading.client import TradingClient


warnings.filterwarnings('ignore')

alpaca_keys = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])




def modified_traded_data_sheets():
    
    print('MODIFIED MARKET ENTRY TIMES COMMENCING')

    ticker_parameters = pd.read_csv('ticker_parameter_grades.csv')
    
    for item_tickers in ticker_parameters['Ticker']:
    
        #print(item_tickers)
        
        days_data = pd.read_csv('PMAX_'+item_tickers+'_alert_source_tradingview_data.csv')
        days_times = days_data['Timestamp'].to_numpy().tolist()
        #print(days_times)
        
        todays_time = days_data['Timestamp'][len(days_data)-1][0:10]
        #print(todays_time)
        
        df_new = []
        for items in days_times:
            examined_date = items[0:10]
            #print(examined_date)
            if(examined_date == todays_time):
                df_new.append(items)
        #print(empty_array)
        
        
        
        minutes_analysis_period = len(df_new)-1
        #print(minutes_analysis_period)
        
        
        PMAX_posistion_signal_lag = pd.read_csv('PMAX_'+item_tickers+'_alert_source_tradingview_data.csv')
        length_of_PMAX_trade_alerts_lag = len(PMAX_posistion_signal_lag['Trade_Alerts'])-1
        ####print("Length of PMax Alert DF:", length_of_PMAX_trade_alerts_lag)
        lag_period = PMAX_posistion_signal_lag[length_of_PMAX_trade_alerts_lag-minutes_analysis_period:]
        #print(lag_period)
        #lag_position_price = PMAX_posistion_signal_lag['Source_Data'][length_of_PMAX_trade_alerts_lag]
        pd.set_option('display.max_rows', 100000)
        #print(lag_period)
        
        
        today = date.today()
        #today.strftime("%d/%m/%Y")
        #print(today)
        
        index_location = np.where(lag_period['Timestamp'] == str(today)+' 06:30:00-07:00')
        #print(index_location)
        number = index_location[0][0]
        #print(number)
        #print(lag_period['Timestamp'].to_numpy().tolist()[number])
        
        
        first_half = lag_period.iloc[:number]
        #print(first_half)
        second_half = lag_period.iloc[number:]
        #print(second_half) 
        
        
        trade_alert_append_first_half = []
        for items_first_half_trade_alerts in first_half['Trade_Alerts']:
            if(items_first_half_trade_alerts == 'BUY'):
                trade_alert_append_first_half.append(items_first_half_trade_alerts)
            elif(items_first_half_trade_alerts == 'SELL'):
                trade_alert_append_first_half.append(items_first_half_trade_alerts)
        
        if(len(trade_alert_append_first_half)==0):
            trade_alert_append_first_half.append('HOLD')
        
        #print(trade_alert_append_first_half)
        
    
        #print(second_half.index[0])
        
        
        second_half.loc[second_half.index[0],['Trade_Alerts']]=[trade_alert_append_first_half[len(trade_alert_append_first_half)-1]]
        #print(second_half[:1])
    
        second_half.pop('Unnamed: 0')
        second_half.to_csv('modified_start_exit_times_'+item_tickers+'.csv')
    
    
        #print('-------------------------')

    print('MODIFIED MARKET ENTRY TIMES COMPLETE')    

modified_traded_data_sheets()

  
    
    

        
        
        
        
    


























