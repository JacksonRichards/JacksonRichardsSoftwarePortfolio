
import pandas as pd
import csv
import numpy as np
import urllib.request
import time
from alpaca.trading.client import TradingClient


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
            
            print("ASSET LIQUIDATION COMPLETE")
        
        liquidation()
        
        break
    
    except:
        print("No Internet Connection, Attempting Reconnection...")
        time.sleep(0.5)










