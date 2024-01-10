

import pandas as pd
import numpy as np
import schedule
import time



def parameter_autofiller():
    
    print("PARAMETER AUTOFILLER COMMENCING")
    
    ticker_exchange_csv_data = pd.read_csv('ticker_list_today.csv')
    #print(ticker_exchange_csv_data)
    
    ticker_csv_data = ticker_exchange_csv_data['Tickers'].to_numpy().tolist()
    #print("Ticker List:", ticker_csv_data)
    
    exchange_csv_data = ticker_exchange_csv_data['Exchange'].to_numpy().tolist()
    #print("Exchanges:", exchange_csv_data)
    
    
    
    
    #ticker_csv_data = pd.read_csv('ticker_list_today.csv')
    #print(ticker_csv_data)

    #ticker_csv_data = ticker_csv_data['Tickers'].to_numpy().tolist()
    #print(ticker_csv_data)
    
    #exchange_csv_data = ticker_csv_data['Exchange'].to_numpy().tolist()
    #print(exchange_csv_data)
    
    
    
    
    
    

    ##tickers = ['MSFT','NVDA']
    tickers = ticker_csv_data
    exchanges = exchange_csv_data
    
    
    Multiplier_ATR_arrays = []
    Length_Tillson_arrays = []
    T3a1_Tillson_Volume_arrays = []
    Period_ATR_arrays = []
    rsi_length_arrays = []
    letter_grade_append = []
    net_profit = []
    ts = []
    se = []
    stop_loss_append = []
    number_of_trades_append = []
    percentage_profitable_append = []
    percentage_profitable_long_append = []
    percentage_profitable_short_append = []
    trend_percentage_append = []
    max_deviation_append = []
    max_drawdown_append = []
    maxdrawdown_netprofit_ratio_append = []
    win_loss_ratio_append = []
    bhr_append = []
    stdev_append = []
    net_profit_long = []
    average_trade_long = []
    for ticker, exchange in zip(tickers, exchanges):
    
        
    
        csv = 'training_data_compiled_'+ticker+'.csv'
        
        pd.set_option('display.max_columns', 6)
        data = pd.read_csv(csv)[0:]
        ####print("Ticker Symbol:", ticker) 
        
        #print(data['Pmax_Letter_Grade'])
        
        #print('------------------------------------------------')
        
        #data = data.set_index('Pmax_Letter_Grade')   
        #print(data)
        #print('---------------------------------------------------')
        data_one = data.drop(data[data.PMax_Letter_Grade != 'AAA'].index)
        #print(data_one)
        if(len(data_one) == 0):
            data_one = data.drop(data[data.PMax_Letter_Grade != 'AA'].index)
            #print(len(data_one))
            #print(data_one) 
            if(len(data_one) == 0):
                data_one = data.drop(data[data.PMax_Letter_Grade != 'A'].index)       
                #print(len(data_one))
                #print(data_one) 
                if(len(data_one) == 0):
                    data_one = data.drop(data[data.PMax_Letter_Grade != 'BBB'].index)
                    #print(len(data_one))
                    #print(data_one) 
                    if(len(data_one) == 0):
                        data_one = data.drop(data[data.PMax_Letter_Grade != 'BB'].index)
                        #print(len(data_one))
                        #print(data_one) 
                        if(len(data_one) == 0):
                            data_one = data.drop(data[data.PMax_Letter_Grade != 'B'].index)
                            #print(len(data_one))
                            #print(data_one) 
                            if(len(data_one) == 0):
                                data_one = data.drop(data[data.PMax_Letter_Grade != 'CCC'].index)
                                #print(len(data_one))
                                #print(data_one) 
                                if(len(data_one) == 0):
                                    data_one = data.drop(data[data.PMax_Letter_Grade != 'CC'].index)
                                    #print(len(data_one))
                                    #print(data_one) 
                                    if(len(data_one) == 0):
                                        data_one = data.drop(data[data.PMax_Letter_Grade != 'C'].index)
                                        #print(len(data_one))
                                        #print(data_one) 
                                        if(len(data_one) == 0):
                                            data_one = data.drop(data[data.PMax_Letter_Grade != 'DDD'].index)
                                            #print(len(data_one))
                                            #print(data_one) 
                                            if(len(data_one) == 0):
                                                data_one = data.drop(data[data.PMax_Letter_Grade != 'DD'].index)
                                                #print(len(data_one))
                                                #print(data_one) 
                                                if(len(data_one) == 0):
                                                    data_one = data.drop(data[data.PMax_Letter_Grade != 'D'].index)
                                                    #print(len(data_one))
                                                    #print(data_one) 
                                                    if(len(data_one) == 0):
                                                        data_one = data.drop(data[data.PMax_Letter_Grade != 'FF'].index)
                                                        #print(len(data_one))
                                                        #print(data_one) 
                                                        if(len(data_one) == 0):
                                                            data_one = data.drop(data[data.PMax_Letter_Grade != 'F'].index)
                                                            #print(len(data_one))
                                                            #print(data_one) 
                                                            if(len(data_one) == 0):
                                                                print("NO GOOD PARAMETERS")
        
        #print('---------------------------------------------------')
    
        #data_one = data_one.sample()
        #pd.set_option('display.max_columns', 100)
        #print(data_one)
        #data_one = data_one['Net Profit All'].max()
        #print(data_one)
        #pd.set_option('display.max_columns', 100)
        data_one = data_one[data_one['Profit Factor'] == data_one['Profit Factor'].max()]
        #print(data_one)


        letter_grade = [data_one.iloc[0]['PMax_Letter_Grade']]
        #print(letter_grade)
        
        #print('---------------------------------------------------')
        
        Multiplier_ATR_arrays.append(data_one.iloc[0]['ATR Multiplier'])
        
        Length_Tillson_arrays.append(data_one.iloc[0]['Tillson T3 Length'])
        
        T3a1_Tillson_Volume_arrays.append(data_one.iloc[0]['T3a1 Tillson Volume'])
        
        Period_ATR_arrays.append(data_one.iloc[0]['ATR Length'])
        
        rsi_length_arrays.append(data_one.iloc[0]['RSI Length'])
        
        letter_grade_append.append(letter_grade)
        
        net_profit.append(data_one.iloc[0]['Net Profit All'])
        #print("Net Profit:", net_profit)
        
        stop_loss_append.append(data_one.iloc[0]['Stop Loss Percentage'])
        
        number_of_trades_append.append(data_one.iloc[0]['Total Closed Trades'])
        
        percentage_profitable_append.append(data_one.iloc[0]['Percent Profitable'])
        
        percentage_profitable_long_append.append(data_one.iloc[0]['Percent Profitable Long'])
        
        percentage_profitable_short_append.append(data_one.iloc[0]['Percent Profitable Short'])
        
        trend_percentage_append.append(data_one.iloc[0]['Trend Percentage'])
        
        max_deviation_append.append(data_one.iloc[0]['Portfolio Max Deviation'])
        
        max_drawdown_append.append(data_one.iloc[0]['Portfolio Max Drawdown Percentage'])
        
        maxdrawdown_netprofit_ratio_append.append(data_one.iloc[0]['MaxDrawdown/NetProfit Ratio'])
        
        win_loss_ratio_append.append(data_one.iloc[0]['Ratio Average Win/Loss'])
        
        bhr_append.append(data_one.iloc[0]['Buy and Hold Return'])
        
        stdev_append.append(data_one.iloc[0]['Profit Factor'])
        
        net_profit_long.append(data_one.iloc[0]['Net Profit Long'])
        
        average_trade_long.append(data_one.iloc[0]['Average Trade Long'])
        
        ##length_parameter_data = len(net_profit)
        #print(length_parameter_data)
        #print('------------------------------------------------')
        ##if(length_parameter_data == 10+1):
            ##break
        
        ts.append(ticker)
        se.append(exchange)
        
    
        #print(Multiplier_ATR_arrays)   
        #print(Length_Tillson_arrays)   
        #print(T3a1_Tillson_Volume_arrays)    
        #print(Period_ATR_arrays)    
        #print(rsi_length_arrays)  
        #print(letter_grade_append)
        
        pd.set_option('display.max_columns', 6)
        ticker_symbol_grade_df = pd.DataFrame(ts)
        ticker_stock_exchange = pd.DataFrame(se)
        letter_grade_df = pd.DataFrame(letter_grade_append)
        atr_mult_df = pd.DataFrame(Multiplier_ATR_arrays)
        Length_Tillson_df = pd.DataFrame(Length_Tillson_arrays)
        T3a1_Tillson_Volume_df = pd.DataFrame(T3a1_Tillson_Volume_arrays)
        period_atr_df = pd.DataFrame(Period_ATR_arrays)
        rsi_length_df = pd.DataFrame(rsi_length_arrays)
        net_profit_all_df = pd.DataFrame(net_profit)
        stop_loss_all_df = pd.DataFrame(stop_loss_append)
        number_trades_df = pd.DataFrame(number_of_trades_append)
        percent_profitable_df = pd.DataFrame(percentage_profitable_append)
        percent_profitable_long_df = pd.DataFrame(percentage_profitable_long_append)
        percent_profitable_short_df = pd.DataFrame(percentage_profitable_short_append)
        trend_percentage_df = pd.DataFrame(trend_percentage_append)
        max_deviation_df = pd.DataFrame(max_deviation_append)
        max_drawdown_df = pd.DataFrame(max_drawdown_append)
        maxdrawdown_netprofit_ratio_df = pd.DataFrame(maxdrawdown_netprofit_ratio_append)
        win_loss_ratio_df = pd.DataFrame(win_loss_ratio_append)
        bhr_df = pd.DataFrame(bhr_append)
        stdev_df = pd.DataFrame(stdev_append)
        net_profit_long_df = pd.DataFrame(net_profit_long)
        average_trade_long_df = pd.DataFrame(average_trade_long)
        
        #max_perc_df = pd.concat([csv_ticker_list['Percent Profitable Long'],csv_ticker_list['Percent Profitable Short']], axis = 1)
        #print(max_perc_df)
        
        max_perc_short_np = percent_profitable_short_df.to_numpy().tolist()
        #print(max_perc_short_np)
        
        max_perc_long_np = percent_profitable_long_df.to_numpy().tolist()
        #print(max_perc_long_np)
        
        perc_pos_ind_append = []
        for items_long, items_short in zip(max_perc_long_np, max_perc_short_np):
            #print(items_long)
            #print(items_short)
            if(items_long > items_short):
                perc_pos_ind = 1
            else:
                perc_pos_ind = 0
            perc_pos_ind_append.append(perc_pos_ind)
            
        #print(perc_pos_ind_append)
        
        #max_finder = max_perc_df.max(axis=1)
        #print(max_finder)
        
        max_finder = pd.DataFrame(perc_pos_ind_append)
        #max_finder.columns = ['Percent Position']
        #print(max_finder)
        
        
        
        parameter_grade_df = pd.concat([ticker_symbol_grade_df, ticker_stock_exchange, letter_grade_df, atr_mult_df,Length_Tillson_df,T3a1_Tillson_Volume_df,period_atr_df,rsi_length_df,net_profit_all_df,stop_loss_all_df,number_trades_df,percent_profitable_df,percent_profitable_long_df,percent_profitable_short_df,trend_percentage_df,max_deviation_df,max_drawdown_df,maxdrawdown_netprofit_ratio_df,max_finder,win_loss_ratio_df,stdev_df,net_profit_long_df,average_trade_long_df], axis = 1)
        parameter_grade_df.columns =['Ticker','Exchange','PMax_Letter_Grade','ATR Multiplier','Tillson T3 Length','T3a1 Tillson Volume','ATR Length','RSI Length','Net Profit All','Stop Loss Percentage','Number of Closed Trades','Percent Profitable','Percent Profitable Long','Percent Profitable Short','Trend Percentage','Portfolio Max Deviation','Portfolio Max Drawdown Percentage','MaxDrawdown/NetProfit Ratio','Percent Position','Win/Loss Ratio','Profit Factor','Net Profit Long','Average Trade Long']
        pd.set_option('display.max_rows', 500)  
        #print(parameter_grade_df)
        
        ticker_grades_csv = parameter_grade_df.to_csv("original_ticker_parameter_grades.csv")
      
    

        
    
    
    parameter_data_reader = pd.read_csv('original_ticker_parameter_grades.csv')
    #print(parameter_data_reader)     
    
    
    
    
    
    
    keep_AAA = parameter_data_reader.drop(parameter_data_reader[parameter_data_reader.PMax_Letter_Grade != 'AAA'].index)
    #print(keep_AAA)
    AAA_parameter_data_reader_ticker = keep_AAA['Ticker'].to_numpy().tolist()
    
    
    
    
    
    sum_total_points = []
    sum_ticker_list = []
    for items_keep_AAA_list_np in AAA_parameter_data_reader_ticker:
        
        keep_AAA.sort_values(by=['Net Profit All'], inplace=True, ascending=False)
        keep_AAA_list_np = keep_AAA['Ticker'].to_numpy().tolist()
        
        point_list = []
        
        #print("Ticker:", items_keep_AAA_list_np)
        
        
        
        AAA_np_index = keep_AAA_list_np.index(items_keep_AAA_list_np)
        #print("Pos in Array:", AAA_np_index)
        
        
        
        if(AAA_np_index == 0):
            points = 4
            #print('Points Assigned NP:', points)
            point_list.append(points)
        elif(AAA_np_index == 1):
            points = 3
            #print('Points Assigned NP:', points)
            point_list.append(points)
        elif(AAA_np_index == 2):
            points = 2
            #print('Points Assigned NP:', points)
            point_list.append(points)
        elif(AAA_np_index == 3):
            points = 1
            #print('Points Assigned NP:', points)
            point_list.append(points)
            
            
            
        



        #print(point_list)
        #print("Ticker:", items_keep_AAA_list_np, "Points Sum:", sum(point_list))
        
        sum_ticker_list.append(items_keep_AAA_list_np)
        sum_total_points.append(sum(point_list))
            
        #print('-------------------')
     
    
    #print(sum_ticker_list)
    #print(sum_total_points)
     
    
    total_points_ticker_df = pd.DataFrame(sum_ticker_list)
    total_points_ticker_df.columns = ['Ticker']
    total_points_df = pd.DataFrame(sum_total_points)
    total_points_df.columns = ['Total Points']
    
    concat_total = pd.concat([total_points_ticker_df,total_points_df], axis = 1)
    concat_total.sort_values(by=['Total Points'], inplace=True, ascending=False)
    concat_total = concat_total.set_index('Ticker')
    #print(concat_total)
    
    #print('------------------------')
    
    keep_AAA = keep_AAA.reset_index()
    keep_AAA = keep_AAA.drop('Unnamed: 0',axis=1)
    keep_AAA = keep_AAA.drop('index',axis=1)
    keep_AAA = keep_AAA.set_index('Ticker')
    #print(keep_AAA)
    
    
    #print('------------------------')
    
    final = pd.concat([concat_total['Total Points'],keep_AAA], axis = 1)      
    #print(final)
    #final.to_csv('ticker_parameter_grades.csv')
    final.to_csv('all_AAA_points.csv')
    
    #print(final[0:4])
    
    final = final.reset_index()
    final[0:4].to_csv('ticker_parameter_grades.csv')
        
    print("PARAMETER AUTOFILLER COMPLETE")
    
parameter_autofiller()













 
    
    
    
    

