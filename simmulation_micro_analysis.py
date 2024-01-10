

import pandas as pd
import numpy as np
import math
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce




alpaca_keys = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

# keys required for stock historical data client
data_client = StockHistoricalDataClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0])
trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])




def portfolio_simmulation_micro_view():
    
    
    print("PORTFOLIO SIMMULATION MICRO VIEW COMMENCING")
    
    
    account = trading_client.get_account()
    last_equity = float(account.last_equity)
    #print("Last Equity:", last_equity)
    
    
    
    detailed_transactions = pd.read_csv("one_day_2_percentage_movements.csv")
    detailed_transactions.sort_values(by=['Position Time'], inplace=True, ascending=True)
    #print(detailed_transactions)
    pd.set_option('display.max_columns', 10000)
    #print(detailed_transactions)
    
    dollar_result = detailed_transactions['Dollar'].to_numpy().tolist()
    position_time = detailed_transactions['Position Time'].to_numpy().tolist()
    #print(dollar_result)
    
    portfolio_total = last_equity
    #print(portfolio_total)
    portfolio_total_initial = portfolio_total
    #print('------')
    
    portfolio_total_append = []
    position_time_append = []
    #porftolio_percentage_append = []
    for items_dollar_result, items_position_time in zip(dollar_result, position_time):
        portfolio_total = items_dollar_result+portfolio_total
        #print(portfolio_total)
        portfolio_total_append.append(portfolio_total)
        position_time_append.append(items_position_time)
        
        #portfolio_percentage = (items_dollar_result/last_equity)
        #porftolio_percentage_append.append(portfolio_percentage)
    
    #print(portfolio_total_append)
    
    portfolio_total_date_df = pd.DataFrame(position_time_append)
    portfolio_total_date_df.columns = ['Transaction Time']
    
    portfolio_total_df = pd.DataFrame(portfolio_total_append)
    portfolio_total_df.columns = ['Portfolio History']
    #print(portfolio_total_df)
    
    

    
    final = pd.concat([portfolio_total_date_df,portfolio_total_df], axis = 1)
    #print(final)
    
    
    final_portfolio = (final['Portfolio History'].to_numpy().tolist())
    final_portfolio_percentage_append = []
    for items_final_portfolio in final_portfolio:
        #print(portfolio_total_initial)
        testing = (items_final_portfolio-portfolio_total_initial)/portfolio_total_initial
        #print(testing)
        final_portfolio_percentage_append.append(testing)
        #print('------')
    
    
    #print(final_portfolio_percentage_append)
    final_portfolio_percentage_df = pd.DataFrame(final_portfolio_percentage_append)
    final_portfolio_percentage_df.columns = ['Percentage History']
    
    #print(final_portfolio_percentage_df)
    
    all_concat = pd.concat([final,final_portfolio_percentage_df], axis=1)
    #print(all_concat)
    
    all_concat.to_csv('portfolio_view_micro_view.csv')
    
    #portfolio_percentage_df = pd.DataFrame(porftolio_percentage_append)
    #portfolio_percentage_df.columns = ['Portfolio Percentage']
    
    
    print("PORTFOLIO SIMMULATION MICRO VIEW COMPLETE")


portfolio_simmulation_micro_view()



































