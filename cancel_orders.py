# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 01:19:18 2023

@author: jacks
"""




from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import pandas as pd



def cancel_orders():

    alpaca_keys = pd.read_csv("alpaca_api_information_trading.csv")
    
    #paper_tf = pd.read_csv('paper_true_false.csv')
    
    # keys required for stock historical data client
    data_client = StockHistoricalDataClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0])
    trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])
    
    
    close_pos = trading_client.close_all_positions(cancel_orders=True)
    
    all_positions_liquidated = pd.DataFrame([1])
    all_positions_liquidated.to_csv('liquidated_at_SOD.csv')

cancel_orders()
