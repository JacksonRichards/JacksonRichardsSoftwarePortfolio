


import alpaca_trade_api as alpaca
import pandas as pd
import time
import urllib.request

api_keys_csv = pd.read_csv('alpaca_api_information.csv')
API_KEY = api_keys_csv['API KEY'][0]
API_SECRET = api_keys_csv['API SECRET KEY'][0]



def shortable_stocks():
    
    while True:
    
        try:
            
            urllib.request.urlopen('http://google.com') #Python 3.x
            #print("Internet Connection Detected - Shortable Stock List")
            #time.sleep(1)
        
            print("SHORTABLE STOCK LSIT DOWNLOAD COMMENCING")
            
            api = alpaca.REST(API_KEY, API_SECRET, 'https://api.alpaca.markets')
            active_assets = api.list_assets(status='active')
            short_list = []
            for asset in active_assets:
                if asset.easy_to_borrow and asset.marginable:
                    short_list.append(asset.symbol)
            
            
            shortable_stocks_df = pd.DataFrame(short_list)
            shortable_stocks_df.columns = ["Ticker"]
            shortable_stocks_df.to_csv("shortable_stocks.csv")
            print("SHORTABLE STOCK LSIT DOWNLOAD COMPLETE")  
            
            break
            
        except:
            print("No Internet Connection, Attempting Reconnection... - Shortable Stock List")
            time.sleep(0.5)
        
shortable_stocks()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        