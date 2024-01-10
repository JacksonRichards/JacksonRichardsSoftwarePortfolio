

import yfinance as yf
import pandas as pd
from datetime import date
import urllib.request
import time

def nasdaq_data():

    print("NASDAQ DATA DOWNLOADER COMMENCING")
    
    while True:
    
        try:
            
            urllib.request.urlopen('http://google.com') #Python 3.x
            #print("Internet Connection Detected - Stock Trading Bot")
            #time.sleep(1)
            break
        
        except:
            
            print("No Internet Connection, Attempting Reconnection... - Stock Trading Bot")
            time.sleep(0.5)
    
    
    while True:
        
        today_initial_data = date.today()
        current_date = today_initial_data
        #print(current_date)
        #print(type(current_date))
        
        
        
    
        data = yf.download(tickers = '^IXIC', period = '6mo', interval = '1d')
        data = data.reset_index()
        pd.set_option('display.max_rows', 10)
        #print(data)
        
        
        open_day_price = data['Date'][len(data['Date'])-1]
        open_day_price.to_pydatetime()
        #print(open_day_price)
        #print(type(open_day_price))

        
        #print(str(current_date)[0:11])  
        #print(str(open_day_price)[0:11])
        
        

        #print(str(current_date)[0:11].strip() == str(open_day_price)[0:11].strip())
    
        if(str(open_day_price)[0:11].strip() == str(current_date)[0:11].strip()):
            #data = yf.download(tickers = '^VIX', period = '6mo', interval = '1d')
            #pd.set_option('display.max_rows', 5000)
            data.to_csv('nasdaq_amounts.csv')
            print("NASDAQ DATA DOWNLOADER COMPLETE")

            break
        
        else:
            #break
            print('NASDAQ NOT YET AVAILABLE')
            time.sleep(1)
                
    
nasdaq_data()








































