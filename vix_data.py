
import yfinance as yf
import pandas as pd
import urllib.request
import time
import os

def vix_data():
    
    print("VIX DATA DOWNLOAD COMMENCING")
    
    try:
        
        while True:
       
            data = yf.download(tickers = '^VIX', period = '6mo', interval = '1d')
            pd.set_option('display.max_rows', 5000)
            #print(data)
            
            #print(data['Close'][len(data['Close'])-1])
            
            
            data.to_csv('vix_amounts.csv')
            
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\\vix_amounts.csv') == True):
            
                print("VIX DATA DOWNLOAD COMPLETE")
                break
            
            else:
                
                print("DATA NOT YET AVAILABLE")
                
            time.sleep(0.5)
        
        
    except:
        print("No Internet Connection, Attempting Reconnection... - Stock Trading Bot")
        time.sleep(0.5)
    
vix_data()