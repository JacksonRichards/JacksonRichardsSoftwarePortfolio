
import pandas as pd
import numpy as np
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import warnings
from datetime import date






def Algorithm():
    
    warnings.filterwarnings('ignore')

    alpaca_keys = pd.read_csv(r"C:\Users\jacks\Desktop\Simmulation\alpaca_api_information.csv")


    data_client = StockHistoricalDataClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0])
    trading_client = TradingClient(alpaca_keys['API KEY'][0], alpaca_keys['API SECRET KEY'][0], paper=alpaca_keys['Portfolio Type'][0])
    
    sim_date = pd.read_csv("sim_date.csv")


    today_initial_data = date.today()
    y = today_initial_data.strftime("%Y-%m-%d")
    LA = 'America/los_angeles'
    end=pd.Timestamp(y, tz=LA)    
    time_string_initial_data = sim_date['Date'][0]

    start_data_global = time_string_initial_data

    #----------------------------------------------------------------
    pd.set_option('display.max_columns', 10000)
    ticker_grades_csv = pd.read_csv("stock_beg_performance.csv")[0:10]
    
    ###NOTE: CAN INSERT OTHER ALOGIRTHMS HERE OR LINK IT FROM ANOTHER .PY FILE!!!!
    #----------------------------------------------------------------

    
    ticker_csv_data = ticker_grades_csv['Ticker'].to_numpy().tolist()
    #print("Ticker List Today:", ticker_csv_data)
    percentage_csv_data = ticker_grades_csv['Percentage'].to_numpy().tolist()

    tickers = ticker_csv_data
    percentages = percentage_csv_data
    
    top_performers = []
    for ticker_top_performers, percentage_items in zip(tickers, percentages):
        top_performers.append(ticker_top_performers)
        


    time_list = [' 06:31:00-08:00',' 06:32:00-08:00',' 06:33:00-08:00',' 06:34:00-08:00',' 06:35:00-08:00',
                 ' 06:36:00-08:00',' 06:37:00-08:00',' 06:38:00-08:00',' 06:39:00-08:00',' 06:40:00-08:00',
                 ' 06:41:00-08:00',' 06:42:00-08:00',' 06:43:00-08:00',' 06:44:00-08:00',' 06:45:00-08:00',
                 ' 06:46:00-08:00',' 06:47:00-08:00',' 06:48:00-08:00',' 06:49:00-08:00',' 06:50:00-08:00',
                 ' 06:51:00-08:00',' 06:52:00-08:00',' 06:53:00-08:00',' 06:54:00-08:00',' 06:55:00-08:00',
                 ' 06:56:00-08:00',' 06:57:00-08:00',' 06:58:00-08:00',' 06:59:00-08:00',' 07:00:00-08:00',
                 ' 07:01:00-08:00',' 07:02:00-08:00',' 07:03:00-08:00',' 07:04:00-08:00',' 07:05:00-08:00',
                 ' 07:06:00-08:00',' 07:07:00-08:00',' 07:08:00-08:00',' 07:09:00-08:00',' 07:10:00-08:00',
                 ' 07:11:00-08:00',' 07:12:00-08:00',' 07:13:00-08:00',' 07:14:00-08:00',' 07:15:00-08:00',
                 ' 07:16:00-08:00',' 07:17:00-08:00',' 07:18:00-08:00',' 07:19:00-08:00',' 07:20:00-08:00',
                 ' 07:21:00-08:00',' 07:22:00-08:00',' 07:23:00-08:00',' 07:24:00-08:00',' 07:25:00-08:00',
                 ' 07:26:00-08:00',' 07:27:00-08:00',' 07:28:00-08:00',' 07:29:00-08:00',' 07:30:00-08:00',
                 ' 07:31:00-08:00',' 07:32:00-08:00',' 07:33:00-08:00',' 07:34:00-08:00',' 07:35:00-08:00',
                 ' 07:36:00-08:00',' 07:37:00-08:00',' 07:38:00-08:00',' 07:39:00-08:00',' 07:40:00-08:00',
                 ' 07:41:00-08:00',' 07:42:00-08:00',' 07:43:00-08:00',' 07:44:00-08:00',' 07:45:00-08:00',
                 ' 07:46:00-08:00',' 07:47:00-08:00',' 07:48:00-08:00',' 07:49:00-08:00',' 07:50:00-08:00',
                 ' 07:51:00-08:00',' 07:52:00-08:00',' 07:53:00-08:00',' 07:54:00-08:00',' 07:55:00-08:00',
                 ' 07:56:00-08:00',' 07:57:00-08:00',' 07:58:00-08:00',' 07:59:00-08:00',' 08:00:00-08:00',
                 ' 08:01:00-08:00',' 08:02:00-08:00',' 08:03:00-08:00',' 08:04:00-08:00',' 08:05:00-08:00',
                 ' 08:06:00-08:00',' 08:07:00-08:00',' 08:08:00-08:00',' 08:09:00-08:00',' 08:10:00-08:00',
                 ' 08:11:00-08:00',' 08:12:00-08:00',' 08:13:00-08:00',' 08:14:00-08:00',' 08:15:00-08:00',
                 ' 08:16:00-08:00',' 08:17:00-08:00',' 08:18:00-08:00',' 08:19:00-08:00',' 08:20:00-08:00',
                 ' 08:21:00-08:00',' 08:22:00-08:00',' 08:23:00-08:00',' 08:24:00-08:00',' 08:25:00-08:00',
                 ' 08:26:00-08:00',' 08:27:00-08:00',' 08:28:00-08:00',' 08:29:00-08:00',' 08:30:00-08:00',
                 ' 08:31:00-08:00',' 08:32:00-08:00',' 08:33:00-08:00',' 08:34:00-08:00',' 08:35:00-08:00',
                 ' 08:36:00-08:00',' 08:37:00-08:00',' 08:38:00-08:00',' 08:39:00-08:00',' 08:40:00-08:00',
                 ' 08:41:00-08:00',' 08:42:00-08:00',' 08:43:00-08:00',' 08:44:00-08:00',' 08:45:00-08:00',
                 ' 08:46:00-08:00',' 08:47:00-08:00',' 08:48:00-08:00',' 08:49:00-08:00',' 08:50:00-08:00',
                 ' 08:51:00-08:00',' 08:52:00-08:00',' 08:53:00-08:00',' 08:54:00-08:00',' 08:55:00-08:00',
                 ' 08:56:00-08:00',' 08:57:00-08:00',' 08:58:00-08:00',' 08:59:00-08:00',' 09:00:00-08:00',
                 ' 09:01:00-08:00',' 09:02:00-08:00',' 09:03:00-08:00',' 09:04:00-08:00',' 09:05:00-08:00',
                 ' 09:06:00-08:00',' 09:07:00-08:00',' 09:08:00-08:00',' 09:09:00-08:00',' 09:10:00-08:00',
                 ' 09:11:00-08:00',' 09:12:00-08:00',' 09:13:00-08:00',' 09:14:00-08:00',' 09:15:00-08:00',
                 ' 09:16:00-08:00',' 09:17:00-08:00',' 09:18:00-08:00',' 09:19:00-08:00',' 09:20:00-08:00',
                 ' 09:21:00-08:00',' 09:22:00-08:00',' 09:23:00-08:00',' 09:24:00-08:00',' 09:25:00-08:00',
                 ' 09:26:00-08:00',' 09:27:00-08:00',' 09:28:00-08:00',' 09:29:00-08:00',' 09:30:00-08:00',
                 ' 09:31:00-08:00',' 09:32:00-08:00',' 09:33:00-08:00',' 09:34:00-08:00',' 09:35:00-08:00',
                 ' 09:36:00-08:00',' 09:37:00-08:00',' 09:38:00-08:00',' 09:39:00-08:00',' 09:40:00-08:00',
                 ' 09:41:00-08:00',' 09:42:00-08:00',' 09:43:00-08:00',' 09:44:00-08:00',' 09:45:00-08:00',
                 ' 09:46:00-08:00',' 09:47:00-08:00',' 09:48:00-08:00',' 09:49:00-08:00',' 09:50:00-08:00',
                 ' 09:51:00-08:00',' 09:52:00-08:00',' 09:53:00-08:00',' 09:54:00-08:00',' 09:55:00-08:00',
                 ' 09:56:00-08:00',' 09:57:00-08:00',' 09:58:00-08:00',' 09:59:00-08:00',' 10:00:00-08:00',
                 ' 10:01:00-08:00',' 10:02:00-08:00',' 10:03:00-08:00',' 10:04:00-08:00',' 10:05:00-08:00',
                 ' 10:06:00-08:00',' 10:07:00-08:00',' 10:08:00-08:00',' 10:09:00-08:00',' 10:10:00-08:00',
                 ' 10:11:00-08:00',' 10:12:00-08:00',' 10:13:00-08:00',' 10:14:00-08:00',' 10:15:00-08:00',
                 ' 10:16:00-08:00',' 10:17:00-08:00',' 10:18:00-08:00',' 10:19:00-08:00',' 10:20:00-08:00',
                 ' 10:21:00-08:00',' 10:22:00-08:00',' 10:23:00-08:00',' 10:24:00-08:00',' 10:25:00-08:00',
                 ' 10:26:00-08:00',' 10:27:00-08:00',' 10:28:00-08:00',' 10:29:00-08:00',' 10:30:00-08:00',
                 ' 10:31:00-08:00',' 10:32:00-08:00',' 10:33:00-08:00',' 10:34:00-08:00',' 10:35:00-08:00',
                 ' 10:36:00-08:00',' 10:37:00-08:00',' 10:38:00-08:00',' 10:39:00-08:00',' 10:40:00-08:00',
                 ' 10:41:00-08:00',' 10:42:00-08:00',' 10:43:00-08:00',' 10:44:00-08:00',' 10:45:00-08:00',
                 ' 10:46:00-08:00',' 10:47:00-08:00',' 10:48:00-08:00',' 10:49:00-08:00',' 10:50:00-08:00',
                 ' 10:51:00-08:00',' 10:52:00-08:00',' 10:53:00-08:00',' 10:54:00-08:00',' 10:55:00-08:00',
                 ' 10:56:00-08:00',' 10:57:00-08:00',' 10:58:00-08:00',' 10:59:00-08:00',' 11:00:00-08:00',
                 ' 11:01:00-08:00',' 11:02:00-08:00',' 11:03:00-08:00',' 11:04:00-08:00',' 11:05:00-08:00',
                 ' 11:06:00-08:00',' 11:07:00-08:00',' 11:08:00-08:00',' 11:09:00-08:00',' 11:10:00-08:00',
                 ' 11:11:00-08:00',' 11:12:00-08:00',' 11:13:00-08:00',' 11:14:00-08:00',' 11:15:00-08:00',
                 ' 11:16:00-08:00',' 11:17:00-08:00',' 11:18:00-08:00',' 11:19:00-08:00',' 11:20:00-08:00',
                 ' 11:21:00-08:00',' 11:22:00-08:00',' 11:23:00-08:00',' 11:24:00-08:00',' 11:25:00-08:00',
                 ' 11:26:00-08:00',' 11:27:00-08:00',' 11:28:00-08:00',' 11:29:00-08:00',' 11:30:00-08:00',
                 ' 11:31:00-08:00',' 11:32:00-08:00',' 11:33:00-08:00',' 11:34:00-08:00',' 11:35:00-08:00',
                 ' 11:36:00-08:00',' 11:37:00-08:00',' 11:38:00-08:00',' 11:39:00-08:00',' 11:40:00-08:00',
                 ' 11:41:00-08:00',' 11:42:00-08:00',' 11:43:00-08:00',' 11:44:00-08:00',' 11:45:00-08:00',
                 ' 11:46:00-08:00',' 11:47:00-08:00',' 11:48:00-08:00',' 11:49:00-08:00',' 11:50:00-08:00',
                 ' 11:51:00-08:00',' 11:52:00-08:00',' 11:53:00-08:00',' 11:54:00-08:00',' 11:55:00-08:00',
                 ' 11:56:00-08:00',' 11:57:00-08:00',' 11:58:00-08:00',' 11:59:00-08:00',' 12:00:00-08:00',
                 ' 12:01:00-08:00',' 12:02:00-08:00',' 12:03:00-08:00',' 12:04:00-08:00',' 12:05:00-08:00',
                 ' 12:06:00-08:00',' 12:07:00-08:00',' 12:08:00-08:00',' 12:09:00-08:00',' 12:10:00-08:00',
                 ' 12:11:00-08:00',' 12:12:00-08:00',' 12:13:00-08:00',' 12:14:00-08:00',' 12:15:00-08:00',
                 ' 12:16:00-08:00',' 12:17:00-08:00',' 12:18:00-08:00',' 12:19:00-08:00',' 12:20:00-08:00',
                 ' 12:21:00-08:00',' 12:22:00-08:00',' 12:23:00-08:00',' 12:24:00-08:00',' 12:25:00-08:00',
                 ' 12:26:00-08:00',' 12:27:00-08:00',' 12:28:00-08:00',' 12:29:00-08:00',' 12:30:00-08:00',
                 ' 12:31:00-08:00',' 12:32:00-08:00',' 12:33:00-08:00',' 12:34:00-08:00',' 12:35:00-08:00',
                 ' 12:36:00-08:00',' 12:37:00-08:00',' 12:38:00-08:00',' 12:39:00-08:00',' 12:40:00-08:00',
                 ' 12:41:00-08:00',' 12:42:00-08:00',' 12:43:00-08:00',' 12:44:00-08:00',' 12:45:00-08:00',
                 ' 12:46:00-08:00',' 12:47:00-08:00',' 12:48:00-08:00',' 12:49:00-08:00',' 12:50:00-08:00',
                 ' 12:51:00-08:00',' 12:52:00-08:00',' 12:53:00-08:00',' 12:54:00-08:00',' 12:55:00-08:00',
                 ' 12:56:00-08:00',' 12:57:00-08:00',' 12:58:00-08:00',' 12:59:00-08:00']
                 
    
    portfolio_perc_minute_by_minute = []
    portfolio_time_minute_by_minute = []
    
    
    for time_items in time_list:
        
        percentage_gains = []
        ticker_time_minute_by_minute = []
        
        for ticker in top_performers:
            


            start_time = pd.to_datetime(start_data_global+' 06:31:00-08:00', utc=True)
            end_time = pd.to_datetime(start_data_global+time_items, utc=True)
           
            
            
            
            request_params = StockBarsRequest(
                    symbol_or_symbols=ticker,
                    timeframe=TimeFrame.Minute,
                    start=start_time,
                    end=end_time,
                    adjustment = 'split',
                    feed = 'sip'
                    )
            #print(request_params)
            
            
            try:
                minute_bars = data_client.get_stock_bars(request_params).df
                
            except:
                percentage_gain = 0
                percentage_gains.append(percentage_gain)
                continue


            minute_bars = minute_bars.reset_index()
            minute_bars = minute_bars.set_index('timestamp')
            minute_bars.drop(['symbol'], axis=1)
            minute_bars = minute_bars.tz_convert('America/Los_angeles')
            
            
            if(len(minute_bars) == 0): 
                continue
            else:
                percentage_gain = ((minute_bars['high'][len(minute_bars)-1] - minute_bars['close'][0])/minute_bars['close'][0])*100
                percentage_gains.append(percentage_gain)

                
                ticker_perc_df = pd.DataFrame([percentage_gain])   
                ticker_time_df = pd.DataFrame([time_items])  
                ticker_total_final = pd.concat([ticker_perc_df, ticker_time_df], axis = 1) 
                ticker_total_final.to_csv('individual_minute_by_minute_'+ticker+'.csv', mode='a', index=False, header=False)
                

        total_portfolio_gain = sum(percentage_gains)/len(top_performers)

        portfolio_perc_minute_by_minute.append(total_portfolio_gain)
        portfolio_time_minute_by_minute.append(time_items)
      

        
    port_perc_df = pd.DataFrame(portfolio_perc_minute_by_minute)   
    port_time_df = pd.DataFrame(portfolio_time_minute_by_minute)   
    port_total_final = pd.concat([port_perc_df, port_time_df], axis = 1) 
    port_total_final.columns = ['Percentage','Time']
    #print(port_total_final)
    port_total_final.to_csv('port_minute_by_minute.csv')
    

    
    tickers_data_df = pd.DataFrame(top_performers)
    percentage_gains_df = pd.DataFrame(percentage_gains)
    indiv_stocks_final = pd.concat([tickers_data_df, percentage_gains_df], axis = 1) 
    indiv_stocks_final.columns = ['Tickers','Percentage']
    indiv_stocks_final.to_csv('individual_percentage_gains.csv')   
    

    
    indiv_ticker_zero = pd.read_csv('individual_minute_by_minute_'+top_performers[0]+'.csv')
    indiv_ticker_one = pd.read_csv('individual_minute_by_minute_'+top_performers[1]+'.csv')
    indiv_ticker_two = pd.read_csv('individual_minute_by_minute_'+top_performers[2]+'.csv')
    indiv_ticker_three = pd.read_csv('individual_minute_by_minute_'+top_performers[3]+'.csv')
    indiv_ticker_four = pd.read_csv('individual_minute_by_minute_'+top_performers[4]+'.csv')
    indiv_ticker_five = pd.read_csv('individual_minute_by_minute_'+top_performers[5]+'.csv')
    indiv_ticker_six = pd.read_csv('individual_minute_by_minute_'+top_performers[6]+'.csv')
    indiv_ticker_seven = pd.read_csv('individual_minute_by_minute_'+top_performers[7]+'.csv')
    indiv_ticker_eight = pd.read_csv('individual_minute_by_minute_'+top_performers[8]+'.csv')
    indiv_ticker_nine = pd.read_csv('individual_minute_by_minute_'+top_performers[9]+'.csv')
    
    final_concat_indiv_tickers = pd.concat([port_time_df,indiv_ticker_zero[indiv_ticker_zero.columns[0]],indiv_ticker_one[indiv_ticker_one.columns[0]],indiv_ticker_two[indiv_ticker_two.columns[0]],indiv_ticker_three[indiv_ticker_three.columns[0]],indiv_ticker_four[indiv_ticker_four.columns[0]],indiv_ticker_five[indiv_ticker_five.columns[0]],
                                            indiv_ticker_six[indiv_ticker_six.columns[0]],indiv_ticker_seven[indiv_ticker_seven.columns[0]],indiv_ticker_eight[indiv_ticker_eight.columns[0]],indiv_ticker_nine[indiv_ticker_nine.columns[0]]], axis=1)
    final_concat_indiv_tickers.columns = ['Time',str(top_performers[0]),str(top_performers[1]),str(top_performers[2]),str(top_performers[3]),str(top_performers[4]),str(top_performers[5]),str(top_performers[6]),str(top_performers[7]),str(top_performers[8]),str(top_performers[9])]
    final_concat_indiv_tickers.to_csv('final_individual_tickers_by_minute.csv')
    
    
    max_ticker_0 = max(final_concat_indiv_tickers[str(top_performers[0])])
    max_ticker_1 = max(final_concat_indiv_tickers[str(top_performers[1])])
    max_ticker_2 = max(final_concat_indiv_tickers[str(top_performers[2])])
    max_ticker_3 = max(final_concat_indiv_tickers[str(top_performers[3])])
    max_ticker_4 = max(final_concat_indiv_tickers[str(top_performers[4])])
    max_ticker_5 = max(final_concat_indiv_tickers[str(top_performers[5])])
    max_ticker_6 = max(final_concat_indiv_tickers[str(top_performers[6])])
    max_ticker_7 = max(final_concat_indiv_tickers[str(top_performers[7])])
    max_ticker_8 = max(final_concat_indiv_tickers[str(top_performers[8])])
    max_ticker_9 = max(final_concat_indiv_tickers[str(top_performers[9])])
    
    
    max_df0 = pd.DataFrame([max_ticker_0])
    max_df1 = pd.DataFrame([max_ticker_1])
    max_df2 = pd.DataFrame([max_ticker_2])
    max_df3 = pd.DataFrame([max_ticker_3])
    max_df4 = pd.DataFrame([max_ticker_4])
    max_df5 = pd.DataFrame([max_ticker_5])
    max_df6 = pd.DataFrame([max_ticker_6])
    max_df7 = pd.DataFrame([max_ticker_7])
    max_df8 = pd.DataFrame([max_ticker_8])
    max_df9 = pd.DataFrame([max_ticker_9])
    
    max_concat = pd.concat([max_df0,max_df1,max_df2,max_df3,max_df4,max_df5,max_df6,max_df7,max_df8,max_df9])
    max_concat.index = [str(top_performers[0]),str(top_performers[1]),str(top_performers[2]),str(top_performers[3]),str(top_performers[4]),str(top_performers[5]),str(top_performers[6]),str(top_performers[7]),str(top_performers[8]),str(top_performers[9])]
    max_concat.to_csv('individual_tickers_max_revenue.csv')

#Algorithm()








