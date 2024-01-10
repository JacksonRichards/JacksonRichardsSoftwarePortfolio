


import webbrowser
import time
import keyboard
import pyautogui
import urllib.request
import pandas as pd
import os
import shutil

def csv_auto_download():

    print("CSV DATA DOWNLOAD COMMENCING")
    
    master_list = pd.read_csv('ticker_list_today.csv')
    
    
    exchange = master_list['Exchange'].to_numpy().tolist()
    ticker = master_list['Tickers'].to_numpy().tolist()
    
    for download_exchange, ticker in zip(exchange, ticker):
        
        original = r'C:\Users\jacks\Desktop\New folder\\'+download_exchange+'_'+ticker+', 1.csv'
        #print(original)
        target = r'C:\Users\jacks\Desktop\New folder\tradingview_'+ticker+'_data.csv'
        #print(target)
        shutil.move(original, target)
        #print(ticker, "CSV data scraped")

    
    print("CSV DATA DOWNLOAD COMPLETE")
        
        
                
                
            
            
            
            
        
      
    
    
csv_auto_download()






















