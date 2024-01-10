# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 13:48:54 2023

@author: jacks
"""








import pandas as pd
import numpy as np
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from datetime import date








alpaca_keys = pd.read_csv(r"C:\Users\jacks\Desktop\Open Day High Yielding Stocks\Simmulation\4000 stocks - with indiv stocks - Newest Version High - with volume setting\alpaca_api_information.csv")

#paper_tf = pd.read_csv('paper_true_false.csv')

# keys required for stock historical data client
data_client = StockHistoricalDataClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0])
trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=True)

sim_date = pd.read_csv("sim_date.csv")

today_initial_data = date.today()
y = today_initial_data.strftime("%Y-%m-%d")
LA = 'America/los_angeles'
end=pd.Timestamp(y, tz=LA)    
time_string_initial_data = sim_date['Date'][0]
#print("Current Day:", time_string_initial_data)

start_data_global = time_string_initial_data+' 06:31:00-08:00'
end_data_global = time_string_initial_data+' 07:01:00-08:00'






pd.set_option('display.max_columns', 10000)
ticker_grades_csv = pd.read_csv("ticker_list_today.csv")[0:]
#print(ticker_grades_csv)


tickers = ticker_grades_csv['Tickers'].to_numpy().tolist()
#print("Ticker List Today:", tickers)






perc_append = []
ticker_append = []
volume_sum = []
avg_pps = []
value_traded = []
amount_of_activity_per_minute = []
for ticker in tickers:

    print(ticker)
    start_time = pd.to_datetime(start_data_global, utc=True)
    end_time = pd.to_datetime(end_data_global, utc=True)
   
    
    
    
    request_params = StockBarsRequest(
            symbol_or_symbols=ticker,
            timeframe=TimeFrame.Minute,
            start=start_time,
            end=end_time,
            adjustment = 'split',
            feed = 'sip'
            )
    #print(request_params)
    
    
    
    
    try:
        minute_bars = data_client.get_stock_bars(request_params).df
        
    except:
        ##ticker_append.append(ticker)
        ##percentage_change = 0
        ##perc_append.append(percentage_change)
        continue
    
    
    
    
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
    if(len(minute_bars) == 1):
        #print('YES')
        continue
    else:
        #print(len(minute_bars))
        agg_functions = {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum', }
        minute_bars_initial = minute_bars.resample('1Min', offset='30T').agg(agg_functions).between_time('6:30', '12:59')
        
        minute_bars_initial = minute_bars_initial.reset_index()
        minute_bars_initial.rename(columns={"timestamp":"time"}, inplace=True)
        minute_bars_initial.rename(columns={"volume":"Volume"}, inplace=True)  
        minute_bars_initial = minute_bars_initial.dropna()  
        print(minute_bars_initial)
        minute_bars_initial_volume_sum = sum(minute_bars_initial['Volume'])
        minute_bars_initial_avg_pps = sum(minute_bars_initial['close'])/len(minute_bars_initial['close'])
        minute_bars_initial_value_traded = minute_bars_initial_avg_pps*minute_bars_initial_volume_sum
        minute_bars_initial_value_traded = f'{minute_bars_initial_value_traded:.2f}'
        amount_of_minutes_with_activity = len(minute_bars_initial['close'])
        
        
        minute_bars_initial = minute_bars_initial['close'].to_numpy().tolist()
        
        
        
        percentage_change = (minute_bars_initial[len(minute_bars_initial)-1] - minute_bars_initial[0])/minute_bars_initial[0]
        
        
        
        perc_append.append(percentage_change)    
        ticker_append.append(ticker)
        volume_sum.append(minute_bars_initial_volume_sum)
        avg_pps.append(minute_bars_initial_avg_pps)
        value_traded.append(minute_bars_initial_value_traded)
        amount_of_activity_per_minute.append(amount_of_minutes_with_activity)
    
   
    
perc_df = pd.DataFrame(perc_append)
ticker_df = pd.DataFrame(ticker_append)
volume_sum_df = pd.DataFrame(volume_sum)
avg_pps_df = pd.DataFrame(avg_pps)
value_traded_df = pd.DataFrame(value_traded)
amount_of_activity_per_minute_df = pd.DataFrame(amount_of_activity_per_minute)

combined_df = pd.concat([perc_df, ticker_df, volume_sum_df, avg_pps_df,value_traded_df,amount_of_activity_per_minute_df], axis = 1)
combined_df.columns = ['Percentage','Ticker', 'Volume_Sum', 'Avg PPS', 'Value Traded','Amt of Act In TF']
combined_df.drop(combined_df[combined_df['Volume_Sum'] < 500000].index, inplace = True)
combined_df.dropna(inplace=True)
combined_df.sort_values(by=['Percentage'], inplace=True, ascending=False)
pd.set_option('display.max_rows', 10000)
#print(combined_df)
combined_df.to_csv('stock_beg_performance_1.csv')

























