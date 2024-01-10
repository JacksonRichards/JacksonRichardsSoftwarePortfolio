

import warnings
import urllib.request
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
import time
import pandas as pd
import datetime


warnings.filterwarnings('ignore')


print("ALL TERMINALS LIQUIDATION COMMENCING")


account_numbers = [1,2,3,4,5,6]
trading_mode = [False,False,False,False,False,False]
all_accounts_array = []
for item_account_numbers, item_trading_mode in zip(account_numbers,trading_mode):
    
    ##print("Account Number:", item_account_numbers)    

    api_keys_csv = pd.read_csv('alpaca_api_information_terminal_'+str(item_account_numbers)+'.csv')
    
    trading_client = TradingClient(api_keys_csv['API KEY'][0], api_keys_csv['API SECRET KEY'][0], paper=item_trading_mode)
    
    account = trading_client.get_account()
    
    close_pos = trading_client.close_all_positions(cancel_orders=True)

print("ALL TERMINALS LIQUIDATED")

print('--------------------------')

    
    
    

    
    





