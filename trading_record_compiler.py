

import pandas as pd
import numpy as np
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from datetime import datetime
from statistics import mean

def trading_record_compiler():
    
    print("TRADING RECORDS COMPILER COMMENCING")
    
    now = datetime.now()
    current_date = now.strftime('%m/%d/%Y')
    #print("Current Date:", current_date)
    
    
    old_overall_records = pd.read_csv('overall_records.csv')
    #print(old_overall_records.columns)
    
    
    old_overall_records_date = old_overall_records['Date']
    old_overall_records_date.to_numpy().tolist()
    
    if(old_overall_records_date[len(old_overall_records_date)-1] == current_date):
        print("RECORDS ALREADY RECORDED")
        return()
    else:
        
        
    
        alpaca_keys = pd.read_csv('alpaca_api_information.csv')
        
        #paper_tf = pd.read_csv('paper_true_false.csv')
        
        overall_records = pd.read_csv('overall_records.csv')
        #print(overall_records)
    
        # keys required for stock historical data client
        data_client = StockHistoricalDataClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0])
        trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])
        
        
        
        date_append = []
        portfolio_start_append = []
        portfolio_end_append = []
        dollar_change_append = []
        percentage_change_append = []
        total_portfolio_value_dollar_append = []
        total_portfolio_perc_append = []
        
        made_money_append = []
        stocks_trained_append = []
        total_closed_trades_avg_append = []
        prediction_number_avg_append = []
        storage_average_append = []
        
        
        now = datetime.now()
        current_date = now.strftime('%m/%d/%Y')
        #print("Current Date:", current_date)
        date_append.append(current_date)
        
        account = trading_client.get_account()
        
        portfolio_start = account.last_equity
        #print("Portfolio Start:", portfolio_start)
        portfolio_start_append.append(portfolio_start)
        portfolio_end = account.equity
        #print("Portfolio End:", portfolio_end)
        portfolio_end_append.append(portfolio_end)
        
        dollar_change = float(portfolio_end) - float(portfolio_start)
        #print("Dollar Change:", dollar_change)
        dollar_change_append.append(dollar_change)
        
        percentage_change = float(dollar_change)/float(portfolio_start)
        #print("Percentage Change:", percentage_change)
        percentage_change_append.append(percentage_change)
        
        overall_records_list = overall_records['total_portfolio_value_dollar'].to_numpy().tolist()
        #print(overall_records_list)
        prev_port_value = overall_records_list[len(overall_records_list)-2]
        #print(prev_port_value)
        total_portfolio_value_dollar = (float(prev_port_value)*float(percentage_change))+float(prev_port_value)
        #print("Total Portfolio Dollar:", total_portfolio_value_dollar)
        total_portfolio_value_dollar_append.append(total_portfolio_value_dollar)
        total_portfolio_percentage = (total_portfolio_value_dollar-float(portfolio_start))/float(portfolio_start)
        #print("Total Portfolio Percentage:", total_portfolio_percentage)
        total_portfolio_perc_append.append(total_portfolio_percentage)
        
        
        if(percentage_change >= 0):
            made_money = 1
            #print("Made Money:", made_money)
            made_money_append.append(made_money)
        else:
            made_money = 0
            #print("Made Money:", made_money)
            made_money_append.append(made_money)
         
        stocks_trained = 18
        #print("Stocks Trained:", stocks_trained)
        stocks_trained_append.append(stocks_trained)
        #print(stocks_trained_append)
            

        
        
        
        
        

        
        ticker_parameter_grades = pd.read_csv('ticker_parameter_grades.csv')
        total_closed_trades_avg = mean(ticker_parameter_grades['Number of Closed Trades'].to_numpy().tolist())
        #print("Total Closed Trades:", total_closed_trades_avg)
        total_closed_trades_avg_append.append(total_closed_trades_avg)
        prediction_number_avg = mean(ticker_parameter_grades['Total Points'].to_numpy().tolist())
        #print("Prediction Number:", prediction_number_avg)
        prediction_number_avg_append.append(prediction_number_avg)
        
        storage_average = 6400
        storage_average_append.append(storage_average)
        
        
        date_df = pd.DataFrame(date_append)
        portfolio_start_df = pd.DataFrame(portfolio_start_append)
        #print(portfolio_start_df)
        portfolio_end_df = pd.DataFrame(portfolio_end_append)
        #print(portfolio_end_df)
        dollar_change_df = pd.DataFrame(dollar_change_append)
        percentage_change_df = pd.DataFrame(percentage_change_append)
        
        total_portfolio_value_dollar_df = pd.DataFrame(total_portfolio_value_dollar_append)
        total_portfolio_percentage_df = pd.DataFrame(total_portfolio_perc_append)
        
        made_money_append = pd.DataFrame(made_money_append)
        stocks_trained_append = pd.DataFrame(stocks_trained_append)
        

        

        total_closed_trades_avg_append = pd.DataFrame(total_closed_trades_avg_append)
        prediction_number_avg_append = pd.DataFrame(prediction_number_avg_append)
        storage_average_df = pd.DataFrame(storage_average_append)
        
        final_concat = pd.concat([date_df,portfolio_start_df,portfolio_end_df,dollar_change_df,percentage_change_df,total_portfolio_value_dollar_df,
                                  total_portfolio_percentage_df,made_money_append,stocks_trained_append,
                                  total_closed_trades_avg_append,prediction_number_avg_append,storage_average_df], axis = 1) 
        
        final_concat.columns = ['Date','Portfolio_Start','Portfolio_End','Dollar_Change','Percentage_Change','total_portfolio_value_dollar',
                                'total_portfolio_perc','gain_loss','Number_Stocks_Trained','Average_Closed_Trades - BT',
                                'Predictive_Model_Average','Storage_Average']
        
        pd.set_option('display.max_columns', 10000)
        
        #print(final_concat)
        
        prev_overall_records = pd.read_csv('overall_records.csv')
        
        
        #print(prev_overall_records)
        
        overall_concat = pd.concat([prev_overall_records,final_concat], axis = 0)
        
        #print(overall_concat)
        
        overall_concat.to_csv('overall_records.csv')
        
        overall_concat = pd.read_csv('overall_records.csv')
        
        overall_concat.drop(overall_concat.filter(regex="Unname"),axis=1, inplace=True)
        ##del overall_concat[overall_concat.columns[0]]
        
        overall_concat.to_csv('overall_records.csv', index=False)
        
    print("TRADING RECORDS COMPILER COMPLETE")
        
    return()
    
trading_record_compiler()











    
    
    