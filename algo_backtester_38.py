

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
import datetime
from talib import stream

startTime = time.time()
def all_backtest_elements():
    #print("ALGORITHM TRAINING COMMENCING")

    warnings.filterwarnings('ignore')
    
    
    ticker_csv_data = pd.read_csv('ticker_list_today.csv')
    #print(ticker_csv_data)
    
    ticker_csv_data = ticker_csv_data['Tickers'].to_numpy().tolist()
    #print("Full Ticker List:", ticker_csv_data) 
    
    #tickers = ['BA','NVDA','PTON','SABR','AAPL','MSFT','AMD','COST','MAR','PYPL','AEP']
    tickers = ticker_csv_data
    #print("Full Ticker List:", tickers) 
    
    
    
    
    dict_append = []
    for ticker in tickers:
        
        
        DATA_SOURCE = 'TRADINGVIEW'
        "OPTIONS: TRADINGVIEW"
        
        "UNCOMMENT FOR TRADINGVIEW DATA:"
        data = pd.read_csv("tradingview_"+ticker+"_data.csv")
        
        
        
        
        
        #ticker_dict = {'ticker': ticker,
                #}
        #close_data = {'close': torch.FloatTensor(data['close']),
                #}
        #open_data = {'open': torch.FloatTensor(data['open']),
                #}
        #high_data = {'high': torch.FloatTensor(data['high']),
                #}
        #low_data = {'low': torch.FloatTensor(data['low']),
                #}
        
        
        ticker_dict = {'ticker': ticker,
                }
        close_data = {'close': (data['close'].to_numpy().tolist()),
                }
        open_data = {'open': (data['open'].to_numpy().tolist()),
                }
        high_data = {'high': (data['high'].to_numpy().tolist()),
                }
        low_data = {'low': (data['low'].to_numpy().tolist()),
                }   
        time_data = {'timestamp': (data['time'].to_numpy().tolist()),
                }
        
        
        my_dict = ticker_dict | close_data | open_data | high_data | low_data | time_data
        
        
        # changes made in dict2
        #print(my_dict['ticker'])
        
        '''
        my_dict["ticker"].append(ticker)
        my_dict["close"].append(data['close'].to_numpy().tolist())
        my_dict["open"].append(data['open'].to_numpy().tolist())
        my_dict["high"].append(data['high'].to_numpy().tolist())
        my_dict["low"].append(data['low'].to_numpy().tolist())
        '''
        
        #df_to_dict = data.to_dict() 
        
        dict_append.append(my_dict)
          
    #print(dict_append)
          
    #for num in dict_append:
        #print(num)
        #print(num['close'][0])
      
     
    #print(my_dict["close"]) 
    #time.sleep(10)
    return(dict_append,tickers)
    
    
    
    
dict_append, tickers = all_backtest_elements()    
    
    
starting_money = 100000


while True:

    for dict_number in dict_append:
        #print(dict_number['ticker'])
 
        def algorithm_body():
            
            start = timer()
            
            
        
            
            Open = dict_number["open"]
            #print(type(Open))
            Close = dict_number["close"]
            #print(type(Close))
            High = dict_number["high"]
            #print(type(High))
            Low = dict_number["low"]
            #print(type(Low))
            
        
            
            length_OCHL_backward_offset = len(Low)-1
            #print(length_OCHL_backward_offset)
            length_OCHL_front_offset = len(Low)-1
            #print(length_OCHL_front_offset)
        
        
        
        
            'src = input(hl2, title="Source")'
            #np.set_printoptions(precision=2)  
            ##src = (High + Low)/2
            src = Close
            
            
            
            
            
            
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
            Multiplier_ATR = float(decimal.Decimal(random.randrange(50, 600))/100)
            
            'length'
            ##Length_Tillson = float(np.random.randint(5,51,size=1))
            Length_Tillson = float(np.random.randint(3,51,size=1))
            
            'T3a1'
            ##T3a1_Tillson_Volume = float(decimal.Decimal(random.randrange(1000))/100)
            T3a1_Tillson_Volume = float(decimal.Decimal(random.randrange(50, 400))/100)
            
            'Periods'
            ##Period_ATR = float(np.random.randint(5,51,size=1))
            Period_ATR = float(np.random.randint(5,150,size=1))
            
            'rsilength = input(43, minval=1, title="RSI Length")'
            ##rsi_length = float(np.random.randint(5,51,size=1))
            rsi_length = float(np.random.randint(5,150,size=1))
            
            
            
        
           
            
            'i = src>=src[1] ? src-src[1] : 0'
            #print(src)
            #print('---------')
            length_src = len(src)-1
            #print("length_src:", length_src)
            #src_var = []
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
            
            
            
            
            
            'i2 = src<src[1] ? src[1]-src : 0'
            #print(src)
            #print('---------')
            
            #src_var = []
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
            #AvgUp = np.nan_to_num(AvgUp)
            #print(AvgUp)
            #print('-------------')
            AvgDown = ta.SMA(i2_array, timeperiod = rsi_length)
            #AvgDown = np.nan_to_num(AvgDown)
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
            #rsi_forward_offset = rsi_array_var_zero[1:length_rsi_rsih_rsil]
            
            #rsih_backward_offset = rsih_array_var_zero[0:length_rsi_rsih_rsil]
            #print(rsi_backward_offset)
            rsih_forward_offset = rsih_array_var_zero[1:length_rsi_rsih_rsil]
            
            rsil_backward_offset = rsil_array_var_zero[0:length_rsi_rsih_rsil]
            #print(rsi_backward_offset)
            rsil_forward_offset = rsil_array_var_zero[1:length_rsi_rsih_rsil]
            
            TR_1_array = []
            TR_2_array = [0]
            TR_3_array = [0]
            #TR_max = []
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
            #T3e1 = np.nan_to_num(T3e1)
            #print(T3e1)
            #print('----------')
            T3e2 = ta.EMA(T3e1, timeperiod = Length_Tillson)
            #T3e2 = np.nan_to_num(T3e2)
            #print(T3e2)
            #print('----------')
            T3e3 = ta.EMA(T3e2, timeperiod = Length_Tillson)
            #T3e3 = np.nan_to_num(T3e3)
            #print(T3e3)
            #print('----------')
            T3e4 = ta.EMA(T3e3, timeperiod = Length_Tillson)
            #T3e4 = np.nan_to_num(T3e4)
            #print(T3e4)
            #print('----------')
            T3e5 = ta.EMA(T3e4, timeperiod = Length_Tillson)
            #T3e5 = np.nan_to_num(T3e5)
            #print(T3e5)
            #print('----------')
            T3e6 = ta.EMA(T3e5, timeperiod = Length_Tillson)
            #T3e6 = np.nan_to_num(T3e6)
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
            
            
            
            trade_signals = {'trade_signal':  alert_append,
                    }
            
            
            
            df = pd.DataFrame(trade_signals)
            pd.set_option('display.max_rows', 500)  
            
            #print (df)
            
            df['trade_signal'] = df['trade_signal'].mask(df['trade_signal'].eq(df['trade_signal'].shift()))
            #print(df['trade_signal'])
            
            
            df['trade_signal'].fillna('HOLD',inplace=True)
            #print(df['trade_signal'])
            
            alert_array = np.array(df['trade_signal'])
            #print(alert_array)
            ###print("alert_array:", len(alert_array))
            
            
            
            
            
            
            length_open_front_offset = len(dict_number['open'])
            src_open = dict_number['open'][1:length_open_front_offset]
            
            
            
            
            
            
            
            source = src_open          
            alert = alert_array
            money = starting_money
            ticker = dict_number['ticker']
            Multiplier_ATR = Multiplier_ATR
            Length_Tillson = Length_Tillson
            T3a1_Tillson_Volume = T3a1_Tillson_Volume
            Period_ATR = Period_ATR
            rsi_length = rsi_length 
            
            
            src_append = []
            for items in source:
                #print("{:f}".format(float(items)))
                src_append.append(items)
            #print(src_append)
            src_append = src_append
            
            
            
            lineCount = -1
            ##risk_free_rate = 0.0238
            closed_trades = 0
            number_of_bars_in_each_trade = 0
            number_of_bars_in_each_winning_trade = 0
            number_of_bars_in_each_loss_trade = 0
            
            closed_trades_long = 0
            number_of_bars_in_each_trade_long = 0
            number_of_bars_in_each_winning_trade_long = 0
            number_of_bars_in_each_loss_trade_long = 0
            
            closed_trades_short = 0
            number_of_bars_in_each_trade_short = 0
            number_of_bars_in_each_winning_trade_short = 0
            number_of_bars_in_each_losing_trade_short = 0
            
            gross_profit = []
            gross_loss = []
            portfolio_totals = []
            buy_hold_return = []
            excess_returns = []
            percentage_profit_or_loss = []
            negative_assets = []
            max_contracts_held = []
            closed_trades_append = []
            positive_assets = []
            average_trade = []
            average_of_bars_in_each_trade_group = [0]
            average_of_bars_in_winning_trade = []
            average_of_bars_in_losing_trade = []
            
            gross_profit_long = []
            gross_loss_long = []
            max_contracts_held_long = []
            closed_trades_long_append = []
            average_trade_long = []
            average_of_bars_in_each_trade_long_group = [0]
            average_of_bars_in_winning_trade_long = []
            average_of_bars_in_losing_trade_long = []
            
            gross_profit_short = []
            gross_loss_short = []
            max_contracts_held_short = []
            closed_trades_short_append = []
            average_trade_short = []
            average_of_bars_in_each_trade_short_group = [0]
            average_of_bars_in_winning_trade_short = []
            average_of_bars_in_losing_trade_short = []
            
            
            for items_alert, items_source, items_src_append in zip(alert, source, src_append):
                lineCount = lineCount + 1
                
                ##print(lineCount)
                #print(items_alert)
                ##print(items_source)
                #print(items_src_append)
                if(items_alert == "BUY"):
                    ##print(items_src_append)
                    ##print("Enter LONG")
                    place_holder = 0
                    #break
                    ##print('-----------')
                    ##print("Money:", money)
                    ##print("Posistion:", items_alert)
                    open_posistion_price =  items_src_append
                    ##print("open_posistion_price:", open_posistion_price)
                    
                    
                    quantity_shares = (int(money/open_posistion_price))
                    ##print("Shares", quantity_shares)        
    
                    investment_amount = (quantity_shares * open_posistion_price)
                    #print("investment_amount", investment_amount)
                    amount_left = money - investment_amount
                    #print("amount_left", amount_left)
                    
                    
                    
                    
                    
                    #quantity_shares_offset = (money/open_posistion_price) - quantity_shares
                    #print("quantity_shares_offset", quantity_shares_offset)              
                    #remainder_money = quantity_shares_offset*open_posistion_price
                    #print("remainder_money", remainder_money)
                    #money = money+remainder_money
                    #print("Money:", money)
                    
                    max_contracts_held.append(quantity_shares)
                    max_contracts_held_long.append(quantity_shares)
                    ##print('-----------')
                    #break
                    for items_alert, items_source, items_src_append in zip(alert[lineCount:], source[lineCount:], src_append[lineCount:]):
                        number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                        number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                        #print(number_of_bars_in_each_winning_trade)
                        #print(items_src_append)
                        number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                        
                        number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                        number_of_bars_in_each_winning_trade_long = number_of_bars_in_each_winning_trade_long + 1
                        number_of_bars_in_each_loss_trade_long = number_of_bars_in_each_loss_trade_long + 1
                        
                        
                        if(items_alert == "SELL"):
                            ##print(items_src_append)
                            ##print("Exit Long")
                            place_holder = 0
                            ##print('-----------')
                            close_posistion_price = items_src_append
                            ##print("Close Posistion Price:", close_posistion_price)
                            percentage_profit_loss = (close_posistion_price - open_posistion_price)/open_posistion_price
                            ##print("% Profit/Loss:", percentage_profit_loss)
                            percentage_profit_or_loss.append(percentage_profit_loss)
                            ##profit_loss = (close_posistion_price * quantity_shares)
                            profit_loss = (investment_amount * (1+percentage_profit_loss))
                            ##print("Profit/Loss:", profit_loss)
                            investment_revenue = profit_loss - (investment_amount)
                            ##print("Investment Revenue:", investment_revenue)
                            excess_return = percentage_profit_loss - 0.0238
                            excess_returns.append(excess_return)
                            money = profit_loss+amount_left
                            if(investment_revenue > 0):
                                gross_profit.append(investment_revenue)
                            elif(investment_revenue < 0):
                                gross_loss.append(investment_revenue)
                            portfolio_totals.append(profit_loss)
                            ##print('-----------')
                            #buy_hold_return = ((close_posistion_price - open_posistion_price)/open_posistion_price)*100
                            #buy_hold_return.append(buy_hold_return)
                            if(percentage_profit_loss < 0):
                                negative_assets.append((percentage_profit_loss-0.0238)**2)
                                average_of_bars_in_each_trade_group.append(number_of_bars_in_each_trade)
                                average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                
                                average_of_bars_in_each_trade_long_group.append(number_of_bars_in_each_trade_long)
                                average_of_bars_in_losing_trade_long.append(number_of_bars_in_each_loss_trade_long)
                                                         
                            closed_trades_append.append(closed_trades + 1)
                            if(percentage_profit_loss > 0):
                                positive_assets.append(percentage_profit_loss)
                                average_of_bars_in_each_trade_group.append(number_of_bars_in_each_trade)
                                average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                
                                average_of_bars_in_each_trade_long_group.append(number_of_bars_in_each_trade_long)
                                average_of_bars_in_winning_trade_long.append(number_of_bars_in_each_winning_trade_long)
                                
                            average_trade.append(investment_revenue)
                            
                            
                            
                            
                          
                            if(investment_revenue > 0):
                                gross_profit_long.append(investment_revenue)
                            elif(investment_revenue < 0):
                                gross_loss_long.append(investment_revenue)
                            closed_trades_long_append.append(closed_trades_long + 1)
                            average_trade_long.append(investment_revenue)
                            
                            ##money = money + amount_left
                            break
                        else:
                            place_holder = 0
                            number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                            average_of_bars_in_each_trade_long_group.append(number_of_bars_in_each_trade_long) 
            
            
            
            
            
            
                elif(items_alert == "SELL"):
                    ##print(items_src_append)
                    ##print("Enter Short")
                    place_holder = 0
                    #break
                    ##print('-----------')
                    ##print("Money:", money)
                    ##print("Posistion:", items_alert)
                    open_posistion_price =  items_src_append
                    ##print("open_posistion_price:", open_posistion_price)
                    
                    
                    quantity_shares = (int(money/open_posistion_price))
                    ##print("Shares", quantity_shares)        
                    
                    investment_amount = (quantity_shares * open_posistion_price)
                    #print("investment_amount", investment_amount)
                    amount_left = money - investment_amount
                    #print("amount_left", amount_left)
                    
                    
                    
                    
                    
                    #money = money+remainder_money
                    #print("Money:", money)
                    
                    max_contracts_held.append(quantity_shares)
                    max_contracts_held_short.append(quantity_shares)
                    ##print('-----------')
                    #break
                    for items_alert, items_source, items_src_append in zip(alert[lineCount:], source[lineCount:], src_append[lineCount:]):
                        number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                        number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                        #print(number_of_bars_in_each_winning_trade)
                        #print(items_src_append)
                        number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                        
                        number_of_bars_in_each_trade_short = number_of_bars_in_each_trade_short + 1
                        number_of_bars_in_each_winning_trade_short = number_of_bars_in_each_winning_trade_short + 1
                        number_of_bars_in_each_losing_trade_short = number_of_bars_in_each_losing_trade_short + 1
                        if(items_alert == "BUY"):
                            ##print(items_src_append)
                            ##print("Exit Short")
                            place_holder = 0
                            ##print('-----------')
                            close_posistion_price = items_src_append
                            ##print("Close Posistion Price:", close_posistion_price)
                            percentage_profit_loss = (open_posistion_price - close_posistion_price)/open_posistion_price
                            ##print("% Profit/Loss:", percentage_profit_loss)
                            percentage_profit_or_loss.append(percentage_profit_loss)
                            ###profit_loss = (close_posistion_price * quantity_shares)
                            profit_loss = (investment_amount * (1+percentage_profit_loss))
                            ##print("Profit/Loss:", profit_loss)
                            investment_revenue = profit_loss - (investment_amount)
                            ##print("Investment Revenue:", investment_revenue)
                            excess_return = percentage_profit_loss - 0.0238
                            excess_returns.append(excess_return)
                            money = profit_loss+amount_left
                            if(investment_revenue > 0):
                                gross_profit.append(investment_revenue)
                            elif(investment_revenue < 0):
                                gross_loss.append(investment_revenue)
                            portfolio_totals.append(profit_loss)
                            ##print('-----------')
                            #buy_hold_return = ((close_posistion_price - open_posistion_price)/open_posistion_price)*100
                            #buy_hold_return.append(buy_hold_return)
                            if(percentage_profit_loss < 0):
                                negative_assets.append((percentage_profit_loss-0.0238)**2)
                                average_of_bars_in_each_trade_group.append(number_of_bars_in_each_trade)
                                average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                
                                average_of_bars_in_each_trade_short_group.append(number_of_bars_in_each_trade_short)
                                average_of_bars_in_losing_trade_short.append(number_of_bars_in_each_losing_trade_short)
                                
                            closed_trades_append.append(closed_trades + 1)
                            if(percentage_profit_loss > 0):
                                positive_assets.append(percentage_profit_loss)
                                average_of_bars_in_each_trade_group.append(number_of_bars_in_each_trade)
                                average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                
                                average_of_bars_in_each_trade_short_group.append(number_of_bars_in_each_trade_short)
                                average_of_bars_in_winning_trade_short.append(number_of_bars_in_each_winning_trade_short)
                                
                            average_trade.append(investment_revenue)
                            
                            
                            if(investment_revenue > 0):
                                gross_profit_short.append(investment_revenue)
                            elif(investment_revenue < 0):
                                gross_loss_short.append(investment_revenue)
                            closed_trades_short_append.append(closed_trades_short + 1)
                            average_trade_short.append(investment_revenue)
                            
                            
                            
                            ##money = money + amount_left
                            break
                
                    if(money < 0):
                        break
            
                    
                else:
                    #print('-----------')
                    #print(items_src_append)
                    ##print("HOLD")
                    
                    number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                    average_of_bars_in_each_trade_group.append(number_of_bars_in_each_trade)
                    #print(number_of_bars_in_each_trade)
                    ##print('-----------')
                    #print(gross_profit)
                #print(excess_returns)
                #print(r_minus_rf)
                
            
            
            
            
            
            ##print("Calculations for Everything:", '-------------')
            
            #print(money)
            net_profit_all = money-100000
            #print(money)
            ##print("Net Profit:","$", net_profit_all)
            
            #print(gross_profit)
            #print(gross_loss)
            total_gross_profit = sum(gross_profit)
            ##print("Gross Profit:","$", total_gross_profit)
            
            total_gross_loss = sum(gross_loss)
            ##print("Gross Loss:","$", total_gross_loss)
            
            if(len(portfolio_totals) == 0):
                return()
            #print(portfolio_totals)
            length_of_portfolio_totals = len(portfolio_totals)-1
            #print("Length of Portfolio Totals Array:", length_of_portfolio_totals)
            portfolio_max = max(portfolio_totals)
            #print("Portfolio Max:", portfolio_max)
            position_of_portfolio_max = portfolio_totals.index(portfolio_max)
            #print("Position in Array of Portfolio Max:", position_of_portfolio_max)
            if(length_of_portfolio_totals == 0):
                return()
            portfolio_max_deviation = 1-(position_of_portfolio_max/length_of_portfolio_totals)
            #print("Portfolio Max Deviation:", portfolio_max_deviation)               
            if(portfolio_max == 0):
                return()
            #print("Portfolio Max:", portfolio_max)
            portfolio_min = min(portfolio_totals)
            #print("Portfolio Min:", portfolio_min)
            
            
            
            
            
            
            
            
            
            #print(portfolio_totals)
            data_portfolio_totals_df = pd.DataFrame(portfolio_totals)

            df = data_portfolio_totals_df.pct_change().dropna()

            comp_ret = (df+1).cumprod()
            peak = comp_ret.expanding(min_periods=1).max()
            dd = (comp_ret/peak)-1
            #print(dd)
            
            dd_list = dd.to_numpy().tolist()
            #print(dd_list)
        
            portfolio_max_drawdown = min(dd_list)
            #print("Portfolio Max Drawdown:", portfolio_max_drawdown)
            
            
            for items_portfolio_max_drawdown in portfolio_max_drawdown:
                for_loop = 0
            ##print("Portfolio Max Drawdown Percentage:", items_portfolio_max_drawdown)
                
            
            
            
            
            
            
            
            
            
            
            
            #print(buy_hold_return)
            buy_hold_return = sum(buy_hold_return)
            ##print("Buy and Hold Return:", buy_hold_return,"%")
            
            #print(percentage_profit_or_loss)
            average_percentage_profit_loss_all_assets = (sum(percentage_profit_or_loss)/len(percentage_profit_or_loss))
            if(average_percentage_profit_loss_all_assets == 0):
                return()
            #print("Average Percentage Profit or Loss All Assets:", average_percentage_profit_loss_all_assets)
            #print(excess_returns)
            if(excess_returns == 0):
                return()
            if(len(excess_returns) == 0 or len(excess_returns) == 1):
                return()
            stdev_portfolio_excess_return  = (statistics.stdev(excess_returns))
            if(stdev_portfolio_excess_return == 0):
                return()
            #print("Standard Deviation:", stdev_portfolio_excess_return)
            sharpe_ratio = (average_percentage_profit_loss_all_assets)/stdev_portfolio_excess_return
            #if(sharpe_ratio == 0):
                #return()
            ##print("Sharpe Ratio:", sharpe_ratio)
            
            #print(negative_assets)
            r_minus_rf_squared = sum(negative_assets)
            #print(r_minus_rf_squared)
            stdev_negative_asset_return = math.sqrt(r_minus_rf_squared/9)
            ##print("Standard Deviation:", stdev_negative_asset_return)
            if(percentage_profit_or_loss == 0 or len(percentage_profit_or_loss) == 0 or stdev_negative_asset_return == 0):
               return()
            sortino_ratio = ((sum(percentage_profit_or_loss)/len(percentage_profit_or_loss)) - 0.0238)/stdev_negative_asset_return
            ##print("Sortino Ratio:", sortino_ratio)
        
            profit_factor = total_gross_profit/abs(total_gross_loss)
            ##print("profit Factor:", profit_factor)
            
            max_contracts_held = max(max_contracts_held)
            ##print("Max Contracts Held:", int(max_contracts_held))
            
            ##dt = datetime.now()
            # Format datetime string
            ##x = dt.strftime("%Y-%m-%d %H:%M")
            #print(x)
            ##NY = 'America/new_york'
            ##end=pd.Timestamp(x, tz=NY)
            #print(end)
            ##current_price = api.get_bars("MSFT", "1Min", "2022-04-12", "2022-04-13", adjustment='raw').df
            #print(current_price["close"])
            ##length_current_price = len(current_price["close"])
            
            #["close"][length_current_price-1]
            current_price = 0
            
            open_profit_loss = open_posistion_price - current_price
            ##print("Open Profit or Loss:", open_profit_loss)
            
            commission_paid = 0
            ##print("Commission Paid:", commission_paid)
            
            total_closed_trades = len(closed_trades_append)
            ##print("Total Closed Trades:", total_closed_trades)
            
            total_open_trades = 1
            ##print("Total Open Trades:", total_open_trades)
            
            #print(positive_assets)
            number_of_winning_trades = len(positive_assets)
            ##print("Number of Winning Trades:", number_of_winning_trades)
            
            number_of_losing_trades = len(negative_assets)
            ##print("Number of Losing Trades:", number_of_losing_trades)
            
            percent_profitable = number_of_winning_trades/(number_of_losing_trades+number_of_winning_trades)
            ##print("Percent Profitable:", percent_profitable)
            
            #print(average_trade)
            average_trade = sum(average_trade)/len(average_trade)
            ##print("Average Trade:", average_trade)
            
            
            if(sum(gross_profit) == 0):
                return()
            average_winning_trades = sum(gross_profit)/len(gross_profit)
            ##print("Average Winning Trades:", average_winning_trades)
            
            average_losing_trades = sum(gross_loss)/len(gross_loss)
            ##print("Average Losing Trades:", average_losing_trades) 
            
            ratio_avg_win_loss = abs(average_winning_trades/average_losing_trades)
            ##print("Ratio Average Win/Loss:", ratio_avg_win_loss)
            
            largest_winning_trade = max(gross_profit)
            ##print("Largest Winning Trade:", largest_winning_trade)
            
            largest_losing_trade = min(gross_loss)
            ##print("Largest Losing Trade:", largest_losing_trade)
            
            #print(average_of_bars_in_each_trade)
            length_abiet = len(average_of_bars_in_each_trade_group)-1
            #print(length_abiet)
            #print(average_of_bars_in_each_trade[length_abiet])
            #print(len(gross_profit)+len(gross_loss))
            average_of_bars_in_each_trade = int(average_of_bars_in_each_trade_group[length_abiet]/(len(gross_profit)+len(gross_loss)))
            #print("Average # of Bars in Each Trade:", average_of_bars_in_each_trade)
            
            #print(average_of_bars_in_each_trade)
            #print(len(average_of_bars_in_each_trade_group))
            #print(average_of_bars_in_winning_trade)
            #print(average_of_bars_in_losing_trade)
            
            
            
            
            length_of_average_of_bars_in_winning_trade = len(average_of_bars_in_winning_trade)
            #print(length_of_average_of_bars_in_winning_trade)
            i = 0
            #a = 0
            average_of_bars_in_each_trade_append = []
            length_append = []
            for items, stuff in zip(average_of_bars_in_each_trade_group[0:], average_of_bars_in_each_trade_group[1:]):
                #test_append.append(items)
                average_of_bars_in_each_trade_append.append(items)
                if(items == average_of_bars_in_winning_trade[i]):
                    #print(items)
                    length_another = (len(average_of_bars_in_each_trade_append)-1)
                    #print(length_another)
                    length_append.append(length_another)
                    i = i + 1
                    if(i == length_of_average_of_bars_in_winning_trade):
                        break
                    
            number_of_bars_append = [0]
            for items, stuff in zip(average_of_bars_in_each_trade_group[0:], average_of_bars_in_each_trade_group[1:]):
                aa = stuff - items
                number_of_bars_append.append(aa)
                #print(a)
    
            winner_bars_append = []
            for shit in length_append:
                winner_bars = number_of_bars_append[shit]
                #print(winner_bars)
                winner_bars_append.append(winner_bars)
            
            #print(number_of_bars_append)
            #print(length_append)
            #print(winner_bars_append)
            
            average_number_of_winning_bars = int(sum(winner_bars_append)/length_of_average_of_bars_in_winning_trade)
            ##print("Average Number of Winner Bars:", average_number_of_winning_bars)
            
            
            
            
            
            
            length_average_of_bars_in_losing_trade = len(average_of_bars_in_losing_trade)
            i = 0
            #a = 0
            average_of_bars_in_each_trade_append = []
            length_append = []
            for items, stuff in zip(average_of_bars_in_each_trade_group[0:], average_of_bars_in_each_trade_group[1:]):
                #test_append.append(items)
                average_of_bars_in_each_trade_append.append(items)
                if(items == average_of_bars_in_losing_trade[i]):
                    #print(items)
                    length_another = (len(average_of_bars_in_each_trade_append)-1)
                    #print(length_another)
                    length_append.append(length_another)
                    i = i + 1
                    if(i == length_average_of_bars_in_losing_trade):
                        break
                    
            number_of_bars_append = [0]
            for items, stuff in zip(average_of_bars_in_each_trade_group[0:], average_of_bars_in_each_trade_group[1:]):
                aa = stuff - items
                number_of_bars_append.append(aa)
                #print(a)
    
            losing_bars_append = []
            for shit in length_append:
                losing_bars = number_of_bars_append[shit]
                #print(winner_bars)
                losing_bars_append.append(losing_bars)
            
            #print(number_of_bars_append)
            #print(length_append)
            #print(losing_bars_append)
            
            average_number_of_losing_bars = int(sum(losing_bars_append)/length_average_of_bars_in_losing_trade)
            ##print("Average Number of Losing Bars:", average_number_of_losing_bars)
            
            
            
            
            
            
            
            
            margin_calls = 0
            ##print("Margin Calls:", margin_calls)
            
            ##print('------------------------------------')
            
            ##print("Calculations for Long:", '-------------')
            
            
            #print(gross_profit_long)
            #print(gross_loss_long)
            net_profit_long = sum(gross_profit_long)+sum(gross_loss_long)
            ##print("Net Proift Long:", net_profit_long)
            
            gross_profit_long_metric = sum(gross_profit_long)
            #print("Gross Profit Long:", gross_profit_long_metric )
            gross_loss_long_metric = sum(gross_loss_long)
            #print("Gross Loss Long:", gross_loss_long_metric)
            
            if(gross_profit_long_metric == 0 or len(gross_profit_long) == 0 or gross_loss_long_metric == 0 or len(gross_loss_long) == 0):
               return()
            profit_factor_long = gross_profit_long_metric/abs(gross_loss_long_metric)
            ##print("Profit Factor Long:", profit_factor_long)
            
            max_contracts_held_long = max(max_contracts_held_long)
            ##print("Max Contracts Held Long:", int(max_contracts_held_long))
            
            commission_paid_long = 0
            ##print("Commission Paid Long:", commission_paid_long)
            
            total_closed_trades_long = len(closed_trades_long_append)
            ##print("Total Closed Trades Long:", total_closed_trades_long)
            
            total_open_trades_long = 0
            ##print("Total Open Trades Long:", total_open_trades_long)
            
            number_of_winning_trades_long = len(gross_profit_long)
            ##print("Number of Winning Trades Long:", number_of_winning_trades_long)
            
            number_of_losing_trades_long = len(gross_loss_long)
            ##print("Number of Losing Trades Long:", number_of_losing_trades_long)
            
            percent_profitable_long = number_of_winning_trades_long/(number_of_losing_trades_long+number_of_winning_trades_long)
            ##print("Percent Profitable Long:", percent_profitable_long)
            
            #print(average_trade_long)
            average_trade_long = sum(average_trade_long)/len(average_trade_long)
            ##print("Average Trade Long:", average_trade_long)
            
            if(sum(gross_profit_long) == 0):
                return()
            average_winning_trades_long = sum(gross_profit_long)/len(gross_profit_long)
            ##print("Average Winning Trades Long:", average_winning_trades_long)
            
            #print(gross_loss_long)
            average_losing_trades_long = sum(gross_loss_long)/len(gross_loss_long)
            ##print("Average Losing Trades Long:", average_losing_trades_long) 
            
            ratio_avg_win_loss_long = abs(average_winning_trades_long/average_losing_trades_long)
            ##print("Ratio Average Win/Loss Long:", ratio_avg_win_loss_long)
            
            #print(gross_profit_long)
            largest_winning_trade_long = max(gross_profit_long)
            ##print("Largest Winning Trade Long:", largest_winning_trade_long)
            
            largest_losing_trade_long = min(gross_loss_long)
            ##print("Largest Losing Trade Long:", largest_losing_trade_long)
            
            #print(average_of_bars_in_each_trade_long)
            length_abietl = len(average_of_bars_in_each_trade_long_group)-1
            #print(length_abietl)
            #print(average_of_bars_in_each_trade[length_abietl])
            #print(len(gross_profit)+len(gross_loss))
            average_of_bars_in_each_trade_long = int(average_of_bars_in_each_trade_long_group[length_abietl]/(len(gross_profit_long)+len(gross_loss_long)))
            ##print("Average # of Bars in Each Trade Long:", average_of_bars_in_each_trade_long)
            
            
            
            #print(average_of_bars_in_each_trade_long)
            #print(average_of_bars_in_winning_trade_long)
            #print(average_of_bars_in_losing_trade_long)
            
            
            
            #print(average_of_bars_in_winning_trade_long)
            length_of_average_of_bars_in_winning_trade = len(average_of_bars_in_winning_trade_long)
            #print(length_of_average_of_bars_in_winning_trade)
            i = 0
            #a = 0
            average_of_bars_in_each_trade_append = []
            length_append = []
            for items, stuff in zip(average_of_bars_in_each_trade_long_group[0:], average_of_bars_in_each_trade_long_group[1:]):
                #test_append.append(items)
                average_of_bars_in_each_trade_append.append(items)
                if(items == average_of_bars_in_winning_trade_long[i]):
                    #print(items)
                    length_another = (len(average_of_bars_in_each_trade_append)-1)
                    #print(length_another)
                    length_append.append(length_another)
                    i = i + 1
                    if(i == length_of_average_of_bars_in_winning_trade):
                        break
                    
            number_of_bars_append = [0]
            for items, stuff in zip(average_of_bars_in_each_trade_long_group[0:], average_of_bars_in_each_trade_long_group[1:]):
                aa = stuff - items
                number_of_bars_append.append(aa)
                #print(a)
    
            winner_bars_append = []
            for shit in length_append:
                winner_bars = number_of_bars_append[shit]
                #print(winner_bars)
                winner_bars_append.append(winner_bars)
            
            #print(number_of_bars_append)
            #print(length_append)
            #print(winner_bars_append)
            
            average_number_of_winning_bars_long = int(sum(winner_bars_append)/length_of_average_of_bars_in_winning_trade)
            ##print("Average Number of Winner Bars Long:", average_number_of_winning_bars_long)
            
            
            
            #print(number_of_bars_append)
            #print(length_append)
            #print(winner_bars_append)
            
            
            
            
            
            
            #print(average_of_bars_in_losing_trade_long)
            length_average_of_bars_in_losing_trade = len(average_of_bars_in_losing_trade_long)
            #print(length_average_of_bars_in_losing_trade)
            i = 0
            #a = 0
            average_of_bars_in_each_trade_append = []
            length_append = []
            for items, stuff in zip(average_of_bars_in_each_trade_long_group[0:], average_of_bars_in_each_trade_long_group[1:]):
                #test_append.append(items)
                average_of_bars_in_each_trade_append.append(items)
                if(items == average_of_bars_in_losing_trade_long[i]):
                    #print(items)
                    length_another = (len(average_of_bars_in_each_trade_append)-1)
                    #print(length_another)
                    length_append.append(length_another)
                    i = i + 1
                    if(i == length_average_of_bars_in_losing_trade):
                        break
                    
            number_of_bars_append = [0]
            for items, stuff in zip(average_of_bars_in_each_trade_long_group[0:], average_of_bars_in_each_trade_long_group[1:]):
                aa = stuff - items
                number_of_bars_append.append(aa)
                #print(a)
    
            losing_bars_append = []
            for shit in length_append:
                losing_bars = number_of_bars_append[shit]
                #print(winner_bars)
                losing_bars_append.append(losing_bars)
            
            #print(number_of_bars_append)
            #print(length_append)
            #print(losing_bars_append)
            
            average_number_of_losing_bars_long = int(sum(losing_bars_append)/length_average_of_bars_in_losing_trade)
            ##print("Average Number of Losing Bars Long:", average_number_of_losing_bars_long)
            
            
            #print(number_of_bars_append)
            #print(length_append)
            #print(losing_bars_append)
            
            
            margin_calls_longs = 0
            ##print("Margin Calls Long:", margin_calls_longs)
            
            ##print('-------------------------------------')
            
            ##print("Calculations for Short:", '-------------')
            
            
            #print(gross_profit_short)
            #print(gross_loss_short)
            net_profit_short = sum(gross_profit_short)+sum(gross_loss_short)
            ##print("Net Proift Long:", net_profit_short)
            
            gross_profit_short_metric = sum(gross_profit_short)
            ##print("Gross Profit Long:", gross_profit_short)
            gross_loss_short_metric = sum(gross_loss_short)
            ##print("Gross Loss Long:", gross_loss_short)
            
            if(gross_profit_short_metric == 0 or len(gross_profit_short) == 0 or gross_loss_short_metric == 0 or len(gross_loss_short) == 0):
               return()
            profit_factor_short = gross_profit_short_metric/abs(gross_loss_short_metric)
            ##print("Profit Factor Short:", profit_factor_short)
            
            max_contracts_held_short = max(max_contracts_held_short)
            ##print("Max Contracts Held Short:", int(max_contracts_held_short))
            
            commission_paid_short = 0
            ##print("Commission Paid Short:", commission_paid_short)
            
            total_closed_trades_short = len(closed_trades_short_append)
            ##print("Total Closed Trades Long:", total_closed_trades_short)
            
            total_open_trades_short = 0
            ##print("Total Open Trades Short:", total_open_trades_short)
            
            number_of_winning_trades_short = len(gross_profit_short)
            ##print("Number of Winning Trades Short:", number_of_winning_trades_short)
            
            number_of_losing_trades_short = len(gross_loss_short)
            ##print("Number of Losing Trades Short:", number_of_losing_trades_short)
            
            percent_profitable_short = number_of_winning_trades_short/(number_of_losing_trades_short+number_of_winning_trades_short)
            ##print("Percent Profitable Short:", percent_profitable_short)
            
            #print(average_trade_long)
            average_trade_short = sum(average_trade_short)/len(average_trade_short)
            ##print("Average Trade Short:", average_trade_short)
            
            average_winning_trades_short = sum(gross_profit_short)/len(gross_profit_short)
            ##print("Average Winning Trades Short:", average_winning_trades_short)
            
            average_losing_trades_short = sum(gross_loss_short)/len(gross_loss_short)
            ##print("Average Losing Trades Short:", average_losing_trades_short) 
            
            ratio_avg_win_loss_short = abs(average_winning_trades_short/average_losing_trades_short)
            ##print("Ratio Average Win/Loss Short:", ratio_avg_win_loss_short)
            
            #print(gross_profit_long)
            largest_winning_trade_short = max(gross_profit_short)
            ##print("Largest Winning Trade Short:", largest_winning_trade_short)
            
            largest_losing_trade_short = min(gross_loss_short)
            ##print("Largest Losing Trade Short:", largest_losing_trade_short)
            
            #print(average_of_bars_in_each_trade_long)
            length_abiets = len(average_of_bars_in_each_trade_short_group)-1
            #print(length_abietl)
            #print(average_of_bars_in_each_trade[length_abietl])
            #print(len(gross_profit)+len(gross_loss))
            average_of_bars_in_each_trade_short = int(average_of_bars_in_each_trade_short_group[length_abiets]/(len(gross_profit_short)+len(gross_loss_short)))
            ##print("Average # of Bars in Each Trade Short:", average_of_bars_in_each_trade_short)
            
            
            
            
            
            
            
            #print(average_of_bars_in_each_trade_short)
            #print(average_of_bars_in_winning_trade_short)
            #print(average_of_bars_in_losing_trade_short)
            
            
            
            #print(average_of_bars_in_winning_trade_long)
            length_of_average_of_bars_in_winning_trade = len(average_of_bars_in_winning_trade_short)
            #print(length_of_average_of_bars_in_winning_trade)
            i = 0
            #a = 0
            average_of_bars_in_each_trade_append = []
            length_append = []
            for items, stuff in zip(average_of_bars_in_each_trade_short_group[0:], average_of_bars_in_each_trade_short_group[1:]):
                #test_append.append(items)
                average_of_bars_in_each_trade_append.append(items)
                if(items == average_of_bars_in_winning_trade_short[i]):
                    #print(items)
                    length_another = (len(average_of_bars_in_each_trade_append)-1)
                    #print(length_another)
                    length_append.append(length_another)
                    i = i + 1
                    if(i == length_of_average_of_bars_in_winning_trade):
                        break
                    
            number_of_bars_append = [0]
            for items, stuff in zip(average_of_bars_in_each_trade_short_group[0:], average_of_bars_in_each_trade_short_group[1:]):
                aa = stuff - items
                number_of_bars_append.append(aa)
                #print(a)
    
            winner_bars_append = []
            for shit in length_append:
                winner_bars = number_of_bars_append[shit]
                #print(winner_bars)
                winner_bars_append.append(winner_bars)
            
            #print(number_of_bars_append)
            #print(length_append)
            #print(winner_bars_append)
            
            average_number_of_winning_bars_short = int(sum(winner_bars_append)/length_of_average_of_bars_in_winning_trade)
            ##print("Average Number of Winner Bars Short:", average_number_of_winning_bars_short)
            
            
            
            
            
            
            
            #print(average_of_bars_in_losing_trade_long)
            length_average_of_bars_in_losing_trade = len(average_of_bars_in_losing_trade_short)
            #print(length_average_of_bars_in_losing_trade)
            i = 0
            #a = 0
            average_of_bars_in_each_trade_append = []
            length_append = []
            for items, stuff in zip(average_of_bars_in_each_trade_short_group[0:], average_of_bars_in_each_trade_short_group[1:]):
                #test_append.append(items)
                average_of_bars_in_each_trade_append.append(items)
                if(items == average_of_bars_in_losing_trade_short[i]):
                    #print(items)
                    length_another = (len(average_of_bars_in_each_trade_append)-1)
                    #print(length_another)
                    length_append.append(length_another)
                    i = i + 1
                    if(i == length_average_of_bars_in_losing_trade):
                        break
                    
            number_of_bars_append = [0]
            for items, stuff in zip(average_of_bars_in_each_trade_short_group[0:], average_of_bars_in_each_trade_short_group[1:]):
                aa = stuff - items
                number_of_bars_append.append(aa)
                #print(a)
    
            losing_bars_append = []
            for shit in length_append:
                losing_bars = number_of_bars_append[shit]
                #print(winner_bars)
                losing_bars_append.append(losing_bars)
            
            #print(number_of_bars_append)
            #print(length_append)
            #print(losing_bars_append)
            
            average_number_of_losing_bars_short = int(sum(losing_bars_append)/length_average_of_bars_in_losing_trade)
            ##print("Average Number of Losing Bars Short:", average_number_of_losing_bars_short)
            
            
            #print(total_gross_profit)
            
            trend_percentage = 1-(money/portfolio_max)
            #print("Trend Percentage:", trend_percentage)
            
            
            #print("Max Drawdown Percentage:", items_portfolio_max_drawdown)
            net_profit_percentage = net_profit_all/starting_money
            
            if(net_profit_percentage == 0):
                return()
            
            #print("Net Profit All Percentage:", net_profit_percentage)
            maxdrawdown_netprofit_ratio = abs(items_portfolio_max_drawdown/net_profit_percentage)
            #print("Maxdrawndown/NetProfit Ratio:", maxdrawdown_netprofit_ratio)                       
            
            
            
            ##print(starting_money)
            
            if(net_profit_all > starting_money*0.25):
                pmax_score_net_profit = 1
                ##print(net_profit_all)
            else:
                pmax_score_net_profit = 0
                ##print(net_profit_all)
                
            if(total_closed_trades > 100 and total_closed_trades < 200):
                pmax_score_closed_trades = 1
                ##print(total_closed_trades)
            else:
                pmax_score_closed_trades = 0
                ##print(total_closed_trades)
                
            if(trend_percentage < 0.015):
                pmax_score_trend_percentage = 1
                ##print(trend_percentage)
            else:
                pmax_score_trend_percentage = 0
                ##print(trend_percentage)
                
            if(portfolio_max_deviation < 0.10):
                pmax_score_portfolio_max_deviation = 1
                ##print(pmax_score_portfolio_max_deviation)
            else:
                pmax_score_portfolio_max_deviation = 0
                ##print(pmax_score_portfolio_max_deviation)
                
            if(items_portfolio_max_drawdown > -0.20):
                pmax_score_portfolio_max_drawdown = 1
                ##print(pmax_score_portfolio_max_drawdown)
            else:
                pmax_score_portfolio_max_drawdown = 0
                ##print(pmax_score_portfolio_max_drawdown)
            
            if(maxdrawdown_netprofit_ratio < 0.20):
                pmax_score_portfolio_maxdrawdown_netprofit_ratio = 1
                ##print(pmax_score_portfolio_max_drawdown)
            else:
                pmax_score_portfolio_maxdrawdown_netprofit_ratio = 0
                ##print(pmax_score_portfolio_max_drawdown)
                
            
            
                
            total_pmax_score = pmax_score_net_profit+pmax_score_closed_trades+pmax_score_trend_percentage+pmax_score_portfolio_max_deviation+pmax_score_portfolio_max_drawdown+pmax_score_portfolio_maxdrawdown_netprofit_ratio
            #print("PMax Score:", total_pmax_score)
            
            
            
            
            
            if(total_pmax_score == 6):
                letter_grade = 'AAA'
            elif(total_pmax_score == 5):
                letter_grade = 'AA'
            elif(total_pmax_score == 4):
                letter_grade = 'A'
            elif(total_pmax_score == 3):
                letter_grade = 'B'
            elif(total_pmax_score == 2):
                letter_grade = 'C'
            elif(total_pmax_score == 1):
                letter_grade = 'D'
            elif(total_pmax_score == 0):
                letter_grade = 'F'
    
            #print("Letter Grade:", letter_grade)
            
            
            
            DATA_SOURCE = 'TRADINGVIEW'
            PMAX_csv = 'Pmax_Algo_Data_collection_38_'+ticker+'_'+DATA_SOURCE+'.csv'
            with open(PMAX_csv, 'a', newline='') as csvfile:
                my_writer = csv.writer(csvfile)
                ##my_writer.writerow(("Ticker","PMax_Letter_Grade","ATR Multiplier","Tillson T3 Length","T3a1 Tillson Volume","ATR Length","RSI Length","Net Profit All","Total Gross Profit","Total Gross Loss","Portfolio Max","Portfolio Max Deviation","Portfolio Max Drawdown Percentage","Buy and Hold Return","Sharpe Ratio","Standard Deviation","Sortino Ratio","Profit Factor","Max Contracts Held","Open Profit Loss","Commission Paid","Total Closed Trades","Total Open Trades","Number of Winning Trades","Number of Losing Trades","Percent Profitable","Average Trade","Average Winning Trades","Average Losing Trades","Ratio Average Win/Loss","Largest Winning Trade","Largest Losing Trade","Average of Bars in Each Trade","Average Number of Winning Bars","Average Number of Losing Bars","Margin Calls","Net Profit Long","Gross Profit Long","Gross Loss Long","Profit Factor Long","Max Contracts Held Long","Commission Paiad Long","Total Closed Trades Long","Total Open Trades Long","Number of Winning Trades Long","Number of Losing Trades Long","Percent Profitable Long","Average Trade Long","Average Winning Trades Long","Average Losing Trades Long","Ratio Average Win/Loss Long","Largest Winning Trade Long","Largest Losing Trade Long","Average Number of Bars In Each Trade Long","Average Number of Winning Bars Long","Average Number of Losing Bars Long","Net Profit Short","Gross Profit Short","Gross Loss Short","Profit Factor Short","Max Contracts Held Short","Commission Paiad Short","Total Closed Trades Short","Total Open Trades Short","Number of Winning Trades Short","Number of Losing Trades Short","Percent Profitable Short","Average Trade Short","Average Winning Trades Short","Average Losing Trades Short","Ratio Average Win/Loss Short","Largest Winning Trade Short","Largest Losing Trade Short","Average Number of Bars In Each Trade Short","Average Number of Winning Bars Short","Average Number of Losing Bars Short","Trend Percentage","Net Profit Percetnage","MaxDrawdown/NetProfit Ratio"))
                my_writer.writerow([ticker,letter_grade,Multiplier_ATR,Length_Tillson,T3a1_Tillson_Volume,Period_ATR,rsi_length,net_profit_all,total_gross_profit,total_gross_loss,portfolio_max,portfolio_max_deviation,items_portfolio_max_drawdown,buy_hold_return,sharpe_ratio,stdev_negative_asset_return,sortino_ratio,profit_factor,max_contracts_held,open_profit_loss,commission_paid,total_closed_trades,total_open_trades,number_of_winning_trades,number_of_losing_trades,percent_profitable,average_trade,average_winning_trades,average_losing_trades,ratio_avg_win_loss,largest_winning_trade,largest_losing_trade,average_of_bars_in_each_trade,average_number_of_winning_bars,average_number_of_losing_bars,margin_calls,net_profit_long,gross_profit_long_metric,gross_loss_long_metric,profit_factor_long,max_contracts_held_long,commission_paid_long,total_closed_trades_long,total_open_trades_long,number_of_winning_trades_long,number_of_losing_trades_long,percent_profitable_long,average_trade_long,average_winning_trades_long,average_losing_trades_long,ratio_avg_win_loss_long,largest_winning_trade_long,largest_losing_trade_long,average_of_bars_in_each_trade_long,average_number_of_winning_bars_long,average_number_of_losing_bars_long,net_profit_short,gross_profit_short_metric,gross_loss_short_metric,profit_factor_short,max_contracts_held_short,commission_paid_short,total_closed_trades_short,total_open_trades_short,number_of_winning_trades_short,number_of_losing_trades_short,percent_profitable_short,average_trade_short,average_winning_trades_short,average_losing_trades_short,ratio_avg_win_loss_short,largest_winning_trade_short,largest_losing_trade_short,average_of_bars_in_each_trade_short,average_number_of_winning_bars_short,average_number_of_losing_bars_short,trend_percentage,net_profit_percentage,maxdrawdown_netprofit_ratio])
            
            
            
            
            #print("without GPU:", timer()-start)   
            
            #return(src_open, alert_array, ticker, Multiplier_ATR, Length_Tillson, T3a1_Tillson_Volume, Period_ATR, rsi_length)
        algorithm_body()      
    e = datetime.datetime.now()
    current = ("%s:%s" % (e.hour, e.minute))
    target_time = '6:30'
    ####print("Current Time:", current)
    ####print(current.lower() == target_time.lower())
    weekday = e.strftime('%A')
    #print('Day Of The Week Is:', weekday)
    if(weekday != 'Saturday' and weekday != 'Sunday'):
        if(current.lower() == target_time.lower()):
            #print("ALGORITHM TRAINING PROCCESS COMPLETE")
            break
    

              
            
       


              
                
           
      
    
            
            
                    
                           
                      
            
            
            
            
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    