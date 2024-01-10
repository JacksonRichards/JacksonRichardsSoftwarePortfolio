
from timeit import default_timer as timer 
import time
from datetime import datetime
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
from datetime import date
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


warnings.filterwarnings('ignore')

alpaca_keys = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

# keys required for stock historical data client
data_client = StockHistoricalDataClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0])
trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])



def post_market_data_updater():
    
    print("POST MARKET DATA UPDATER COMMENCING")

    
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
    total_point_average = mean(ticker_grades_csv['Total Points'].to_numpy().tolist())
    #print("Total Point Average:", total_point_average)
    total_number_closed_trades_average = mean(ticker_grades_csv['Number of Closed Trades'].to_numpy().tolist())
    #print("Total Closed Trades Average:", total_number_closed_trades_average)
    #print('------------------------------')
    
    #vix_previous_open = pd.read_csv('vix_amounts.csv')
    #print("VIX Number:", vix_previous_open['Open'][len(vix_previous_open['Open'])-1])
     
    
    
    
    
    
    
    
    #print("TRADING COMMENCING")
    
    #print('------------------------------------------------')
    
    sms_array = []
    while True:
        
        for ticker, Multiplier_ATR_items, Length_Tillson_items, T3a1_Tillson_Volume_items, Period_ATR_items, rsi_length_items, exchange_market, trend_percentage_data_items, stop_loss_perc in zip(tickers, Multiplier_ATR_arrays, Length_Tillson_arrays, T3a1_Tillson_Volume_arrays, Period_ATR_arrays, rsi_length_arrays, exchange, trend_percentage_data, stop_loss):
            #print("Trend Percentage Value:", trend_percentage_data_items)
            try:
                #pygame.quit()
                sms_array.clear()
                urllib.request.urlopen('http://google.com') #Python 3.x
                #print("Internet Connection Detected - Stock Trading Bot")
                #time.sleep(1)
                
                e = datetime.datetime.now()
                current = ("%s:%s:%s" % (e.hour, e.minute, e.second))
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
                    
                
                    data = pd.read_csv(csv)
                    #data = 'testing123.csv'
                    #colNames = data.columns
                    ##print(colNames)                       
                    df_new = pd.DataFrame(data=minute_bars_initial)
                    df_new = df_new.dropna() 
                    
                    df_new.to_csv('new_alpaca_tv_data_'+ticker+'.csv', index=False)
                    
                    #print('------------------------------')
                    
                    
    
         
                if(len(minute_bars) == 0):
                    nothing = 0
                    ####print("STOCK NOT REPORTING DATA")
                    ####print('–––––––––––––––––––––––––––––––––––––––––––––––––')
                    ####print('–––––––––––––––––––––––––––––––––––––––––––––––––')
                    
                else:
                    data = pd.read_csv('new_alpaca_tv_data_'+ticker+'.csv')
                    
                    
                    
                    Open = data["open"]
                    Close = data["close"]
                    High = data["high"]
                    Low = data["low"]
                    ##Close = Close[~np.isnan(Close)]
                    ##print(Close)
                    #print(Low.to_numpy().tolist())
                    
                
                    
                    length_OCHL_backward_offset = len(Low)-1
                    #print(length_OCHL_backward_offset)
                    length_OCHL_front_offset = len(Low)-1
                    #print(length_OCHL_front_offset)
                
                
                
                
                    'src = input(hl2, title="Source")'
                    #np.set_printoptions(precision=2)  
                    ##src = (High + Low)/2
                    src = Close
                    
                    #print(src)
                    src = src.to_numpy().tolist()
                    #print(src[0:1])
                    
                    
                    
                    
                    src_backward_offset = src[0:length_OCHL_backward_offset]
                    src_forward_offset = src[1:length_OCHL_front_offset+1]
                    
                    
                    close_backward_offset = Close[0:length_OCHL_backward_offset]
                    close_forward_offset = Close[1:length_OCHL_front_offset+1]
                    
                    open_backward_offset = Open[0:length_OCHL_backward_offset]
                    open_forward_offset = Open[1:length_OCHL_front_offset+1]
                    
                    high_backward_offset = High[0:length_OCHL_backward_offset]
                    high_forward_offset = High[1:length_OCHL_front_offset+1]
                    
                    low_backward_offset = Low[0:length_OCHL_backward_offset]
                    low_forward_offset = Low[1:length_OCHL_front_offset+1]
                    
                    
                    
                    'Multiplier = input(title="ATR Multiplier", type=input.float, step=0.1, defval=3.7)'
                    ##Multiplier_ATR = float(decimal.Decimal(random.randrange(1000))/100)           
                    Multiplier_ATR = Multiplier_ATR_items
                    
                    ##Multiplier_ATR = float(decimal.Decimal(random.randrange(1000))/100)
                    #Multiplier_ATR = float(np.random.randint(2.55,6.89,size=1))
                    ##print("ATR Multiplier:", Multiplier_ATR)
                    ##Multiplier_ATR = 1.01
                    
                    'length'
                    Length_Tillson = Length_Tillson_items
                    
                    ##Length_Tillson = float(np.random.randint(5,51,size=1))
                    ##print("Tillson T3 Length:", Length_Tillson)
                    ##Length_Tillson = 5
                    
                    'T3a1'
                    T3a1_Tillson_Volume = T3a1_Tillson_Volume_items
                    
                    ##T3a1_Tillson_Volume = float(decimal.Decimal(random.randrange(1000))/100)
                    #T3a1_Tillson_Volume = float(np.random.randint(1,10,size=1))
                    #print("Tillson T3 Volume Factor:", T3a1_Tillson_Volume)
                    ##T3a1_Tillson_Volume = 8.46
                    
                    'Periods'
                    Period_ATR = Period_ATR_items
                    
                    ##Period_ATR = float(np.random.randint(5,51,size=1))
                    #print("ATR Length:", Period_ATR)
                    ##Period_ATR = 7
                    
                    'rsilength = input(43, minval=1, title="RSI Length")'
                    rsi_length = rsi_length_items
                    
                    ##rsi_length = float(np.random.randint(5,51,size=1))
                    #print("RSI Length:", rsi_length)
                    ##rsi_length = 37
                    
                    
                    
                
                   
                    
                    'i = src>=src[1] ? src-src[1] : 0'
                    #print(src)
                    #print('---------')
                    length_src = len(src)-1
                    #print("length_src:", length_src)
                    src_var = []
                    i_var = [0]
                    
                    for src_prices_backward_offset, src_prices_forward_offset in zip(src_backward_offset, src_forward_offset): 
                        #src_var.append(src_prices)
                        #print(src_var)
                        if(src_prices_forward_offset >= src_prices_backward_offset):
                            #i = src_prices_forward_offset - src_prices_backward_offset
                            i = src_prices_forward_offset - src_prices_backward_offset
                        else:
                            i = 0
                        i_var.append(i)
                        #print(i)
                    #print('----------')
                    #print(i_var)
                    i_array = np.array(i_var)
                    #print(i_array)
                    #print(len(i_array))
                    i_df = pd.DataFrame(i_array)
                    pd.set_option('display.max_rows', 10000)
                    #print(i_df)
                    
                    
                    
                    
                    'i2 = src<src[1] ? src[1]-src : 0'
                    #print(src)
                    #print('---------')
                    length_src = len(src)
                    ###print("length_src:", length_src)
                    src_var = []
                    i2_var = [0]
                    for src_prices_backward_offset, src_prices_forward_offset in zip(src_backward_offset, src_forward_offset): 
                        #src_var.append(src_prices)
                        #print(src_var)
                        if(src_prices_forward_offset < src_prices_backward_offset):
                            i2 = src_prices_backward_offset - src_prices_forward_offset
                        else:
                            i2 = 0
                        i2_var.append(i2)
                        #print(i)
                        #print("Value: %.2f" % float(i2))
                    #print('----------')
                    #print(i2_var)
                    i2_array = np.array(i2_var)
                    #print(i2_array)
                    i2_df = pd.DataFrame(i2_array)
                    pd.set_option('display.max_rows', 10000)
                    #print(i2_df)
                    
                    
                    ###print("i_array:", len(i_array))
                    ###print("i2_array:", len(i2_array))
                    
                    
                    
                    
                    
                    'Wwma_Func(src,rsilength)=>'
                    
                    'wwalpha = 1/ rsilength'
                    'WWMA = 0.0'
                    'WWMA := wwalpha*src + (1-wwalpha)*nz(WWMA[1])'
                    #wwma = 0
                    
                    
                    wwalpha = 1/rsi_length
                    
                    
                    #wwma_1 = wwalpha*src_forward_offset[0]+(1-wwalpha)*0
                    #print(wwma)
                    #wwma_array_test.append(wwma_1)
                    #print(wwma_array_test)
                    
                    #wwma_2 = wwalpha*src_forward_offset[1]+(1-wwalpha)*wwma_1
                    #print(wwma)
                    #wwma_array_test.append(wwma_2)
                    #print(wwma_array_test)
                    
                    
                    length = len(src)
                    #print(length)
                    #print(src[247])
                    
                    
                    #wwma = wwalpha*0.1367185+(1-wwalpha)*0
                    #print(wwma)
                    
                    #sums = 0
                    wwma = 0
                    wwma_array = [0]
                    for src_prices_forward_offset in src_forward_offset:
                        #print(length_sums)
                        
                        wwma = wwalpha*src_prices_forward_offset+(1-wwalpha)*wwma
                        
                        wwma_array.append(wwma)
                            
                        #print(wwma)
                        #print(wwma_array)
                        #sums = sums + 1
                    ###print("wwma_array:", len(wwma_array))
                    #print(wwma_array)
                    #print(s_array)
                    pd.set_option('display.max_rows', 10000)
                    wwma_pd = pd.DataFrame(wwma_array)
                    #print(wwma_pd)
                    
                    
                    
                    
                    
                    
                    
                    'AvUp = Wwma_Func(i,rsilength)'
                    'AvDown = Wwma_Func(i2,rsilength)'
                    'NOT SURE ABOUT THESE FUNCTIONS YET - ADDRESS LATER'
                    
                    AvUp_array = []
                    AvDown_array = []
                    AvUp = 0
                    AvDown = 0
                    for i1_num, i2_num in zip(i_array, i2_array):
                        #print(wwma_var)
                        AvUp = wwalpha*i1_num+(1-wwalpha)*AvUp
                        AvDown = wwalpha*i2_num+(1-wwalpha)*AvDown
                        AvUp_array.append(AvUp)
                        AvDown_array.append(AvDown)
                        #print(AvUp)
                        #print(wwma_i2)
                        #break
                    #print(wwma_i1_array)
                    #print(wwma_i2_array)
                    #print(AvUp_array)
                    #print(AvDown_array)
                    
                    #print(len(AvUp_array))
                    #print(len(AvDown_array))
                    
                    ###print("AvUp_array:", len(AvUp_array))
                    ###print("AvDown_array:", len(AvDown_array))
                    
                    
                    
                    
                    
                    'AvgUp = sma(i,rsilength)'
                    'AvgDown =sma(i2,rsilength)'
                    AvgUp = ta.SMA(i_array, timeperiod = rsi_length)
                    #print(AvgUp)
                    #print('-------------')
                    AvgDown = ta.SMA(i2_array, timeperiod = rsi_length)
                    #print(AvgDown)
                    
                    #print(len(AvgUp))
                    #print(len(AvgDown))
                    
                    ###print("AvgUp:", len(AvgUp))
                    ###print("AvgUp:", len(AvgUp))
                    
                    
                    
                    'k1 = high>close[1] ? high-close[1] : 0'
                    'k2 = high<close[1] ? close[1]-high : 0'
                    'k3 = low>close[1] ? low-close[1] : 0'
                    'k4 = low<close[1] ? close[1]-low : 0'
                    k1_array = [0]
                    k2_array = [0]
                    k3_array = [0]
                    k4_array = [0]
                    for prices_high, prices_low, prices_close, close_prices_backward_offset, close_prices_forward_offset, open_prices_backward_offset, open_prices_forward_offset, high_prices_backward_offset, high_prices_forward_offset, low_prices_backward_offset, low_prices_forward_offset in zip(High, Close, Low, close_backward_offset, close_forward_offset, open_backward_offset, open_forward_offset, high_backward_offset, high_forward_offset, low_backward_offset, low_forward_offset):
                    #for prices_high, prices_low, prices_close in zip(High, Close, Low):  
                        if(high_prices_forward_offset > close_prices_backward_offset):
                            k1 = high_prices_forward_offset - close_prices_backward_offset
                        else:
                            k1 = 0
                        #print(k1)
                        k1_array.append(k1)
                        
                        
                        if(high_prices_forward_offset < close_prices_backward_offset):
                            k2 = close_prices_backward_offset - high_prices_forward_offset
                        else:
                            k2 = 0
                        #print(k2)
                        k2_array.append(k2)
                        
                        
                        if(low_prices_forward_offset > close_prices_backward_offset):
                            k3 = low_prices_forward_offset - close_prices_backward_offset
                        else:
                            k3 = 0
                        #print(k3)
                        k3_array.append(k3)
                        
                        
                        if(low_prices_forward_offset < close_prices_backward_offset):
                            k4 = close_prices_backward_offset - low_prices_forward_offset
                        else:
                            k4 = 0
                        #print(k4)
                        k4_array.append(k4)
                    
                    
                    #print(k1_array) 
                    #print('--------')
                    #print(k2_array)
                    #print('--------')
                    #print(k3_array)
                    #print('--------')
                    #print(k4_array)  
                    
                    ###print("k1_array:", len(k1_array))
                    ###print("k2_array:", len(k2_array))
                    ###print("k3_array:", len(k3_array))
                    ###print("k4_array:", len(k4_array))
                        
                        
                    'AvgUpH=(AvgUp*(rsilength-1)+ k1)/rsilength'
                    'AvgDownH=(AvgDown*(rsilength-1)+ k2)/rsilength'
                    'AvgUpL=(AvgUp*(rsilength-1)+ k3)/rsilength'
                    'AvgDownL=(AvgDown*(rsilength-1)+ k4)/rsilength'
                    
                    AvgUpH_array = []
                    AvgDownH_array = []
                    AvgUpL_array = []
                    AvgDownL_array = []
                    for AvgUp_var, AvgDown_var, k1_var, k2_var, k3_var, k4_var in zip(AvgUp, AvgDown, k1_array, k2_array, k3_array, k4_array):
                        #print(AvgUp_var)
                        #print(AvgDown_var)
                        
                        AvgUpH = (AvgUp_var*(rsi_length-1)+k1_var)/rsi_length
                        #print(AvgUp_var)
                        AvgUpH_array.append(AvgUpH)
                        AvgDownH = (AvgDown_var*(rsi_length-1)+k2_var)/rsi_length
                        #print(AvgDownH)
                        AvgDownH_array.append(AvgDownH)
                        
                        AvgUpL = (AvgUp_var*(rsi_length-1)+k3_var)/rsi_length
                        #print(AvgUpL)
                        AvgUpL_array.append(AvgUpL)
                        AvgDownL = (AvgDown_var*(rsi_length-1)+k4_var)/rsi_length
                        #print(AvgDownL)
                        AvgDownL_array.append(AvgDownL)
                    
                    #print(AvgUpH_array)  
                    #print('--------')  
                    #print(AvgDownH_array)
                    #print('--------')
                    #print(AvgUpL_array)
                    #print('--------')
                    #print(AvgDownL_array)
                    
                    ###print("AvgUpH_array:", len(AvgUpH_array))
                    ###print("AvgDownH_array:", len(AvgDownH_array))
                    ###print("AvgUpL_array:", len(AvgUpL_array))
                    ###print("AvgDownL_array:", len(AvgDownL_array))
                     
                        
                    'rs = AvUp/AvDown'
                    'rsi= rs==-1 ? 0 : (100-(100/(1+rs)))'
                    'rsh=AvgUpH/AvgDownH'
                    'rsih= rsh==-1 ? 0 : (100-(100/(1+rsh)))'
                    'rsl=AvgUpL/AvgDownL'
                    'rsil= rsl==-1 ? 0 : (100-(100/(1+rsl)))'
                    
                    rs_array = []
                    rsh_array = []
                    rsl_array = []
                    for AvUp_array_rs, AvDown_array_rs, AvgUpH_array_rsh, AvgDownH_array_rsh, AvgHighL_array_rsl, AvgDownL_array_rsl in zip(AvUp_array, AvDown_array, AvgUpH_array, AvgDownH_array, AvgUpL_array, AvgDownL_array):
                        #print(wwma_i1_array_rs)
                        #print(wwma_i2_array_rs)
                        rs = AvUp_array_rs/AvDown_array_rs
                        #print(rs)
                        rs_array.append(rs)
                            
                        rsh = AvgUpH_array_rsh/AvgDownH_array_rsh
                        rsh_array.append(rsh)
                        
                        rsl = AvgHighL_array_rsl/AvgDownL_array_rsl
                        rsl_array.append(rsl)
                      
                        
                    #print(rs_array)
                    #rs_array = np.nan_to_num(rs_array, copy=True)
                    
                    #print(rs_array)
                    #print(rsh_array)  
                    #print(rsl_array)
                    
                    ###print("rs_array:", len(rs_array))
                    ###print("rsh_array:", len(rsh_array))
                    ###print("rsl_array:", len(rsl_array))
                    
                    length_rs_rsh_rsl = len(rs_array)-1
                    #print(length_rs_rsh_rsl)
                    #length_rs_rsh_rsl = len(rsh_array)
                    #print(length_rs_rsh_rsl)
                    #length_rs_rsh_rsl = len(rsl_array)
                    #rint(length_rs_rsh_rsl)
                    rsi_array_var = []
                    rsih_array_var = []
                    rsil_array_var = []
                    for rs_var, rsh_var, rsl_var in zip(rs_array, rsh_array, rsl_array):
                        #print(rs_var)
                        if(rs_var == -1):
                            rsi = 0
                        else:
                            rsi = (100-(100/(1+rs_var)))
                        #print(rsi)
                        rsi_array_var.append(rsi)
                        #print(rsh_var)
                        if(rsh_var == -1):
                            rsih = 0
                        else:
                            rsih = (100-(100/(1+rsh_var)))
                        #print(rsih)
                        rsih_array_var.append(rsih)
                    
                        #print(rsl_var)
                        if(rsl_var == -1):
                            rsil = 0
                        else:
                            rsil = (100-(100/(1+rsl_var)))
                        #print(rsil)
                        rsil_array_var.append(rsil)
                    
                    #print(rsi_array_var)
                    #print(rsih_array_var)
                    #print(rsil_array_var)
                    
                    #print(len(rsi_array_var))
                    #print(len(rsih_array_var))
                    #print(len(rsil_array_var))
                    #print(len(rs_array))
                    #print(len(rsh_array))
                    #print(len(rsl_array))
                    
                    ###print("rsi_array_var:", len(rsi_array_var))
                    ###print("rsih_array_var:", len(rsih_array_var))
                    ###print("rsil_array_var:", len(rsil_array_var))
                    ###print("rs_array:", len(rs_array))
                    ###print("rsh_array:", len(rsh_array))
                    ###print("rsl_array:", len(rsl_array))
                    
                    
                    'TR=max(rsih-rsil,abs(rsih-rsi[1]),abs(rsil-rsi[1]))'
                    length_rsi_rsih_rsil = len(rsil_array_var)
                    #print(length_rsi_rsih_rsil) 
                    
                    rsi_array_var_zero = np.nan_to_num(rsi_array_var)
                    #print(rsi_array_var_zero)
                    
                    rsih_array_var_zero = np.nan_to_num(rsih_array_var)
                    #print(rsih_array_var_zero)
                    
                    rsil_array_var_zero = np.nan_to_num(rsil_array_var)
                    #print(rsih_array_var_zero)
                    
                    
                    
                    rsi_backward_offset = rsi_array_var_zero[0:length_rsi_rsih_rsil]
                    #print(rsi_backward_offset)
                    rsi_forward_offset = rsi_array_var_zero[1:length_rsi_rsih_rsil]
                    
                    rsih_backward_offset = rsih_array_var_zero[0:length_rsi_rsih_rsil]
                    #print(rsi_backward_offset)
                    rsih_forward_offset = rsih_array_var_zero[1:length_rsi_rsih_rsil]
                    
                    rsil_backward_offset = rsil_array_var_zero[0:length_rsi_rsih_rsil]
                    #print(rsi_backward_offset)
                    rsil_forward_offset = rsil_array_var_zero[1:length_rsi_rsih_rsil]
                    
                    TR_1_array = []
                    TR_2_array = [0]
                    TR_3_array = [0]
                    TR_max = []
                    for rsih_TR, rsil_TR in zip(rsih_array_var, rsil_array_var):
                        
                        TR_1 = (rsih_TR - rsil_TR)
                        TR_1_array.append(TR_1)
                    
                    for rsi_TR, items_rsi_backward_offset, items_rsih_forward_offset, items_rsil_backward_offset, items_rsil_forward_offset in zip(rsi_array_var, rsi_backward_offset, rsih_forward_offset, rsil_backward_offset, rsil_forward_offset):
                        
                        TR_2 = abs(items_rsih_forward_offset - items_rsi_backward_offset)
                        TR_2_array.append(TR_2)
                        #print(TR_2)
                        
                        TR_3 = abs(items_rsil_forward_offset - items_rsi_backward_offset)
                        TR_3_array.append(TR_3)
                        #print(TR_3)
                        
                    
                    TR_1_array_zero = np.nan_to_num(TR_1_array)
                    #print(TR_1_array_zero)
                    #print(len(TR_1_array_zero))
                    #print(TR_1_array_zero)
                    
                    #print('----------------')
                    
                    TR_2_array_zero = np.nan_to_num(TR_2_array)
                    #print(TR_2_array_zero)
                    #print(len(TR_2_array_zero))
                    
                    #print('----------------')
                    
                    TR_3_array_zero = np.nan_to_num(TR_3_array)
                    #print(TR_3_array_zero)
                    #print(len(TR_3_array_zero))
                    
                    ###print("TR_1_array_zero:", len(TR_1_array_zero))
                    ###print("TR_2_array_zero:", len(TR_2_array_zero))
                    ###print("TR_3_array_zero:", len(TR_3_array_zero))
                    
                    
                    TR_data = {'TR_1': TR_1_array_zero,
                            'TR_2': TR_2_array_zero,
                            'TR_3': TR_3_array_zero
                            }
                    
                    df_TR = pd.DataFrame(TR_data)
                    pd.set_option('display.max_rows', 5)
                    
                    #print(df_TR)
                    #print('----------')
                    #print(df_TR['TR_1'][95])
                    
                    df_TR_max = df_TR.max(axis=1)
                    #print(df_TR_max)
                    #print(len(TR_3_array_zero))
                    
                    
                    'atr=sma(TR,Periods)'
                    atr = ta.SMA(df_TR_max, timeperiod = Period_ATR)
                    pd.set_option('display.max_rows', 300)
                    #print(atr)
                    #print(len(atr))
                    
                    
                    atr_array = np.array(atr)
                    #print(atr_array)
                    atr_array = np.nan_to_num(atr_array)
                    #print(atr_array)
                    ###print("atr:", len(atr_array))
                    
                    
                    'T3e1=ema(rsi, length)'
                    'T3e2=ema(T3e1,length)'
                    'T3e3=ema(T3e2,length)'
                    'T3e4=ema(T3e3,length)'
                    'T3e5=ema(T3e4,length)'
                    'T3e6=ema(T3e5,length)'
                    rsi_array_var_convert = np.array(rsi_array_var)
                    #print(rsi_array_var_convert)
                    T3e1 = ta.EMA(rsi_array_var_convert, timeperiod = Length_Tillson)
                    #print(T3e1)
                    #print('----------')
                    T3e2 = ta.EMA(T3e1, timeperiod = Length_Tillson)
                    #print(T3e2)
                    #print('----------')
                    T3e3 = ta.EMA(T3e2, timeperiod = Length_Tillson)
                    #print(T3e3)
                    #print('----------')
                    T3e4 = ta.EMA(T3e3, timeperiod = Length_Tillson)
                    #print(T3e4)
                    #print('----------')
                    T3e5 = ta.EMA(T3e4, timeperiod = Length_Tillson)
                    #print(T3e5)
                    #print('----------')
                    T3e6 = ta.EMA(T3e5, timeperiod = Length_Tillson)
                    #print(T3e6)
                    
                    ##print(len(T3e1))
                    ##print(len(T3e2))
                    ##print(len(T3e3))
                    ##print(len(T3e4))
                    ##print(len(T3e5))
                    ##print(len(T3e6))
                    
                    ###print("T3e1:", len(T3e1))
                    ###print("T3e2:", len(T3e2))
                    ###print("T3e4:", len(T3e4))
                    ###print("T3e4:", len(T3e4))
                    ###print("T3e5:", len(T3e5))
                    ###print("T3e6:", len(T3e6))
                    
                    
                    
                    
                    'T3c1=-T3a1*T3a1*T3a1'
                    'T3c2=3*T3a1*T3a1+3*T3a1*T3a1*T3a1'
                    'T3c3=-6*T3a1*T3a1-3*T3a1-3*T3a1*T3a1*T3a1'
                    'T3c4=1+3*T3a1+T3a1*T3a1*T3a1+3*T3a1*T3a1'
                    'T3=T3c1*T3e6+T3c2*T3e5+T3c3*T3e4+T3c4*T3e3'
                    'T3=T3c1*T3e6+T3c2*T3e5+T3c3*T3e4+T3c4*T3e3'
                    'MAvg=T3'
                    
                    T3c1 = -T3a1_Tillson_Volume*T3a1_Tillson_Volume*T3a1_Tillson_Volume
                    #print(T3c1)
                    T3c2 = 3*T3a1_Tillson_Volume*T3a1_Tillson_Volume+3*T3a1_Tillson_Volume*T3a1_Tillson_Volume*T3a1_Tillson_Volume
                    #print(T3c2)
                    T3c3 = -6*T3a1_Tillson_Volume*T3a1_Tillson_Volume-3*T3a1_Tillson_Volume-3*T3a1_Tillson_Volume*T3a1_Tillson_Volume*T3a1_Tillson_Volume
                    #print(T3c3)
                    T3c4 = 1+3*T3a1_Tillson_Volume+T3a1_Tillson_Volume*T3a1_Tillson_Volume*T3a1_Tillson_Volume+3*T3a1_Tillson_Volume*T3a1_Tillson_Volume
                    #print(T3c4)
                    
                    T3 = T3c1*T3e6+T3c2*T3e5+T3c3*T3e4+T3c4*T3e3
                    #print(T3)
                    
                    ##print(len(T3))
                    
                    MAvg = T3
                    #print(MAvg)
                    ###print("MAvg:", len(MAvg))
                    
                    ##print(len(MAvg))
                    
                    
                    'Pmax_Func(rsi,length)=>'
                    '    longStop = MAvg - Multiplier*atr'
                    '    longStopPrev = nz(longStop[1], longStop)'
                    '    longStop := MAvg > longStopPrev ? max(longStop, longStopPrev) : longStop'
                    '    shortStop = MAvg + Multiplier*atr'
                    '    shortStopPrev = nz(shortStop[1], shortStop)'
                    '    shortStop := MAvg < shortStopPrev ? min(shortStop, shortStopPrev) : shortStop'
                    '    dir = 1'
                    '    dir := nz(dir[1], dir)'
                    '    dir := dir == -1 and MAvg > shortStopPrev ? 1 : dir == 1 and MAvg < longStopPrev ? -1 : dir'
                    '    PMax = dir==1 ? longStop: shortStop'
                    'PMax=Pmax_Func(rsi,length)'
                
                
                
                    ls_data = {'MAvg': MAvg,
                            'ATR': atr
                            }
                    
                    df_ls = pd.DataFrame(ls_data)
                    pd.set_option('display.max_rows', 5)
                    #print(df_ls)
                    
                    LongStop = df_ls["MAvg"] - Multiplier_ATR*df_ls["ATR"]
                    #print(LongStop)
                    LongStop = LongStop.to_numpy().tolist()
                    #print(LongStop)
                    
                    ###print("LongStop:", len(LongStop))
                    
                    
                    
                    
                    
                    ss_data = {'MAvg': MAvg,
                            'ATR': atr
                            }
                    
                    df_ls = pd.DataFrame(ls_data)
                    pd.set_option('display.max_rows', 5)
                    #print(df_ls)
                    
                    ShortStop = df_ls["MAvg"] + Multiplier_ATR*df_ls["ATR"]
                    #print(LongStop)
                    ShortStop = ShortStop.to_numpy().tolist()
                    #print(ShortStop)
                    ###print("ShortStop:", len(ShortStop))
                    
                    
                    
                    
                    
                
                    LongStopPrev = 0
                    LongStopAdd = 0
                    #i = 0
                    LongStopPrev_append = []
                    LongStopAdd_append = []
                    for items_LongStopAppend_zero, items_MAvg_append in zip(LongStop, MAvg):
                        #print(items_LongStopPrev)
                        #print(items_LongStopAdd)
                        if(LongStopPrev != 0):
                            LongStopPrev = LongStopAdd
                        else:
                            LongStopPrev = items_LongStopAppend_zero
                        
                        #i =+ 1
                        
                        if(items_MAvg_append > LongStopPrev):
                            LongStopAdd = max(items_LongStopAppend_zero,LongStopPrev)
                        else:
                            LongStopAdd = items_LongStopAppend_zero
                        
                        #print(LongStopPrev)
                        #print(LongStopAdd)
                        LongStopPrev_append.append(LongStopPrev)
                        LongStopAdd_append.append(LongStopAdd)
                    
                    
                    #print(LongStopPrev_append)
                    #print(LongStopAdd_append)
                    
                    #print(len(LongStopPrev_append))
                    #print(len(LongStopAdd_append))
                    
                    ###print("LongStopPrev_append:", len(LongStopPrev_append))
                    ###print("LongStopAdd_append:", len(LongStopAdd_append))
                
                
                
                
                
                    ShortStopPrev = 0
                    ShortStopAdd = 0
                    #i = 0
                    ShortStopPrev_append = []
                    ShortStopAdd_append = []
                    for items_ShortStopAppend_zero, items_MAvg_append in zip(ShortStop, MAvg):
                        #print(items_LongStopPrev)
                        #print(items_LongStopAdd)
                        if(ShortStopPrev != 0):
                            ShortStopPrev = ShortStopAdd
                        else:
                            ShortStopPrev = items_ShortStopAppend_zero
                        
                        #i =+ 1
                        
                        if(items_MAvg_append < ShortStopPrev):
                            ShortStopAdd = min(items_ShortStopAppend_zero, ShortStopPrev)
                        else:
                            ShortStopAdd = items_ShortStopAppend_zero
                        
                        #print(ShortStopPrev)
                        #print(ShortStopAdd)
                        ShortStopPrev_append.append(ShortStopPrev)
                        ShortStopAdd_append.append(ShortStopAdd)
                        
                    #print(ShortStopPrev_append)
                    #print(ShortStopAdd_append)
                    
                    #print(len(ShortStopPrev_append))
                    #print(len(ShortStopAdd_append)
                    
                    ###print("ShortStopPrev_append:", len(ShortStopPrev_append))
                    ###print("ShortStopAdd_append:", len(ShortStopAdd_append))
                
                
                
                    'dir = 1'
                    'dir := nz(dir[1], dir)'
                    'dir := dir == -1 and MAvg > shortStopPrev ? 1 : dir == 1 and MAvg < longStopPrev ? -1 : dir'
                    'PMax = dir==1 ? longStop: shortStop'
                    
                    MAvg_append_zero = np.nan_to_num(MAvg)
                    #print(MAvg_append_zero)
                    
                    dir_var = 1
                    dir_var_append = []
                    PMax_append = []
                    for items_MAvg_append_zero, items_LongStopAdd_append, items_ShortStopAdd_append, items_ShortStopPrev_append, items_LongStopPrev_append, items_LongStopAdd_append, items_ShortStopAdd_append in zip(MAvg_append_zero, LongStopAdd_append, ShortStopAdd_append, ShortStopPrev_append, LongStopPrev_append, LongStopAdd_append, ShortStopAdd_append):
                        #print(items_MAvg_append_zero)
                        #print(items_ShortStopPrevAppend_zero)
                        #print(items_LongStopPrevAppend_zero)
                        #print(items_new_longStop)
                        #print(items_new_ShortStop)
                        if(dir_var == -1 and items_MAvg_append_zero > items_ShortStopPrev_append):
                            dir_var = 1
                            #print(dir_var)
                        elif(dir_var == 1 and items_MAvg_append_zero < items_LongStopPrev_append):
                            dir_var = -1
                            #print(dir_var)
                        else:
                            dir_var = dir_var
                        #print(dir_var)
                        dir_var_append.append(dir_var)
                        
                        if(dir_var == 1):
                            PMax = items_LongStopAdd_append
                        else:
                            PMax = items_ShortStopAdd_append
                        PMax_append.append(PMax)
                    #print(PMax_append)
                    ###print("PMax_append:", len(PMax_append))
                    
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                    alert_append = []
                    for alert_MAvg_append_zero, alert_PMax_append in zip(MAvg, PMax_append):
                        #print(alert_MAvg_append_zero)
                        #print(alert_PMax_append)
                        if(alert_MAvg_append_zero > alert_PMax_append and alert_MAvg_append_zero != 0):
                            ##signal = "SELL"
                            signal = "BUY"
                            #print(signal)
                            alert_append.append(signal)
                            #break
                            
                            ##if(signal == "BUY"):
                                ##signal = "HOLD"
                                ##alert_append.append(signal)
                                ##length_buy = len(alert_append)
                                ##break
                        elif(alert_MAvg_append_zero < alert_PMax_append and alert_MAvg_append_zero != 0):
                            ##signal = "BUY"
                            signal = "SELL"
                            #print(signal)
                            alert_append.append(signal)
                            #break
                            
                            ##if(signal == "SELL"):
                                ##signal = "HOLD"
                                ##alert_append.append(signal)
                        else:
                            signal = "NONE"
                            #print(signal)
                            alert_append.append(signal)
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                
                                
                    #print(alert_append)
                    length_alert = len(alert_append)
                    #print(length_alert)
                    
                    
                    trade_signals = {'trade_signal':  alert_append,
                            }
                    
                    df = pd.DataFrame(trade_signals)
                    pd.set_option('display.max_rows', 500)  
                    
                    #print (df)
                    
                    df['trade_signal'] = df['trade_signal'].mask(df['trade_signal'].eq(df['trade_signal'].shift()))
                    #print(df['trade_signal'])
                    length_alert_df = len(df['trade_signal'])
                    #print(length_alert_df)
                    
                    df['trade_signal'].fillna('HOLD',inplace=True)
                    #print(df['trade_signal'])
                    
                    alert_array = np.array(df['trade_signal'])
                    #print(alert_array)
                    ###print("alert_array:", len(alert_array))
                    
                    length_alert_df = len(alert_array)-1
                    #print(length_alert_df)
                    #print(alert_array[length_alert_df])
                    
                    
                    timestamp_data = {'Timestamp': data['time'],
                            }
                    timestamp_data_df = pd.DataFrame(timestamp_data)
                    #print(timestamp_data_df)
                    
                    
                    ##pd.set_option('display.max_rows', 10000)
                    source_data = {'Source_Data': src,
                            }
                    source_ensure_df = pd.DataFrame(source_data)
                    ##print(source_ensure_df)
                    
                    
                    
                    alert_data = {'Trade_Alerts': alert_array,
                            }
                    alert_ensure_df = pd.DataFrame(alert_data)
                    ##print(alert_ensure_df)
                    
                    
                    pd.set_option('display.max_rows', 5)
                    ensure_one = pd.DataFrame(source_ensure_df)
                    ensure_two = pd.DataFrame(alert_ensure_df)
                    ##ensure_three = pd.DataFrame(timestamp_data_df)
                    ensure_df = pd.concat([ensure_one, ensure_two, timestamp_data_df], axis = 1) 
                    #ensure_df=ensure_df.set_index('Source Data')
                    #print(ensure_df)
                    
                    
                    csv_PMAX = 'PMAX_'+ticker+'_alert_source_tradingview_data.csv'
                    ensure_df = ensure_df.dropna() 
                    ensure_df.to_csv(csv_PMAX)
                    ##print('FINISHED PRINTING TO PMAX CSV')
                    
                    ####print("without GPU:", timer()-start)   
                    ####print('-------------------------------------------------')
                    
                
                    
                
                    
                    
                
                
                
                
                
            except:
                print("No Internet Connection, Attempting Reconnection... - Post Market Data Updater")
                time.sleep(0.5)
                
                
                
                
        print("POST MARKET DATA UPDATER COMPLETE")
        
        break
        
        

post_market_data_updater()








