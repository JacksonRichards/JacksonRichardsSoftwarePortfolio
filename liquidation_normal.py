

import pandas as pd
import csv
import numpy as np
import urllib.request
import time
from alpaca.trading.client import TradingClient
from datetime import date


alpaca_keys = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])




print("ASSET LIQUIDATION COMMENCING")

while True:


    try:
        
        urllib.request.urlopen('http://google.com') #Python 3.x
        #print("Internet Connection Detected")
        #time.sleep(1)
    
        def liquidation():
        
            close_pos = trading_client.close_all_positions(cancel_orders=True)
            
            e = date.today()
            current = e.strftime('%H: %M: %S')
            
            exit_market_time = pd.DataFrame([current])
            exit_market_time.columns = ['Market Exit Time']
            exit_market_time.to_csv('market_exit_time.csv')
            
            print("ASSET LIQUIDATION COMPLETE")
        
        liquidation()
        
        break
    
    except:
        print("No Internet Connection, Attempting Reconnection...")
        time.sleep(0.5)










