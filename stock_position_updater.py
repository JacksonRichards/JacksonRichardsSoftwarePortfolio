

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import warnings
import pandas as pd
import urllib.request
import time
import numpy as np

warnings.filterwarnings('ignore')

alpaca_keys = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])




def stock_position_updater():
    
    print("STOCK POSTION UPDATER COMMENCING")
    
    while True:
    
        try:
            
            urllib.request.urlopen('http://google.com') #Python 3.x
            #print("Internet Connection Detected - Stock Position Updater")
            #time.sleep(1)
    
            ticker_exchange_csv_data = pd.read_csv('ticker_parameter_grades.csv')
            #print(ticker_exchange_csv_data)
            
            todays_tickers = ticker_exchange_csv_data['Ticker'].to_numpy().tolist()
            
            
            cp = []
            current_positions = trading_client.get_all_positions()
            for tickers in current_positions:
                open_positions = tickers.symbol
                cp.append(open_positions)
            
            #print("Chosen Tickers:", todays_tickers)
            #print("Current Open Positions:", cp)
            
            #print(type(todays_tickers))
            #print(type(cp))
            
            
            #print(np.intersect1d(todays_tickers, cp))
            #non_intersecting_tickers = np.setxor1d(todays_tickers, cp)
            #print(non_intersecting_tickers)
            '''
            for stuff in todays_tickers:
                one = 1
                #print(stuff)
                #print('-----------')
                for objects in cp:
                    two = 2
                    #print(objects)
                    if(stuff == objects):
                       #print(stuff,objects)
                       old_ticker_list = [x for x in cp if x!=objects]
                       #print('-----------')
            '''
            old_ticker_list = set(cp) - set(todays_tickers)
            old_ticker_list_array = np.array(list(old_ticker_list))
            ####print(old_ticker_list_array)
            
            #print('-------------------------------')
            
            
            for old_ticker_list_items in old_ticker_list:
                ####print("Ticker:", old_ticker_list_items)
                quantity = abs(int(old_ticker_list_items.qty))
                ####print("Quantity:", quantity)
                side = old_ticker_list_items.side
                ####print("Current Side:", side)
                if(side == 'short'):
                    #liquidated_ticker = api.submit_order(symbol=old_ticker_list_items, qty=quantity, side='buy', type='market', time_in_force='day')
                    
                    market_order_data = MarketOrderRequest(
                                        symbol=old_ticker_list_items,
                                        qty=quantity,
                                        side=OrderSide.BUY,
                                        time_in_force=TimeInForce.DAY
                                        )
                    market_order = trading_client.submit_order(
                                    order_data=market_order_data
                                   )
                elif(side == 'long'):
                    #liquidated_ticker = api.submit_order(symbol=old_ticker_list_items, qty=quantity, side='sell', type='market', time_in_force='day')
                    
                    market_order_data = MarketOrderRequest(
                                        symbol=old_ticker_list_items,
                                        qty=quantity,
                                        side=OrderSide.SELL,
                                        time_in_force=TimeInForce.DAY
                                        )
                    market_order = trading_client.submit_order(
                                    order_data=market_order_data
                                   )
                ####print('-------------------------------')   
                
            break
                
            print("STOCK POSITION UPDATER COMPLETE")     
            
        except:
            print("No Internet Connection, Attempting Reconnection... - Stock Position Updater")
            time.sleep(0.5)
    
stock_position_updater()   



























