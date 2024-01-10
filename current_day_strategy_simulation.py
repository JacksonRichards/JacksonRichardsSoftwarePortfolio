
import numpy as np
import pandas as pd
import talib as ta
import math
import csv
from array import *
import time
import matplotlib.pyplot as mp
from numpy import inf
import numpy as np
from timeit import default_timer as timer
import decimal
import random
import statistics
import matplotlib.pyplot as plt
import warnings
from datetime import date
from datetime import timedelta
from datetime import date
import urllib.request
from alpaca.trading.client import TradingClient
import os


alpaca_keys = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])


print("CURRENT DAY SIMMUALTOR COMMENCING")
      
while True:
    
    try:              
                          
        today = date.today()
        ##print("Today is: ", today)           
        # Yesterday date
        curr_date = date.today()
        today_initial_data = date.today()
        y = today_initial_data.strftime("%Y-%m-%d")
        #y =  dt.strftime("%m-%d %H:%M")
        ##print(x)
        ##print(y)
        NY = 'America/los_angeles'
        end=pd.Timestamp(y, tz=NY)
        ##print(end)       
        time_string_initial_data = y
        ##print("Current Day:", time_string_initial_data)
        
        startTime = time.time()
        
        account = trading_client.get_account()
        
        last_equity = float(account.last_equity)
        
        
        def backtest_two():
            
            #current_date = '2022-08-18 06:30:00-07:00'
            ##print("Chosen Date:", current_date)
            
            
            csv_ticker_list = pd.read_csv('ticker_parameter_grades.csv')
            ticker_list = csv_ticker_list['Ticker'].to_numpy().tolist()
            
            ##print(ticker_list)
            
            
            
            starting_money = last_equity
            ##print(starting_money)
            
            action_object = [2,2,2,2]
            #action_object = [1,1,1,1,1,1,1,1,1,1]
            #action_object = [0,0,0,0,0,0,0,0,0,0]
            
            
            percentage_gain_append = []
            percentage_gain_tickers = []
            deviation_results = []
            pos_object = []
            pos_time = []
            investment_revenue_append = []
            portfolio_total_append = []
            for ticker, items_action_object in zip(ticker_list, action_object):
                
                money = starting_money
                
                
                
                src_open = pd.read_csv('PMAX_'+ticker+'_alert_source_tradingview_data.csv')
                #src_open.iloc[200:]
                ##print(src_open)
                
                
                
                
                #shit = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 06:30:00-07:00")]
                ##print(shit.index[0])
                
                #dumb = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 07:00:00-07:00")]
                ##print(dumb.index[0])
                
                ##print('---------------------')
                ##print(src_open['Timestamp'][shit.index[0]:dumb.index[0]])
                
                ##print(ticker)
                array1 = []
                for stuff in src_open['Timestamp']:
                    if(stuff[0:10] == time_string_initial_data):
                        array1.append(stuff)
                        ##print(stuff)
                
                ##print(array1[0])
                
                index = src_open[src_open['Timestamp'] == array1[0]].index[0]
                ##print("Index Number for starting point:", index)
            
                end_index = src_open[src_open['Timestamp'] == array1[len(array1)-1]].index[0]
                ##print("End Index Number for starting point:", end_index)
                
                ##print(len(array1)-1)
                ##print(array1[len(array1)-1])
                
                ##index = 0
                
                ##print(src_open[index:])
                
            
                
                closed_trades = 0
                number_of_bars_in_each_trade = 0
                number_of_bars_in_each_winning_trade = 0
                number_of_bars_in_each_loss_trade = 0
                
                closed_trades_long = 0
                number_of_bars_in_each_trade_long = 0
                number_of_bars_in_each_winning_trade_long = 0
                number_of_bars_in_each_loss_trade_long = 0
                
                closed_trades_short = 0
                number_of_bars_in_each_trade_short = 0
                number_of_bars_in_each_winning_trade_short = 0
                number_of_bars_in_each_losing_trade_short = 0
                
                gross_profit = []
                gross_loss = []
                portfolio_totals = []
                buy_hold_return_append = []
                excess_returns = []
                percentage_profit_or_loss = []
                negative_assets = []
                max_contracts_held = []
                #closed_trades = []
                positive_assets = []
                average_trade = []
                average_of_bars_in_each_trade = [0]
                average_of_bars_in_winning_trade = []
                average_of_bars_in_losing_trade = []
                
                gross_profit_long = []
                gross_loss_long = []
                max_contracts_held_long = []
                #closed_trades_long = []
                average_trade_long = []
                average_of_bars_in_each_trade_long = [0]
                average_of_bars_in_winning_trade_long = []
                average_of_bars_in_losing_trade_long = []
                
                gross_profit_short = []
                gross_loss_short = []
                max_contracts_held_short = []
                #closed_trades_short = []
                average_trade_short = []
                average_of_bars_in_each_trade_short = [0]
                average_of_bars_in_winning_trade_short = []
                average_of_bars_in_losing_trade_short = []
                
                
                
                
                src_open['Trade_Alerts'][index:].to_numpy().tolist
                all_lag = np.array(src_open['Trade_Alerts'][index:])
                sell_lag_index = np.where(all_lag == 'SELL')[0]
                buy_lag_index = np.where(all_lag == 'BUY')[0]
             
                length_sell_lag = len(sell_lag_index)-1                                        
                ##print(length_sell_lag)
                length_buy_lag = len(buy_lag_index)-1  
                
                    
                if(items_action_object == 2):
                    ##print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    ##print('Ticker:', ticker)
                    
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        ##print(items_source_data)
                        ##print(items_trade_alerts)
                        
                        
                        if(items_trade_alerts == 'BUY'):
                            ##print('BUY Indicated')
                            ###print(items_source_data)
                            ###print("Enter LONG")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            ##print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            ##print("Shares", quantity_shares)        
            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #quantity_shares_offset = (money/open_posistion_price) - quantity_shares
                            ##print("quantity_shares_offset", quantity_shares_offset)              
                            #remainder_money = quantity_shares_offset*open_posistion_price
                            ##print("remainder_money", remainder_money)
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_long.append(quantity_shares)
                            ###print('-----------')
                            #break
                            
                            for items_source_data, items_trade_alerts, items_timestamps in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                number_of_bars_in_each_winning_trade_long = number_of_bars_in_each_winning_trade_long + 1
                                number_of_bars_in_each_loss_trade_long = number_of_bars_in_each_loss_trade_long + 1
                                
                                if(items_trade_alerts == "SELL" or items_timestamps == array1[len(array1)-1]):
                                    ###print('SELL Indicated')
                                    ###print(items_source_data)
                                    ###print("Exit Long")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (close_posistion_price - open_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ##profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print(portfolio_totals)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    ##print(buy_hold_return)
                                    #buy_hold_return_append.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_losing_trade_long.append(number_of_bars_in_each_loss_trade_long)
                                    
                                    closed_trades = closed_trades + 1
                                    ##print(closed_trades)
                                    
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_winning_trade_long.append(number_of_bars_in_each_winning_trade_long)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                  
                                    if(investment_revenue > 0):
                                        gross_profit_long.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_long.append(investment_revenue)
                                    
                                    average_trade_long.append(investment_revenue)
                                    
                                    closed_trades_long = closed_trades_long + 1
                                    ##print(closed_trades_long)
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
        
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(1)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    #print('-----------')
                                    break
                                else:
                                    place_holder = 0
                                    number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)   
                       
                        
                        elif(items_trade_alerts == "SELL"):
                            ###print(items_source_data)
                            #print("SELL Indicated")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
                            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_short.append(quantity_shares)
                            ###print('-----------')
                            #break
                            for items_trade_alerts, items_source_data, items_timestamps in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_short = number_of_bars_in_each_trade_short + 1
                                number_of_bars_in_each_winning_trade_short = number_of_bars_in_each_winning_trade_short + 1
                                number_of_bars_in_each_losing_trade_short = number_of_bars_in_each_losing_trade_short + 1
                                if(items_trade_alerts == "BUY" or items_timestamps == array1[len(array1)-1]):
                                    ###print(items_source_data)
                                    ###print("Exit Short")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (open_posistion_price - close_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ###profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    #buy_hold_return.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_losing_trade_short.append(number_of_bars_in_each_losing_trade_short)
                                        
                                    closed_trades = closed_trades + 1
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_winning_trade_short.append(number_of_bars_in_each_winning_trade_short)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    if(investment_revenue > 0):
                                        gross_profit_short.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_short.append(investment_revenue)
                                    closed_trades_short = closed_trades_short + 1
                                   
                                    
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(0)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    
                                    #print('-----------')
                                    
                                    break
                        
                            if(money < 0):
                                break
                    
                            
                        else:
                            ##print('-----------')
                            ##print(items_source_data)
                            ###print("HOLD")
                            place_holder = 0
                            number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                            ##print(number_of_bars_in_each_trade)
                            ###print('-----------')
                            ##print(gross_profit)
                        ##print(excess_returns)
                        ##print(r_minus_rf)
                        
            
            
                       
            
                sum_investment_revenue_2 = sum(investment_revenue_append)
                ##print(sum_investment_revenue_2)
                
                if(sum_investment_revenue_2 == 0):
                    continue
                
                ##print('yes')
                ##print(investment_revenue_append)
                if(length_sell_lag != -1 or length_buy_lag != -1):
                    percentage_movements = pd.DataFrame(percentage_gain_append)
                    ##print(percentage_movements)
                    percentage_ticker_df = pd.DataFrame(percentage_gain_tickers)
                    dollar_ticker_df = pd.DataFrame(investment_revenue_append)
                    portfolio_total_df = pd.DataFrame(portfolio_total_append)
                    ##print(percentage_ticker_df)
                    #deviation_df = pd.DataFrame(deviation_results)
                    ##print(deviation_df)
                    action_object_df = pd.DataFrame(pos_object)
                    pos_time_df = pd.DataFrame(pos_time)
                    
                    
                    
                    pg_concat = pd.concat([percentage_movements,dollar_ticker_df,portfolio_total_df,percentage_ticker_df,action_object_df,pos_time_df], axis=1)
                    pg_concat.columns = ["Percentage","Dollar","Portfolio Total","Ticker","Position Object","Position Time"]
                    
                    ####print('-----------------')
                    ####print('-----------------')
                        
                    ####print(percentage_gain_append)
                    ##print(deviation_df)
                    ##print(pg_concat)
                    pg_concat.to_csv('one_day_'+str(action_object[0])+'_percentage_movements.csv')
                        
                        
            return(sum_investment_revenue_2)
            
        sum_investment_revenue_2 = backtest_two()                              
        
        
                
               
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        startTime = time.time()
        def backtest_one():
            
            #current_date = '2022-08-18 06:30:00-07:00'
            ##print("Chosen Date:", current_date)
            
            
            csv_ticker_list = pd.read_csv('ticker_parameter_grades.csv')
            ticker_list = csv_ticker_list['Ticker'].to_numpy().tolist()
            
            #print(ticker_list)
            
            starting_money = last_equity
        
            
            #action_object = [2,2,2,2,2,2,2,2,2,2]
            action_object = [1,1,1,1]
            #action_object = [0,0,0,0,0,0,0,0,0,0]
            
            
            percentage_gain_append = []
            percentage_gain_tickers = []
            deviation_results = []
            pos_object = []
            pos_time = []
            investment_revenue_append = []
            portfolio_total_append = []
            
            for ticker, items_action_object in zip(ticker_list, action_object):
                
                money = starting_money
                
                
                
                src_open = pd.read_csv('PMAX_'+ticker+'_alert_source_tradingview_data.csv')
                #src_open.iloc[200:]
                ##print(src_open)
                
                
                
                
                #shit = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 06:30:00-07:00")]
                ##print(shit.index[0])
                
                #dumb = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 07:00:00-07:00")]
                ##print(dumb.index[0])
                
                ##print('---------------------')
                ##print(src_open['Timestamp'][shit.index[0]:dumb.index[0]])
                
                ##print(ticker)
                array1 = []
                for stuff in src_open['Timestamp']:
                    if(stuff[0:10] == time_string_initial_data):
                        array1.append(stuff)
                        ##print(stuff)
                
                ##print(array1[0])
                
                index = src_open[src_open['Timestamp'] == array1[0]].index[0]
                ##print("Index Number for starting point:", index)
            
                end_index = src_open[src_open['Timestamp'] == array1[len(array1)-1]].index[0]
                ##print("End Index Number for starting point:", end_index)
                
                ##print(len(array1)-1)
                ##print(array1[len(array1)-1])
                
                ##index = 0
                
                ##print(src_open[index:])
                
            
                
                closed_trades = 0
                number_of_bars_in_each_trade = 0
                number_of_bars_in_each_winning_trade = 0
                number_of_bars_in_each_loss_trade = 0
                
                closed_trades_long = 0
                number_of_bars_in_each_trade_long = 0
                number_of_bars_in_each_winning_trade_long = 0
                number_of_bars_in_each_loss_trade_long = 0
                
                closed_trades_short = 0
                number_of_bars_in_each_trade_short = 0
                number_of_bars_in_each_winning_trade_short = 0
                number_of_bars_in_each_losing_trade_short = 0
                
                gross_profit = []
                gross_loss = []
                portfolio_totals = []
                buy_hold_return_append = []
                excess_returns = []
                percentage_profit_or_loss = []
                negative_assets = []
                max_contracts_held = []
                #closed_trades = []
                positive_assets = []
                average_trade = []
                average_of_bars_in_each_trade = [0]
                average_of_bars_in_winning_trade = []
                average_of_bars_in_losing_trade = []
                
                gross_profit_long = []
                gross_loss_long = []
                max_contracts_held_long = []
                #closed_trades_long = []
                average_trade_long = []
                average_of_bars_in_each_trade_long = [0]
                average_of_bars_in_winning_trade_long = []
                average_of_bars_in_losing_trade_long = []
                
                gross_profit_short = []
                gross_loss_short = []
                max_contracts_held_short = []
                #closed_trades_short = []
                average_trade_short = []
                average_of_bars_in_each_trade_short = [0]
                average_of_bars_in_winning_trade_short = []
                average_of_bars_in_losing_trade_short = []
                
                
                src_open['Trade_Alerts'][index:].to_numpy().tolist
                all_lag = np.array(src_open['Trade_Alerts'][index:])
                sell_lag_index = np.where(all_lag == 'SELL')[0]
                buy_lag_index = np.where(all_lag == 'BUY')[0]
             
                length_sell_lag = len(sell_lag_index)-1                                        
                ##print(length_sell_lag)
                length_buy_lag = len(buy_lag_index)-1  
                
                
                if(items_action_object == 1):
                    #print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    ##print('Ticker:', ticker)
                    
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        ##print(items_source_data)
                        ##print(items_trade_alerts)
                        
                        
                        if(items_trade_alerts == 'BUY'):
                            #print('BUY Indicated')
                            ###print(items_source_data)
                            ###print("Enter LONG")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #quantity_shares_offset = (money/open_posistion_price) - quantity_shares
                            ##print("quantity_shares_offset", quantity_shares_offset)              
                            #remainder_money = quantity_shares_offset*open_posistion_price
                            ##print("remainder_money", remainder_money)
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_long.append(quantity_shares)
                            ###print('-----------')
                            #break
                            
                            for items_source_data, items_trade_alerts, items_timestamps in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                number_of_bars_in_each_winning_trade_long = number_of_bars_in_each_winning_trade_long + 1
                                number_of_bars_in_each_loss_trade_long = number_of_bars_in_each_loss_trade_long + 1
                                
                                if(items_trade_alerts == "SELL" or items_timestamps == array1[len(array1)-1]):
                                    ###print('SELL Indicated')
                                    ###print(items_source_data)
                                    ###print("Exit Long")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (close_posistion_price - open_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ##profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print(portfolio_totals)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    ##print(buy_hold_return)
                                    #buy_hold_return_append.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_losing_trade_long.append(number_of_bars_in_each_loss_trade_long)
                                    
                                    closed_trades = closed_trades + 1
                                    ##print(closed_trades)
                                    
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_winning_trade_long.append(number_of_bars_in_each_winning_trade_long)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                  
                                    if(investment_revenue > 0):
                                        gross_profit_long.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_long.append(investment_revenue)
                                    
                                    average_trade_long.append(investment_revenue)
                                    
                                    closed_trades_long = closed_trades_long + 1
                                    ##print(closed_trades_long)
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
        
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(1)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    #print('-----------')
                                    break
                        
                                
                                    
                                    
                                else:
                                    place_holder = 0
                                    number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)   
                                   
                                    
                        
                        
                        elif(items_trade_alerts == "SELL"):
                            
                            for items_trade_alerts, items_source_data in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:]):
                                
                                if(items_trade_alerts == "BUY"):
                                    nothing = 0
            
                                    ##money = money + amount_left
                                    break
                        
                            if(money < 0):
                                break
                    
                            
                        else:
                            ##print('-----------')
                            ##print(items_source_data)
                            ###print("HOLD")
                            place_holder = 0
                            number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                            ##print(number_of_bars_in_each_trade)
                            ###print('-----------')
                            ##print(gross_profit)
                        ##print(excess_returns)
                        ##print(r_minus_rf)
                
                sum_investment_revenue_1 = sum(investment_revenue_append)
                ##print('yes')
                ##print(investment_revenue_append)
                
                if(sum_investment_revenue_1 == 0):
                    continue
                
                if(length_buy_lag != -1):
                    percentage_movements = pd.DataFrame(percentage_gain_append)
                    ##print(percentage_movements)
                    percentage_ticker_df = pd.DataFrame(percentage_gain_tickers)
                    dollar_ticker_df = pd.DataFrame(investment_revenue_append)
                    portfolio_total_df = pd.DataFrame(portfolio_total_append)
                    ##print(percentage_ticker_df)
                    #deviation_df = pd.DataFrame(deviation_results)
                    ##print(deviation_df)
                    action_object_df = pd.DataFrame(pos_object)
                    pos_time_df = pd.DataFrame(pos_time)
                    
                    
                    
                    pg_concat = pd.concat([percentage_movements,dollar_ticker_df,portfolio_total_df,percentage_ticker_df,action_object_df,pos_time_df], axis=1)
                    pg_concat.columns = ["Percentage","Dollar","Portfolio Total","Ticker","Position Object","Position Time"]
                    
                    ####print('-----------------')
                    ####print('-----------------')
                        
                    ####print(percentage_gain_append)
                    ##print(deviation_df)
                    ##print(pg_concat)
                    pg_concat.to_csv('one_day_'+str(action_object[0])+'_percentage_movements.csv')
            
                    #print('ONE DAY SIMMUALTION COMPLETE')
                    
            return(sum_investment_revenue_1)
            
        sum_investment_revenue_1 = backtest_one() 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        startTime = time.time()
        def backtest_zero():
            
            #current_date = '2022-08-18 06:30:00-07:00'
            ##print("Chosen Date:", current_date)
            
            
            csv_ticker_list = pd.read_csv('ticker_parameter_grades.csv')
            ticker_list = csv_ticker_list['Ticker'].to_numpy().tolist()
            
            #print(ticker_list)
            
            starting_money = last_equity
        
            
            #action_object = [2,2,2,2,2,2,2,2,2,2]
            #action_object = [1,1,1,1,1,1,1,1,1,1]
            action_object = [0,0,0,0]
            
            
            percentage_gain_append = []
            percentage_gain_tickers = []
            deviation_results = []
            pos_object = []
            pos_time = []
            investment_revenue_append = []
            portfolio_total_append = []
            
            for ticker, items_action_object in zip(ticker_list, action_object):
                
                money = starting_money
                
                
                
                src_open = pd.read_csv('PMAX_'+ticker+'_alert_source_tradingview_data.csv')
                #src_open.iloc[200:]
                ##print(src_open)
                
                
                
                
                #shit = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 06:30:00-07:00")]
                ##print(shit.index[0])
                
                #dumb = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 07:00:00-07:00")]
                ##print(dumb.index[0])
                
                ##print('---------------------')
                ##print(src_open['Timestamp'][shit.index[0]:dumb.index[0]])
                
                ##print(ticker)
                array1 = []
                for stuff in src_open['Timestamp']:
                    if(stuff[0:10] == time_string_initial_data):
                        array1.append(stuff)
                        ##print(stuff)
                
                ##print(array1[0])
                
                index = src_open[src_open['Timestamp'] == array1[0]].index[0]
                ##print("Index Number for starting point:", index)
            
                end_index = src_open[src_open['Timestamp'] == array1[len(array1)-1]].index[0]
                ##print("End Index Number for starting point:", end_index)
                
                ##print(len(array1)-1)
                ##print(array1[len(array1)-1])
                
                ##index = 0
                
                ##print(src_open[index:])
                
            
                
                closed_trades = 0
                number_of_bars_in_each_trade = 0
                number_of_bars_in_each_winning_trade = 0
                number_of_bars_in_each_loss_trade = 0
                
                closed_trades_long = 0
                number_of_bars_in_each_trade_long = 0
                number_of_bars_in_each_winning_trade_long = 0
                number_of_bars_in_each_loss_trade_long = 0
                
                closed_trades_short = 0
                number_of_bars_in_each_trade_short = 0
                number_of_bars_in_each_winning_trade_short = 0
                number_of_bars_in_each_losing_trade_short = 0
                
                gross_profit = []
                gross_loss = []
                portfolio_totals = []
                buy_hold_return_append = []
                excess_returns = []
                percentage_profit_or_loss = []
                negative_assets = []
                max_contracts_held = []
                #closed_trades = []
                positive_assets = []
                average_trade = []
                average_of_bars_in_each_trade = [0]
                average_of_bars_in_winning_trade = []
                average_of_bars_in_losing_trade = []
                
                gross_profit_long = []
                gross_loss_long = []
                max_contracts_held_long = []
                #closed_trades_long = []
                average_trade_long = []
                average_of_bars_in_each_trade_long = [0]
                average_of_bars_in_winning_trade_long = []
                average_of_bars_in_losing_trade_long = []
                
                gross_profit_short = []
                gross_loss_short = []
                max_contracts_held_short = []
                #closed_trades_short = []
                average_trade_short = []
                average_of_bars_in_each_trade_short = [0]
                average_of_bars_in_winning_trade_short = []
                average_of_bars_in_losing_trade_short = []
                
                
                src_open['Trade_Alerts'][index:].to_numpy().tolist
                all_lag = np.array(src_open['Trade_Alerts'][index:])
                sell_lag_index = np.where(all_lag == 'SELL')[0]
             
                length_sell_lag = len(sell_lag_index)-1                                        
                ##print(length_sell_lag)
                    
                if(items_action_object == 0):
                    #print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        
                          
                       
                        if(length_sell_lag != -1):
                            if(items_trade_alerts == "SELL"):
                                ###print(items_source_data)
                                #print("SELL Indicated")
                                place_holder = 0
                                #break
                                ###print('-----------')
                                ###print("Money:", money)
                                ###print("Posistion:", items_trade_alerts)
                                open_posistion_price =  items_source_data
                                #print("open_posistion_price:", open_posistion_price)
                                
                                
                                quantity_shares = (int(stock_dev_money/open_posistion_price))
                                #print("Shares", quantity_shares)        
                                
                                investment_amount = (quantity_shares * open_posistion_price)
                                ##print("investment_amount", investment_amount)
                                amount_left = stock_dev_money - investment_amount
                                ##print("amount_left", amount_left)
                                
                                
                                
                                
                                
                                #money = money+remainder_money
                                ##print("Money:", money)
                                
                                max_contracts_held.append(quantity_shares)
                                max_contracts_held_short.append(quantity_shares)
                                ###print('-----------')
                                #break
                                for items_trade_alerts, items_source_data, items_timestamps in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:], src_open['Timestamp'][index:]):
                                    number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                    number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                    ##print(number_of_bars_in_each_winning_trade)
                                    ##print(items_source_data)
                                    number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                    
                                    number_of_bars_in_each_trade_short = number_of_bars_in_each_trade_short + 1
                                    number_of_bars_in_each_winning_trade_short = number_of_bars_in_each_winning_trade_short + 1
                                    number_of_bars_in_each_losing_trade_short = number_of_bars_in_each_losing_trade_short + 1
                                    if(items_trade_alerts == "BUY" or items_timestamps == array1[len(array1)-1]):
                                        ###print(items_source_data)
                                        ###print("Exit Short")
                                        place_holder = 0
                                        ###print('-----------')
                                        close_posistion_price = items_source_data
                                        #print("Close Posistion Price:", close_posistion_price)
                                        percentage_profit_loss = (open_posistion_price - close_posistion_price)/open_posistion_price
                                        #print("% Profit/Loss:", percentage_profit_loss)
                                        percentage_profit_or_loss.append(percentage_profit_loss)
                                        ###profit_loss = (close_posistion_price * quantity_shares)
                                        profit_loss = (investment_amount * (1+percentage_profit_loss))
                                        #print("Profit/Loss:", profit_loss)
                                        investment_revenue = profit_loss - (investment_amount)
                                        #print("Investment Revenue:", investment_revenue)
                                        investment_revenue_append.append(investment_revenue)
                                        excess_return = percentage_profit_loss - 0.0238
                                        excess_returns.append(excess_return)
                                        money = profit_loss+amount_left
                                        portfolio_total_append.append(money)
                                        if(investment_revenue > 0):
                                            gross_profit.append(investment_revenue)
                                        elif(investment_revenue < 0):
                                            gross_loss.append(investment_revenue)
                                        portfolio_totals.append(profit_loss)
                                        ##print('-----------')
                                        buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                        #buy_hold_return.append(buy_hold_return)
                                        if(percentage_profit_loss < 0):
                                            negative_assets.append((percentage_profit_loss-0.0238)**2)
                                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                            average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                            
                                            average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                            average_of_bars_in_losing_trade_short.append(number_of_bars_in_each_losing_trade_short)
                                            
                                        closed_trades = closed_trades + 1
                                        if(percentage_profit_loss > 0):
                                            positive_assets.append(percentage_profit_loss)
                                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                            average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                            
                                            average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                            average_of_bars_in_winning_trade_short.append(number_of_bars_in_each_winning_trade_short)
                                            
                                        average_trade.append(investment_revenue)
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        if(investment_revenue > 0):
                                            gross_profit_short.append(investment_revenue)
                                        elif(investment_revenue < 0):
                                            gross_loss_short.append(investment_revenue)
                                        closed_trades_short = closed_trades_short + 1
                                       
                                        
                                        
                                        ##money = money + amount_left
                                        
                                        #print("Portfolio Value:", money)
                                        
                                        stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
                                        
                                        deviation_results.append((stock_dev_money))
                                        percentage_gain_append.append(percentage_profit_loss)
                                        percentage_gain_tickers.append(ticker)
                                        pos_object.append(0)
                                        
                                        pos_time.append(src_open['Timestamp'][index])
                                        ##print(position_time)
                                        
                                        #print('-----------')
                                        
                                        break
                                    
                                    
                                
                                if(money < 0):
                                    break
                        
                                ##percentage_gain_append.append((money-starting_money)/starting_money)
                                ##print(percentage_gain_append)
                                
                            else:
                                ##print('-----------')
                                ##print(items_source_data)
                                ###print("HOLD")
                                place_holder = 0
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                ##print(number_of_bars_in_each_trade)
                                ###print('-----------')
                                ##print(gross_profit)
                            ##print(excess_returns)
                            ##print(r_minus_rf)
                        
                ##print('yes')
                sum_investment_revenue_0 = sum(investment_revenue_append)
                
                
                if(sum_investment_revenue_0 == 0):
                    continue
                
                
                if(length_sell_lag != -1):
                    percentage_movements = pd.DataFrame(percentage_gain_append)
                    ##print(percentage_movements)
                    percentage_ticker_df = pd.DataFrame(percentage_gain_tickers)
                    dollar_ticker_df = pd.DataFrame(investment_revenue_append)
                    portfolio_total_df = pd.DataFrame(portfolio_total_append)
                    ##print(percentage_ticker_df)
                    #deviation_df = pd.DataFrame(deviation_results)
                    ##print(deviation_df)
                    action_object_df = pd.DataFrame(pos_object)
                    pos_time_df = pd.DataFrame(pos_time)
                    
                    
                    
                    pg_concat = pd.concat([percentage_movements,dollar_ticker_df,portfolio_total_df,percentage_ticker_df,action_object_df,pos_time_df], axis=1)
                    pg_concat.columns = ["Percentage","Dollar","Portfolio Total","Ticker","Position Object","Position Time"]
                    
                    ####print('-----------------')
                    ####print('-----------------')
                        
                    ####print(percentage_gain_append)
                    ##print(deviation_df)
                    ##print(pg_concat)
                    pg_concat.to_csv('one_day_'+str(action_object[0])+'_percentage_movements.csv')
                        
                    #print('ONE DAY SIMMUALTION COMPLETE')
            
            return(sum_investment_revenue_0)   
            
        sum_investment_revenue_0 = backtest_zero() 
        
        
              
            
            
        def backtest_per_chance():
            
            csv_ticker_list = pd.read_csv('ticker_parameter_grades.csv')
            ##print(perc_chance_param)
            
            ticker_list = csv_ticker_list['Ticker'].to_numpy().tolist()
            
            #print(ticker_list)
            
            starting_money = last_equity
        
        
            
            
            
            action_object = csv_ticker_list['Percent Position'].to_numpy().tolist()
          
             
            
            
            
            
            percentage_gain_append = []
            percentage_gain_tickers = []
            deviation_results = []
            pos_object = []
            pos_time = []
            investment_revenue_append = []
            portfolio_total_append = []
            
            for ticker, items_action_object in zip(ticker_list, action_object):
                
                money = starting_money
                
                
                
                src_open = pd.read_csv('PMAX_'+ticker+'_alert_source_tradingview_data.csv')
                #src_open.iloc[200:]
                ##print(src_open)
                
                
                
                
                #shit = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 06:30:00-07:00")]
                ##print(shit.index[0])
                
                #dumb = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 07:00:00-07:00")]
                ##print(dumb.index[0])
                
                ##print('---------------------')
                ##print(src_open['Timestamp'][shit.index[0]:dumb.index[0]])
                
                ##print(ticker)
                array1 = []
                for stuff in src_open['Timestamp']:
                    if(stuff[0:10] == time_string_initial_data):
                        array1.append(stuff)
                        ##print(stuff)
                
                ##print(array1[0])
                
                index = src_open[src_open['Timestamp'] == array1[0]].index[0]
                ##print("Index Number for starting point:", index)
            
                end_index = src_open[src_open['Timestamp'] == array1[len(array1)-1]].index[0]
                ##print("End Index Number for starting point:", end_index)
                
                ##print(len(array1)-1)
                ##print(array1[len(array1)-1])
                
                ##index = 0
                
                ##print(src_open[index:])
                
            
                
                closed_trades = 0
                number_of_bars_in_each_trade = 0
                number_of_bars_in_each_winning_trade = 0
                number_of_bars_in_each_loss_trade = 0
                
                closed_trades_long = 0
                number_of_bars_in_each_trade_long = 0
                number_of_bars_in_each_winning_trade_long = 0
                number_of_bars_in_each_loss_trade_long = 0
                
                closed_trades_short = 0
                number_of_bars_in_each_trade_short = 0
                number_of_bars_in_each_winning_trade_short = 0
                number_of_bars_in_each_losing_trade_short = 0
                
                gross_profit = []
                gross_loss = []
                portfolio_totals = []
                buy_hold_return_append = []
                excess_returns = []
                percentage_profit_or_loss = []
                negative_assets = []
                max_contracts_held = []
                #closed_trades = []
                positive_assets = []
                average_trade = []
                average_of_bars_in_each_trade = [0]
                average_of_bars_in_winning_trade = []
                average_of_bars_in_losing_trade = []
                
                gross_profit_long = []
                gross_loss_long = []
                max_contracts_held_long = []
                #closed_trades_long = []
                average_trade_long = []
                average_of_bars_in_each_trade_long = [0]
                average_of_bars_in_winning_trade_long = []
                average_of_bars_in_losing_trade_long = []
                
                gross_profit_short = []
                gross_loss_short = []
                max_contracts_held_short = []
                #closed_trades_short = []
                average_trade_short = []
                average_of_bars_in_each_trade_short = [0]
                average_of_bars_in_winning_trade_short = []
                average_of_bars_in_losing_trade_short = []
                
                
                src_open['Trade_Alerts'][index:].to_numpy().tolist
                all_lag = np.array(src_open['Trade_Alerts'][index:])
                sell_lag_index = np.where(all_lag == 'SELL')[0]
                buy_lag_index = np.where(all_lag == 'BUY')[0]
             
                length_sell_lag = len(sell_lag_index)-1                                        
                ##print(length_sell_lag)
                length_buy_lag = len(buy_lag_index)-1  
                
                
                if(items_action_object == 1):
                    #print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        ##print(items_source_data)
                        ##print(items_trade_alerts)
                        
                        if(length_buy_lag != -1):
                            
                            if(items_trade_alerts == 'BUY'):
                                
                                #print(ticker)
                                stock_dev_money = starting_money/len(ticker_list)
                                ##print('Ticker:', ticker)
                                
                                for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                                    index = index + 1
                                    ##print(items_source_data)
                                    ##print(items_trade_alerts)
                                    
                                    
                                    if(items_trade_alerts == 'BUY'):
                                        #print('BUY Indicated')
                                        ###print(items_source_data)
                                        ###print("Enter LONG")
                                        place_holder = 0
                                        #break
                                        ###print('-----------')
                                        ###print("Money:", money)
                                        ###print("Posistion:", items_trade_alerts)
                                        open_posistion_price =  items_source_data
                                        #print("open_posistion_price:", open_posistion_price)
                                        
                                        
                                        quantity_shares = (int(stock_dev_money/open_posistion_price))
                                        #print("Shares", quantity_shares)        
                        
                                        investment_amount = (quantity_shares * open_posistion_price)
                                        ##print("investment_amount", investment_amount)
                                        amount_left = stock_dev_money - investment_amount
                                        ##print("amount_left", amount_left)
                                        
                                        
                                        
                                        
                                        
                                        #quantity_shares_offset = (money/open_posistion_price) - quantity_shares
                                        ##print("quantity_shares_offset", quantity_shares_offset)              
                                        #remainder_money = quantity_shares_offset*open_posistion_price
                                        ##print("remainder_money", remainder_money)
                                        #money = money+remainder_money
                                        ##print("Money:", money)
                                        
                                        max_contracts_held.append(quantity_shares)
                                        max_contracts_held_long.append(quantity_shares)
                                        ###print('-----------')
                                        #break
                                        
                                        for items_source_data, items_trade_alerts, items_timestamps in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:], src_open['Timestamp'][index:]):
                                            number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                            number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                            ##print(number_of_bars_in_each_winning_trade)
                                            ##print(items_source_data)
                                            number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                            
                                            number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                            number_of_bars_in_each_winning_trade_long = number_of_bars_in_each_winning_trade_long + 1
                                            number_of_bars_in_each_loss_trade_long = number_of_bars_in_each_loss_trade_long + 1
                                            
                                            if(items_trade_alerts == "SELL" or items_timestamps == array1[len(array1)-1]):
                                                ###print('SELL Indicated')
                                                ###print(items_source_data)
                                                ###print("Exit Long")
                                                place_holder = 0
                                                ###print('-----------')
                                                close_posistion_price = items_source_data
                                                #print("Close Posistion Price:", close_posistion_price)
                                                percentage_profit_loss = (close_posistion_price - open_posistion_price)/open_posistion_price
                                                #print("% Profit/Loss:", percentage_profit_loss)
                                                percentage_profit_or_loss.append(percentage_profit_loss)
                                                ##profit_loss = (close_posistion_price * quantity_shares)
                                                profit_loss = (investment_amount * (1+percentage_profit_loss))
                                                #print("Profit/Loss:", profit_loss)
                                                investment_revenue = profit_loss - (investment_amount)
                                                #print("Investment Revenue:", investment_revenue)
                                                investment_revenue_append.append(investment_revenue)
                                                excess_return = percentage_profit_loss - 0.0238
                                                excess_returns.append(excess_return)
                                                money = profit_loss+amount_left
                                                portfolio_total_append.append(money)
                                                
                                                if(investment_revenue > 0):
                                                    gross_profit.append(investment_revenue)
                                                elif(investment_revenue < 0):
                                                    gross_loss.append(investment_revenue)
                                                portfolio_totals.append(profit_loss)
                                                ##print(portfolio_totals)
                                                ##print('-----------')
                                                buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                                ##print(buy_hold_return)
                                                #buy_hold_return_append.append(buy_hold_return)
                                                if(percentage_profit_loss < 0):
                                                    negative_assets.append((percentage_profit_loss-0.0238)**2)
                                                    average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                                    average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                                    
                                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                                    average_of_bars_in_losing_trade_long.append(number_of_bars_in_each_loss_trade_long)
                                                
                                                closed_trades = closed_trades + 1
                                                ##print(closed_trades)
                                                
                                                if(percentage_profit_loss > 0):
                                                    positive_assets.append(percentage_profit_loss)
                                                    average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                                    average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                                    
                                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                                    average_of_bars_in_winning_trade_long.append(number_of_bars_in_each_winning_trade_long)
                                                    
                                                average_trade.append(investment_revenue)
                                                
                                                
                                                
                                                
                                              
                                                if(investment_revenue > 0):
                                                    gross_profit_long.append(investment_revenue)
                                                elif(investment_revenue < 0):
                                                    gross_loss_long.append(investment_revenue)
                                                
                                                average_trade_long.append(investment_revenue)
                                                
                                                closed_trades_long = closed_trades_long + 1
                                                ##print(closed_trades_long)
                                                
                                                ##money = money + amount_left
                                                
                                                #print("Portfolio Value:", money)
                                                
                                                stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
        
                                                
                                                deviation_results.append((stock_dev_money))
                                                percentage_gain_append.append(percentage_profit_loss)
                                                percentage_gain_tickers.append(ticker)
                                                pos_object.append(1)
                                                
                                                pos_time.append(src_open['Timestamp'][index])
                                                ##print(position_time)
                                                #print('-----------')
                                                break
                                    
                                        
                                        
                                    else:
                                        place_holder = 0
                                        number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)   
                                       
                                        
                        
                        
                        elif(items_trade_alerts == "SELL"):
                            
                            for items_trade_alerts, items_source_data in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:]):
                                
                                if(items_trade_alerts == "BUY"):
                                    nothing = 0
            
                                    ##money = money + amount_left
                                    break
                        
                            if(money < 0):
                                break
                    
                            
                        else:
                            ##print('-----------')
                            ##print(items_source_data)
                            ###print("HOLD")
                            place_holder = 0
                            number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                            ##print(number_of_bars_in_each_trade)
                            ###print('-----------')
                            ##print(gross_profit)
                        ##print(excess_returns)
                        ##print(r_minus_rf)
                        
                        
                        
                        
                
                if(items_action_object == 0):
                    #print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        
                        
                        if(items_trade_alerts == 'BUY'):
                                               
                            for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):                    
                                                        
                                if(items_trade_alerts == "SELL"):
                                    nothing = 0
                                    
                                    break
                                else:
                                    place_holder = 0
                                    number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)   
                       
                        if(length_sell_lag != -1):
                            if(items_trade_alerts == "SELL"):
                                ###print(items_source_data)
                                #print("SELL Indicated")
                                place_holder = 0
                                #break
                                ###print('-----------')
                                ###print("Money:", money)
                                ###print("Posistion:", items_trade_alerts)
                                open_posistion_price =  items_source_data
                                #print("open_posistion_price:", open_posistion_price)
                                
                                
                                quantity_shares = (int(stock_dev_money/open_posistion_price))
                                #print("Shares", quantity_shares)        
                                
                                investment_amount = (quantity_shares * open_posistion_price)
                                ##print("investment_amount", investment_amount)
                                amount_left = stock_dev_money - investment_amount
                                ##print("amount_left", amount_left)
                                
                                
                                
                                
                                
                                #money = money+remainder_money
                                ##print("Money:", money)
                                
                                max_contracts_held.append(quantity_shares)
                                max_contracts_held_short.append(quantity_shares)
                                ###print('-----------')
                                #break
                                for items_trade_alerts, items_source_data, items_timestamps in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:], src_open['Timestamp'][index:]):
                                    number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                    number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                    ##print(number_of_bars_in_each_winning_trade)
                                    ##print(items_source_data)
                                    number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                    
                                    number_of_bars_in_each_trade_short = number_of_bars_in_each_trade_short + 1
                                    number_of_bars_in_each_winning_trade_short = number_of_bars_in_each_winning_trade_short + 1
                                    number_of_bars_in_each_losing_trade_short = number_of_bars_in_each_losing_trade_short + 1
                                    if(items_trade_alerts == "BUY" or items_timestamps == array1[len(array1)-1]):
                                        ###print(items_source_data)
                                        ###print("Exit Short")
                                        place_holder = 0
                                        ###print('-----------')
                                        close_posistion_price = items_source_data
                                        #print("Close Posistion Price:", close_posistion_price)
                                        percentage_profit_loss = (open_posistion_price - close_posistion_price)/open_posistion_price
                                        #print("% Profit/Loss:", percentage_profit_loss)
                                        percentage_profit_or_loss.append(percentage_profit_loss)
                                        ###profit_loss = (close_posistion_price * quantity_shares)
                                        profit_loss = (investment_amount * (1+percentage_profit_loss))
                                        #print("Profit/Loss:", profit_loss)
                                        investment_revenue = profit_loss - (investment_amount)
                                        #print("Investment Revenue:", investment_revenue)
                                        investment_revenue_append.append(investment_revenue)
                                        excess_return = percentage_profit_loss - 0.0238
                                        excess_returns.append(excess_return)
                                        money = profit_loss+amount_left
                                        portfolio_total_append.append(money)
                                        if(investment_revenue > 0):
                                            gross_profit.append(investment_revenue)
                                        elif(investment_revenue < 0):
                                            gross_loss.append(investment_revenue)
                                        portfolio_totals.append(profit_loss)
                                        ##print('-----------')
                                        buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                        #buy_hold_return.append(buy_hold_return)
                                        if(percentage_profit_loss < 0):
                                            negative_assets.append((percentage_profit_loss-0.0238)**2)
                                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                            average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                            
                                            average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                            average_of_bars_in_losing_trade_short.append(number_of_bars_in_each_losing_trade_short)
                                            
                                        closed_trades = closed_trades + 1
                                        if(percentage_profit_loss > 0):
                                            positive_assets.append(percentage_profit_loss)
                                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                            average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                            
                                            average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                            average_of_bars_in_winning_trade_short.append(number_of_bars_in_each_winning_trade_short)
                                            
                                        average_trade.append(investment_revenue)
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        if(investment_revenue > 0):
                                            gross_profit_short.append(investment_revenue)
                                        elif(investment_revenue < 0):
                                            gross_loss_short.append(investment_revenue)
                                        closed_trades_short = closed_trades_short + 1
                                       
                                        
                                        
                                        ##money = money + amount_left
                                        
                                        #print("Portfolio Value:", money)
                                        
                                        stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
                                        
                                        deviation_results.append((stock_dev_money))
                                        percentage_gain_append.append(percentage_profit_loss)
                                        percentage_gain_tickers.append(ticker)
                                        pos_object.append(0)
                                        
                                        pos_time.append(src_open['Timestamp'][index])
                                        ##print(position_time)
                                        
                                        #print('-----------')
                                        
                                        break
                                    
                                    
                                
                                if(money < 0):
                                    break
                        
                                ##percentage_gain_append.append((money-starting_money)/starting_money)
                                ##print(percentage_gain_append)
                                
                            else:
                                ##print('-----------')
                                ##print(items_source_data)
                                ###print("HOLD")
                                place_holder = 0
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                ##print(number_of_bars_in_each_trade)
                                ###print('-----------')
                                ##print(gross_profit)
                            ##print(excess_returns)
                            ##print(r_minus_rf)
                
                
                ##print('yes')
                #print(length_sell_lag)
                #print(length_buy_lag)
                #print('yes')
                sum_investment_revenue_3 = sum(investment_revenue_append)
                
                if(sum_investment_revenue_3 == 0):
                    continue
                
                if(length_buy_lag != 0):
                    percentage_movements = pd.DataFrame(percentage_gain_append)
                    ##print(percentage_movements)
                    percentage_ticker_df = pd.DataFrame(percentage_gain_tickers)
                    dollar_ticker_df = pd.DataFrame(investment_revenue_append)
                    portfolio_total_df = pd.DataFrame(portfolio_total_append)
                    ##print(percentage_ticker_df)
                    #deviation_df = pd.DataFrame(deviation_results)
                    ##print(deviation_df)
                    action_object_df = pd.DataFrame(pos_object)
                    pos_time_df = pd.DataFrame(pos_time)
                    
                    
                    
                    pg_concat = pd.concat([percentage_movements,dollar_ticker_df,portfolio_total_df,percentage_ticker_df,action_object_df,pos_time_df], axis=1)
                    pg_concat.columns = ["Percentage","Dollar","Portfolio Total","Ticker","Position Object","Position Time"]
                    
                    ####print('-----------------')
                    ####print('-----------------')
                        
                    ####print(percentage_gain_append)
                    ##print(deviation_df)
                    ##print(pg_concat)
                    pg_concat.to_csv('one_day_3_percentage_movements.csv')
                        
                    #print('ONE DAY SIMMUALTION COMPLETE')
            
            
            return(sum_investment_revenue_3)    
            
            
            
        #sum_investment_revenue_3 = backtest_per_chance()   
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def backtest_max_dev():
            
            csv_ticker_list = pd.read_csv('ticker_parameter_grades.csv')
            ##print(perc_chance_param)
            
            ticker_list = csv_ticker_list['Ticker'].to_numpy().tolist()
            
            #print(ticker_list)
            
            starting_money = last_equity
        
        
            
            
            
            action_object = csv_ticker_list['Portfolio Max Deviation'].to_numpy().tolist()
            
             
            
            
            
            
            percentage_gain_append = []
            percentage_gain_tickers = []
            deviation_results = []
            pos_object = []
            pos_time = []
            investment_revenue_append = []
            portfolio_total_append = []
            
            
            for ticker, items_action_object in zip(ticker_list, action_object):
                
                money = starting_money
                
                
                
                src_open = pd.read_csv('PMAX_'+ticker+'_alert_source_tradingview_data.csv')
                #src_open.iloc[200:]
                ##print(src_open)
                
                
                
                
                #shit = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 06:30:00-07:00")]
                ##print(shit.index[0])
                
                #dumb = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 07:00:00-07:00")]
                ##print(dumb.index[0])
                
                ##print('---------------------')
                ##print(src_open['Timestamp'][shit.index[0]:dumb.index[0]])
                
                ##print(ticker)
                array1 = []
                for stuff in src_open['Timestamp']:
                    if(stuff[0:10] == time_string_initial_data):
                        array1.append(stuff)
                        ##print(stuff)
                
                ##print(array1[0])
                
                index = src_open[src_open['Timestamp'] == array1[0]].index[0]
                ##print("Index Number for starting point:", index)
            
                end_index = src_open[src_open['Timestamp'] == array1[len(array1)-1]].index[0]
                ##print("End Index Number for starting point:", end_index)
                
                ##print(len(array1)-1)
                ##print(array1[len(array1)-1])
                
                ##index = 0
                
                ##print(src_open[index:])
                
            
                
                closed_trades = 0
                number_of_bars_in_each_trade = 0
                number_of_bars_in_each_winning_trade = 0
                number_of_bars_in_each_loss_trade = 0
                
                closed_trades_long = 0
                number_of_bars_in_each_trade_long = 0
                number_of_bars_in_each_winning_trade_long = 0
                number_of_bars_in_each_loss_trade_long = 0
                
                closed_trades_short = 0
                number_of_bars_in_each_trade_short = 0
                number_of_bars_in_each_winning_trade_short = 0
                number_of_bars_in_each_losing_trade_short = 0
                
                gross_profit = []
                gross_loss = []
                portfolio_totals = []
                buy_hold_return_append = []
                excess_returns = []
                percentage_profit_or_loss = []
                negative_assets = []
                max_contracts_held = []
                #closed_trades = []
                positive_assets = []
                average_trade = []
                average_of_bars_in_each_trade = [0]
                average_of_bars_in_winning_trade = []
                average_of_bars_in_losing_trade = []
                
                gross_profit_long = []
                gross_loss_long = []
                max_contracts_held_long = []
                #closed_trades_long = []
                average_trade_long = []
                average_of_bars_in_each_trade_long = [0]
                average_of_bars_in_winning_trade_long = []
                average_of_bars_in_losing_trade_long = []
                
                gross_profit_short = []
                gross_loss_short = []
                max_contracts_held_short = []
                #closed_trades_short = []
                average_trade_short = []
                average_of_bars_in_each_trade_short = [0]
                average_of_bars_in_winning_trade_short = []
                average_of_bars_in_losing_trade_short = []
                
                
                src_open['Trade_Alerts'][index:].to_numpy().tolist
                all_lag = np.array(src_open['Trade_Alerts'][index:])
                sell_lag_index = np.where(all_lag == 'SELL')[0]
                buy_lag_index = np.where(all_lag == 'BUY')[0]
             
                length_sell_lag = len(sell_lag_index)-1                                        
                ##print(length_sell_lag)
                length_buy_lag = len(buy_lag_index)-1  
                
                
                if(items_action_object == 0):
                    #print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    ##print('Ticker:', ticker)
                    
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        ##print(items_source_data)
                        ##print(items_trade_alerts)
                        
                        
                        if(items_trade_alerts == 'BUY'):
                            #print('BUY Indicated')
                            ###print(items_source_data)
                            ###print("Enter LONG")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #quantity_shares_offset = (money/open_posistion_price) - quantity_shares
                            ##print("quantity_shares_offset", quantity_shares_offset)              
                            #remainder_money = quantity_shares_offset*open_posistion_price
                            ##print("remainder_money", remainder_money)
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_long.append(quantity_shares)
                            ###print('-----------')
                            #break
                            
                            for items_source_data, items_trade_alerts, items_timestamps in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                number_of_bars_in_each_winning_trade_long = number_of_bars_in_each_winning_trade_long + 1
                                number_of_bars_in_each_loss_trade_long = number_of_bars_in_each_loss_trade_long + 1
                                
                                if(items_trade_alerts == "SELL" or items_timestamps == array1[len(array1)-1]):
                                    ###print('SELL Indicated')
                                    ###print(items_source_data)
                                    ###print("Exit Long")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (close_posistion_price - open_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ##profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print(portfolio_totals)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    ##print(buy_hold_return)
                                    #buy_hold_return_append.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_losing_trade_long.append(number_of_bars_in_each_loss_trade_long)
                                    
                                    closed_trades = closed_trades + 1
                                    ##print(closed_trades)
                                    
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_winning_trade_long.append(number_of_bars_in_each_winning_trade_long)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                  
                                    if(investment_revenue > 0):
                                        gross_profit_long.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_long.append(investment_revenue)
                                    
                                    average_trade_long.append(investment_revenue)
                                    
                                    closed_trades_long = closed_trades_long + 1
                                    ##print(closed_trades_long)
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
        
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(1)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    #print('-----------')
                                    break
                                else:
                                    place_holder = 0
                                    number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)   
                       
                        
                        elif(items_trade_alerts == "SELL"):
                            ###print(items_source_data)
                            #print("SELL Indicated")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
                            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_short.append(quantity_shares)
                            ###print('-----------')
                            #break
                            for items_trade_alerts, items_source_data, items_timestamps in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_short = number_of_bars_in_each_trade_short + 1
                                number_of_bars_in_each_winning_trade_short = number_of_bars_in_each_winning_trade_short + 1
                                number_of_bars_in_each_losing_trade_short = number_of_bars_in_each_losing_trade_short + 1
                                if(items_trade_alerts == "BUY" or items_timestamps == array1[len(array1)-1]):
                                    ###print(items_source_data)
                                    ###print("Exit Short")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (open_posistion_price - close_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ###profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    #buy_hold_return.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_losing_trade_short.append(number_of_bars_in_each_losing_trade_short)
                                        
                                    closed_trades = closed_trades + 1
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_winning_trade_short.append(number_of_bars_in_each_winning_trade_short)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    if(investment_revenue > 0):
                                        gross_profit_short.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_short.append(investment_revenue)
                                    closed_trades_short = closed_trades_short + 1
                                   
                                    
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(0)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    
                                    #print('-----------')
                                    
                                    break
                        
                            if(money < 0):
                                break
                    
                            
                        else:
                            ##print('-----------')
                            ##print(items_source_data)
                            ###print("HOLD")
                            place_holder = 0
                            number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                            ##print(number_of_bars_in_each_trade)
                            ###print('-----------')
                            ##print(gross_profit)
                        ##print(excess_returns)
                        ##print(r_minus_rf)
                        
                        
                        
                        
                if(items_action_object > 0):
                    #print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        ##print(items_source_data)
                        ##print(items_trade_alerts)
                        
                    
                            
                        if(items_trade_alerts == 'SELL'):
                            #print('BUY Indicated')
                            ###print(items_source_data)
                            ###print("Enter LONG")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #quantity_shares_offset = (money/open_posistion_price) - quantity_shares
                            ##print("quantity_shares_offset", quantity_shares_offset)              
                            #remainder_money = quantity_shares_offset*open_posistion_price
                            ##print("remainder_money", remainder_money)
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_long.append(quantity_shares)
                            ###print('-----------')
                            #break
                            
                            for items_source_data, items_trade_alerts, items_timestamps in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                number_of_bars_in_each_winning_trade_long = number_of_bars_in_each_winning_trade_long + 1
                                number_of_bars_in_each_loss_trade_long = number_of_bars_in_each_loss_trade_long + 1
                                
                                if(items_trade_alerts == "BUY" or items_timestamps == array1[len(array1)-1]):
                                    ###print('SELL Indicated')
                                    ###print(items_source_data)
                                    ###print("Exit Long")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (close_posistion_price - open_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ##profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print(portfolio_totals)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    ##print(buy_hold_return)
                                    #buy_hold_return_append.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_losing_trade_long.append(number_of_bars_in_each_loss_trade_long)
                                    
                                    closed_trades = closed_trades + 1
                                    ##print(closed_trades)
                                    
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_winning_trade_long.append(number_of_bars_in_each_winning_trade_long)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                  
                                    if(investment_revenue > 0):
                                        gross_profit_long.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_long.append(investment_revenue)
                                    
                                    average_trade_long.append(investment_revenue)
                                    
                                    closed_trades_long = closed_trades_long + 1
                                    ##print(closed_trades_long)
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
        
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(1)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    #print('-----------')
                                    break
                                else:
                                    place_holder = 0
                                    number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)  
                       
                        
                        elif(items_trade_alerts == "BUY"):
                            ###print(items_source_data)
                            #print("SELL Indicated")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
                            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_short.append(quantity_shares)
                            ###print('-----------')
                            #break
                            for items_trade_alerts, items_source_data, items_timestamps in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_short = number_of_bars_in_each_trade_short + 1
                                number_of_bars_in_each_winning_trade_short = number_of_bars_in_each_winning_trade_short + 1
                                number_of_bars_in_each_losing_trade_short = number_of_bars_in_each_losing_trade_short + 1
                                if(items_trade_alerts == "SELL" or items_timestamps == array1[len(array1)-1]):
                                    ###print(items_source_data)
                                    ###print("Exit Short")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (open_posistion_price - close_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ###profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    #buy_hold_return.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_losing_trade_short.append(number_of_bars_in_each_losing_trade_short)
                                        
                                    closed_trades = closed_trades + 1
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_winning_trade_short.append(number_of_bars_in_each_winning_trade_short)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    if(investment_revenue > 0):
                                        gross_profit_short.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_short.append(investment_revenue)
                                    closed_trades_short = closed_trades_short + 1
                                   
                                    
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(0)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    
                                    #print('-----------')
                                    
                                    break
                        
                            if(money < 0):
                                break
                    
                            
                        else:
                            ##print('-----------')
                            ##print(items_source_data)
                            ###print("HOLD")
                            place_holder = 0
                            number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                            ##print(number_of_bars_in_each_trade)
                            ###print('-----------')
                            ##print(gross_profit)
                        ##print(excess_returns)
                        ##print(r_minus_rf)
                
                ##print('yes')
                ##print(length_sell_lag)
                ##print(length_buy_lag)
                sum_investment_revenue_4 = sum(investment_revenue_append)
                
                if(sum_investment_revenue_4 == 0):
                    continue
                
                if(length_sell_lag != -1 or length_buy_lag != -1):
                    
                    percentage_movements = pd.DataFrame(percentage_gain_append)
                    ##print(percentage_movements)
                    percentage_ticker_df = pd.DataFrame(percentage_gain_tickers)
                    dollar_ticker_df = pd.DataFrame(investment_revenue_append)
                    portfolio_total_df = pd.DataFrame(portfolio_total_append)
                    ##print(percentage_ticker_df)
                    #deviation_df = pd.DataFrame(deviation_results)
                    ##print(deviation_df)
                    action_object_df = pd.DataFrame(pos_object)
                    pos_time_df = pd.DataFrame(pos_time)
                    
                    
                    
                    pg_concat = pd.concat([percentage_movements,dollar_ticker_df,portfolio_total_df,percentage_ticker_df,action_object_df,pos_time_df], axis=1)
                    pg_concat.columns = ["Percentage","Dollar","Portfolio Total","Ticker","Position Object","Position Time"]
                    
                    ####print('-----------------')
                    ####print('-----------------')
                        
                    ####print(percentage_gain_append)
                    ##print(deviation_df)
                    ##print(pg_concat)
                    pg_concat.to_csv('one_day_4_percentage_movements.csv')
                        
                    #print('ONE DAY SIMMUALTION COMPLETE')
        
            return(sum_investment_revenue_4)    
            
        sum_investment_revenue_4 = backtest_max_dev()      
        
        
        
        
        
        def backtest_trend_perc():
            
            csv_ticker_list = pd.read_csv('ticker_parameter_grades.csv')
            ##print(perc_chance_param)
            
            ticker_list = csv_ticker_list['Ticker'].to_numpy().tolist()
            
            #print(ticker_list)
            
            starting_money = last_equity
        
        
            
            
            
            action_object = csv_ticker_list['Trend Percentage'].to_numpy().tolist()
            
             
            
            
            
            
            percentage_gain_append = []
            percentage_gain_tickers = []
            deviation_results = []
            pos_object = []
            pos_time = []
            investment_revenue_append = []
            portfolio_total_append = []
            
            
            for ticker, items_action_object in zip(ticker_list, action_object):
                
                money = starting_money
                
                
                
                src_open = pd.read_csv('PMAX_'+ticker+'_alert_source_tradingview_data.csv')
                #src_open.iloc[200:]
                ##print(src_open)
                
                
                
                
                #shit = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 06:30:00-07:00")]
                ##print(shit.index[0])
                
                #dumb = src_open['Timestamp'][src_open['Timestamp'].str.contains("2022-08-22 07:00:00-07:00")]
                ##print(dumb.index[0])
                
                ##print('---------------------')
                ##print(src_open['Timestamp'][shit.index[0]:dumb.index[0]])
                
                ##print(ticker)
                array1 = []
                for stuff in src_open['Timestamp']:
                    if(stuff[0:10] == time_string_initial_data):
                        array1.append(stuff)
                        ##print(stuff)
                
                ##print(array1[0])
                
                index = src_open[src_open['Timestamp'] == array1[0]].index[0]
                ##print("Index Number for starting point:", index)
            
                end_index = src_open[src_open['Timestamp'] == array1[len(array1)-1]].index[0]
                ##print("End Index Number for starting point:", end_index)
                
                ##print(len(array1)-1)
                ##print(array1[len(array1)-1])
                
                ##index = 0
                
                ##print(src_open[index:])
                
            
                
                closed_trades = 0
                number_of_bars_in_each_trade = 0
                number_of_bars_in_each_winning_trade = 0
                number_of_bars_in_each_loss_trade = 0
                
                closed_trades_long = 0
                number_of_bars_in_each_trade_long = 0
                number_of_bars_in_each_winning_trade_long = 0
                number_of_bars_in_each_loss_trade_long = 0
                
                closed_trades_short = 0
                number_of_bars_in_each_trade_short = 0
                number_of_bars_in_each_winning_trade_short = 0
                number_of_bars_in_each_losing_trade_short = 0
                
                gross_profit = []
                gross_loss = []
                portfolio_totals = []
                buy_hold_return_append = []
                excess_returns = []
                percentage_profit_or_loss = []
                negative_assets = []
                max_contracts_held = []
                #closed_trades = []
                positive_assets = []
                average_trade = []
                average_of_bars_in_each_trade = [0]
                average_of_bars_in_winning_trade = []
                average_of_bars_in_losing_trade = []
                
                gross_profit_long = []
                gross_loss_long = []
                max_contracts_held_long = []
                #closed_trades_long = []
                average_trade_long = []
                average_of_bars_in_each_trade_long = [0]
                average_of_bars_in_winning_trade_long = []
                average_of_bars_in_losing_trade_long = []
                
                gross_profit_short = []
                gross_loss_short = []
                max_contracts_held_short = []
                #closed_trades_short = []
                average_trade_short = []
                average_of_bars_in_each_trade_short = [0]
                average_of_bars_in_winning_trade_short = []
                average_of_bars_in_losing_trade_short = []
                
                
                src_open['Trade_Alerts'][index:].to_numpy().tolist
                all_lag = np.array(src_open['Trade_Alerts'][index:])
                sell_lag_index = np.where(all_lag == 'SELL')[0]
                buy_lag_index = np.where(all_lag == 'BUY')[0]
             
                length_sell_lag = len(sell_lag_index)-1                                        
                ##print(length_sell_lag)
                length_buy_lag = len(buy_lag_index)-1  
                
                
                if(items_action_object <= 0):
                    #print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    ##print('Ticker:', ticker)
                    
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        ##print(items_source_data)
                        ##print(items_trade_alerts)
                        
                        
                        if(items_trade_alerts == 'BUY'):
                            #print('BUY Indicated')
                            ###print(items_source_data)
                            ###print("Enter LONG")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #quantity_shares_offset = (money/open_posistion_price) - quantity_shares
                            ##print("quantity_shares_offset", quantity_shares_offset)              
                            #remainder_money = quantity_shares_offset*open_posistion_price
                            ##print("remainder_money", remainder_money)
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_long.append(quantity_shares)
                            ###print('-----------')
                            #break
                            
                            for items_source_data, items_trade_alerts, items_timestamps in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                number_of_bars_in_each_winning_trade_long = number_of_bars_in_each_winning_trade_long + 1
                                number_of_bars_in_each_loss_trade_long = number_of_bars_in_each_loss_trade_long + 1
                                
                                if(items_trade_alerts == "SELL" or items_timestamps == array1[len(array1)-1]):
                                    ###print('SELL Indicated')
                                    ###print(items_source_data)
                                    ###print("Exit Long")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (close_posistion_price - open_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ##profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print(portfolio_totals)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    ##print(buy_hold_return)
                                    #buy_hold_return_append.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_losing_trade_long.append(number_of_bars_in_each_loss_trade_long)
                                    
                                    closed_trades = closed_trades + 1
                                    ##print(closed_trades)
                                    
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_winning_trade_long.append(number_of_bars_in_each_winning_trade_long)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                  
                                    if(investment_revenue > 0):
                                        gross_profit_long.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_long.append(investment_revenue)
                                    
                                    average_trade_long.append(investment_revenue)
                                    
                                    closed_trades_long = closed_trades_long + 1
                                    ##print(closed_trades_long)
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
        
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(1)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    #print('-----------')
                                    break
                                else:
                                    place_holder = 0
                                    number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)   
                       
                        
                        elif(items_trade_alerts == "SELL"):
                            ###print(items_source_data)
                            #print("SELL Indicated")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
                            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_short.append(quantity_shares)
                            ###print('-----------')
                            #break
                            for items_trade_alerts, items_source_data, items_timestamps in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_short = number_of_bars_in_each_trade_short + 1
                                number_of_bars_in_each_winning_trade_short = number_of_bars_in_each_winning_trade_short + 1
                                number_of_bars_in_each_losing_trade_short = number_of_bars_in_each_losing_trade_short + 1
                                if(items_trade_alerts == "BUY" or items_timestamps == array1[len(array1)-1]):
                                    ###print(items_source_data)
                                    ###print("Exit Short")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (open_posistion_price - close_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ###profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    #buy_hold_return.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_losing_trade_short.append(number_of_bars_in_each_losing_trade_short)
                                        
                                    closed_trades = closed_trades + 1
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_winning_trade_short.append(number_of_bars_in_each_winning_trade_short)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    if(investment_revenue > 0):
                                        gross_profit_short.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_short.append(investment_revenue)
                                    closed_trades_short = closed_trades_short + 1
                                   
                                    
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(0)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    
                                    #print('-----------')
                                    
                                    break
                        
                            if(money < 0):
                                break
                    
                            
                        else:
                            ##print('-----------')
                            ##print(items_source_data)
                            ###print("HOLD")
                            place_holder = 0
                            number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                            ##print(number_of_bars_in_each_trade)
                            ###print('-----------')
                            ##print(gross_profit)
                        ##print(excess_returns)
                        ##print(r_minus_rf)
                        
                        
                        
                        
                if(items_action_object > 0):
                    #print(ticker)
                    stock_dev_money = starting_money/len(ticker_list)
                    for items_source_data, items_trade_alerts in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:]):
                        index = index + 1
                        ##print(items_source_data)
                        ##print(items_trade_alerts)
                        
                    
                            
                        if(items_trade_alerts == 'SELL'):
                            #print('BUY Indicated')
                            ###print(items_source_data)
                            ###print("Enter LONG")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #quantity_shares_offset = (money/open_posistion_price) - quantity_shares
                            ##print("quantity_shares_offset", quantity_shares_offset)              
                            #remainder_money = quantity_shares_offset*open_posistion_price
                            ##print("remainder_money", remainder_money)
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_long.append(quantity_shares)
                            ###print('-----------')
                            #break
                            
                            for items_source_data, items_trade_alerts, items_timestamps in zip(src_open['Source_Data'][index:], src_open['Trade_Alerts'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                number_of_bars_in_each_winning_trade_long = number_of_bars_in_each_winning_trade_long + 1
                                number_of_bars_in_each_loss_trade_long = number_of_bars_in_each_loss_trade_long + 1
                                
                                if(items_trade_alerts == "BUY" or items_timestamps == array1[len(array1)-1]):
                                    ###print('SELL Indicated')
                                    ###print(items_source_data)
                                    ###print("Exit Long")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (close_posistion_price - open_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ##profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print(portfolio_totals)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    ##print(buy_hold_return)
                                    #buy_hold_return_append.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_losing_trade_long.append(number_of_bars_in_each_loss_trade_long)
                                    
                                    closed_trades = closed_trades + 1
                                    ##print(closed_trades)
                                    
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)
                                        average_of_bars_in_winning_trade_long.append(number_of_bars_in_each_winning_trade_long)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                  
                                    if(investment_revenue > 0):
                                        gross_profit_long.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_long.append(investment_revenue)
                                    
                                    average_trade_long.append(investment_revenue)
                                    
                                    closed_trades_long = closed_trades_long + 1
                                    ##print(closed_trades_long)
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
        
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(1)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    #print('-----------')
                                    break
                                else:
                                    place_holder = 0
                                    number_of_bars_in_each_trade_long = number_of_bars_in_each_trade_long + 1
                                    average_of_bars_in_each_trade_long.append(number_of_bars_in_each_trade_long)  
                       
                        
                        elif(items_trade_alerts == "BUY"):
                            ###print(items_source_data)
                            #print("SELL Indicated")
                            place_holder = 0
                            #break
                            ###print('-----------')
                            ###print("Money:", money)
                            ###print("Posistion:", items_trade_alerts)
                            open_posistion_price =  items_source_data
                            #print("open_posistion_price:", open_posistion_price)
                            
                            
                            quantity_shares = (int(stock_dev_money/open_posistion_price))
                            #print("Shares", quantity_shares)        
                            
                            investment_amount = (quantity_shares * open_posistion_price)
                            ##print("investment_amount", investment_amount)
                            amount_left = stock_dev_money - investment_amount
                            ##print("amount_left", amount_left)
                            
                            
                            
                            
                            
                            #money = money+remainder_money
                            ##print("Money:", money)
                            
                            max_contracts_held.append(quantity_shares)
                            max_contracts_held_short.append(quantity_shares)
                            ###print('-----------')
                            #break
                            for items_trade_alerts, items_source_data, items_timestamps in zip(src_open['Trade_Alerts'][index:], src_open['Source_Data'][index:], src_open['Timestamp'][index:]):
                                number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                                number_of_bars_in_each_winning_trade = number_of_bars_in_each_winning_trade + 1
                                ##print(number_of_bars_in_each_winning_trade)
                                ##print(items_source_data)
                                number_of_bars_in_each_loss_trade = number_of_bars_in_each_loss_trade + 1
                                
                                number_of_bars_in_each_trade_short = number_of_bars_in_each_trade_short + 1
                                number_of_bars_in_each_winning_trade_short = number_of_bars_in_each_winning_trade_short + 1
                                number_of_bars_in_each_losing_trade_short = number_of_bars_in_each_losing_trade_short + 1
                                if(items_trade_alerts == "SELL" or items_timestamps == array1[len(array1)-1]):
                                    ###print(items_source_data)
                                    ###print("Exit Short")
                                    place_holder = 0
                                    ###print('-----------')
                                    close_posistion_price = items_source_data
                                    #print("Close Posistion Price:", close_posistion_price)
                                    percentage_profit_loss = (open_posistion_price - close_posistion_price)/open_posistion_price
                                    #print("% Profit/Loss:", percentage_profit_loss)
                                    percentage_profit_or_loss.append(percentage_profit_loss)
                                    ###profit_loss = (close_posistion_price * quantity_shares)
                                    profit_loss = (investment_amount * (1+percentage_profit_loss))
                                    #print("Profit/Loss:", profit_loss)
                                    investment_revenue = profit_loss - (investment_amount)
                                    #print("Investment Revenue:", investment_revenue)
                                    investment_revenue_append.append(investment_revenue)
                                    excess_return = percentage_profit_loss - 0.0238
                                    excess_returns.append(excess_return)
                                    money = profit_loss+amount_left
                                    portfolio_total_append.append(money)
                                    if(investment_revenue > 0):
                                        gross_profit.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss.append(investment_revenue)
                                    portfolio_totals.append(profit_loss)
                                    ##print('-----------')
                                    buy_hold_return = [((close_posistion_price - open_posistion_price)/open_posistion_price)*100]
                                    #buy_hold_return.append(buy_hold_return)
                                    if(percentage_profit_loss < 0):
                                        negative_assets.append((percentage_profit_loss-0.0238)**2)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_losing_trade.append(number_of_bars_in_each_loss_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_losing_trade_short.append(number_of_bars_in_each_losing_trade_short)
                                        
                                    closed_trades = closed_trades + 1
                                    if(percentage_profit_loss > 0):
                                        positive_assets.append(percentage_profit_loss)
                                        average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                                        average_of_bars_in_winning_trade.append(number_of_bars_in_each_winning_trade)
                                        
                                        average_of_bars_in_each_trade_short.append(number_of_bars_in_each_trade_short)
                                        average_of_bars_in_winning_trade_short.append(number_of_bars_in_each_winning_trade_short)
                                        
                                    average_trade.append(investment_revenue)
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    if(investment_revenue > 0):
                                        gross_profit_short.append(investment_revenue)
                                    elif(investment_revenue < 0):
                                        gross_loss_short.append(investment_revenue)
                                    closed_trades_short = closed_trades_short + 1
                                   
                                    
                                    
                                    ##money = money + amount_left
                                    
                                    #print("Portfolio Value:", money)
                                    
                                    stock_dev_money = percentage_profit_loss*stock_dev_money+stock_dev_money
                                    
                                    deviation_results.append((stock_dev_money))
                                    percentage_gain_append.append(percentage_profit_loss)
                                    percentage_gain_tickers.append(ticker)
                                    pos_object.append(0)
                                    
                                    pos_time.append(src_open['Timestamp'][index])
                                    ##print(position_time)
                                    
                                    #print('-----------')
                                    
                                    break
                        
                            if(money < 0):
                                break
                    
                            
                        else:
                            ##print('-----------')
                            ##print(items_source_data)
                            ###print("HOLD")
                            place_holder = 0
                            number_of_bars_in_each_trade = number_of_bars_in_each_trade + 1
                            average_of_bars_in_each_trade.append(number_of_bars_in_each_trade)
                            ##print(number_of_bars_in_each_trade)
                            ###print('-----------')
                            ##print(gross_profit)
                        ##print(excess_returns)
                        ##print(r_minus_rf)
                
                ##print('yes')
                ##print(length_sell_lag)
                ##print(length_buy_lag)
                sum_investment_revenue_5 = sum(investment_revenue_append)
                
                if(sum_investment_revenue_5 == 0):
                    continue
                
                if(length_sell_lag != -1 or length_buy_lag != -1):
                    
                    percentage_movements = pd.DataFrame(percentage_gain_append)
                    ##print(percentage_movements)
                    percentage_ticker_df = pd.DataFrame(percentage_gain_tickers)
                    dollar_ticker_df = pd.DataFrame(investment_revenue_append)
                    portfolio_total_df = pd.DataFrame(portfolio_total_append)
                    ##print(percentage_ticker_df)
                    #deviation_df = pd.DataFrame(deviation_results)
                    ##print(deviation_df)
                    action_object_df = pd.DataFrame(pos_object)
                    pos_time_df = pd.DataFrame(pos_time)
                    
                    
                    
                    pg_concat = pd.concat([percentage_movements,dollar_ticker_df,portfolio_total_df,percentage_ticker_df,action_object_df,pos_time_df], axis=1)
                    pg_concat.columns = ["Percentage","Dollar","Portfolio Total","Ticker","Position Object","Position Time"]
                    
                    ####print('-----------------')
                    ####print('-----------------')
                        
                    ####print(percentage_gain_append)
                    ##print(deviation_df)
                    ##print(pg_concat)
                    pg_concat.to_csv('one_day_5_percentage_movements.csv')
                        
                    #print('ONE DAY SIMMUALTION COMPLETE')
                   
            return(sum_investment_revenue_5)    
            
        sum_investment_revenue_5 = backtest_trend_perc()  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def summary_analysis_of_sims(sum_investment_revenue_2,sum_investment_revenue_1,sum_investment_revenue_0,sum_investment_revenue_4,sum_investment_revenue_5):    
        
            #print("sum_investment_revenue_2:", sum_investment_revenue_2)
            #print("sum_investment_revenue_1:", sum_investment_revenue_1)
            #print("sum_investment_revenue_0:", sum_investment_revenue_0)
            ##print("sum_investment_revenue_3:", sum_investment_revenue_3)
            #print("sum_investment_revenue_4:", sum_investment_revenue_4)
            #print("sum_investment_revenue_5:", sum_investment_revenue_5)
            
            
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_2_percentage_movements.csv') != True):
                ir2_perc = sum_investment_revenue_2/last_equity
                #print("percentage_investment_revenue_2:", ir2_perc)
            else:
                ir2_perc = 0
                
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_1_percentage_movements.csv') != True):
                ir1_perc = sum_investment_revenue_1/last_equity
                #print("percentage_investment_revenue_1:", ir1_perc)
            else:
                ir1_perc = 0
                
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_0_percentage_movements.csv') != True):
                ir0_perc = sum_investment_revenue_0/last_equity
                #print("percentage_investment_revenue_0:", ir0_perc)
            else:
                ir0_perc = 0
                
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_4_percentage_movements.csv') != True):
                ir4_perc = sum_investment_revenue_4/last_equity
                #print("percentage_investment_revenue_4:", ir4_perc)
            else:
                ir4_perc = 0
                
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_5_percentage_movements.csv') != True):
                ir5_perc = sum_investment_revenue_5/last_equity
                #print("percentage_investment_revenue_5:", ir5_perc)
            else:
                ir5_perc = 0
            
            
            
            sum_summary_array = [sum_investment_revenue_2,sum_investment_revenue_1,sum_investment_revenue_0,sum_investment_revenue_4,sum_investment_revenue_5]
            perc_summary_array = [ir2_perc,ir1_perc,ir0_perc,ir4_perc,ir5_perc]
            
            df_sum_summary_array = pd.DataFrame(sum_summary_array)
            df_perc_df = pd.DataFrame(perc_summary_array)
            df_summary_combined = pd.concat([df_sum_summary_array,df_perc_df], axis = 1)
            df_summary_combined.columns = ['Sum of Dollar Profit','Percentage Profit']
            df_summary_combined.index = ['Setting 2','Setting 1','Setting 0','Setting 4','Setting 5']
            #print(df_summary_combined)
            
            df_summary_combined.to_csv('intraday_simmulation_summary_analysis.csv')
        
        summary_analysis_of_sims(sum_investment_revenue_2,sum_investment_revenue_1,sum_investment_revenue_0,sum_investment_revenue_4,sum_investment_revenue_5)
        
        print("CURRENT DAY SIMMUALTOR COMPLETE")
        
        break
        
        
        
    except:
        print("No Internet Connection, Attempting Reconnection... - Current Day Simmulator")
        time.sleep(0.5)
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    