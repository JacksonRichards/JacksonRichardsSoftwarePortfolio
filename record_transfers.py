


import shutil
import pandas as pd
import datetime
import calendar
from datetime import date
from datetime import timedelta
from datetime import date
import os



def record_transfers():
    
    print("RECORD TRANSFERS COMMENCING")
    
    today = date.today()
    #print("Today is: ", today)           
    # Yesterday date
    curr_date = date.today()

    #print(calendar.day_name[curr_date.weekday()])



    today_initial_data = date.today()
    y = today_initial_data.strftime("%m-%d-%Y")
    #y =  dt.strftime("%m-%d %H:%M")
    #print(x)
    #print(y)
    NY = 'America/los_angeles'
    end=pd.Timestamp(y, tz=NY)
    #print(end)       
    record_date = y
    #record_date = time_string_initial_data.replace('0', '')
    ####print("Current Day:", record_date)

    #record_date = '6-29-2022'
    
    script_path = os.path.realpath(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records')
    new_abs_path = os.path.join(script_path, '0'+record_date)
    os.mkdir(new_abs_path)
    
    
    #original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\entry_exit_time_simmualtor_detail.csv'
    #target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\entry_exit_time_simmualtor_detail.csv'
    #shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\portfolio_data.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\portfolio_data.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\portfolio_data.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\market_exit_time.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\full_trading_cycle_result.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\full_trading_cycle_result.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\full_trading_cycle_result.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\full_trading_cycle_result_detail.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\full_trading_cycle_result_detail.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\full_trading_cycle_result_detail.csv'
        shutil.move(original, target)
    
    
    #original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stock_positions.csv'
    #target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\stock_positions.csv'
    #shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\gain_cap_variable.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\gain_cap_variable.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\gain_cap_variable.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\error_records.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\error_records.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\error_records.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stock_balance_marginrequirements.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stock_balance_marginrequirements.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\stock_balance_marginrequirements.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\original_ticker_parameter_grades.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\original_ticker_parameter_grades.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\original_ticker_parameter_grades.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stock_activities.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stock_activities.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\stock_activities.csv'
        shutil.move(original, target)
    
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_2_percentage_movements.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_2_percentage_movements.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\one_day_2_percentage_movements.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_1_percentage_movements.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_1_percentage_movements.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\one_day_1_percentage_movements.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_0_percentage_movements.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_0_percentage_movements.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\one_day_0_percentage_movements.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_3_percentage_movements.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_3_percentage_movements.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\one_day_3_percentage_movements.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_4_percentage_movements.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_4_percentage_movements.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\one_day_4_percentage_movements.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_5_percentage_movements.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_5_percentage_movements.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\one_day_5_percentage_movements.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\intraday_simmulation_summary_analysis.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\intraday_simmulation_summary_analysis.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\intraday_simmulation_summary_analysis.csv'
        shutil.move(original, target)
    
    ticker_list_today = pd.read_csv('ticker_list_today.csv')
    
    for ticker in ticker_list_today['Tickers']:
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_1_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_1_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_1_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_2_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_2_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_2_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_3_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_3_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_3_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_4_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_4_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_4_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_5_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_5_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_5_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_6_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_6_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_6_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_7_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_7_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_7_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_8_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_8_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_8_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_9_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_9_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_9_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_10_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_10_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_10_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_11_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_11_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_11_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_12_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_12_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_12_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_13_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_13_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_13_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_14_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_14_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_14_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_15_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_15_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_15_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_16_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_16_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_16_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_17_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_17_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_17_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_18_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_18_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_18_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_19_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_19_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_19_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_20_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_20_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_20_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_21_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_21_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_21_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_22_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_22_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_22_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_23_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_23_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_23_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_24_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_24_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_24_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_25_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_25_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_25_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_26_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_26_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_26_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_27_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_27_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_27_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_28_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_28_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_28_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_29_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_29_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_29_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_30_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_30_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_30_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_31_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_31_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_31_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_32_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_32_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_32_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_33_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_33_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_33_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_34_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_34_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_34_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_35_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_35_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_35_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
            
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_36_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_36_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_36_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_37_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_37_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_37_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_38_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_38_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_38_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_39_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_39_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_39_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_40_'+ticker+'_TRADINGVIEW.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_40_'+ticker+'_TRADINGVIEW.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\Pmax_Algo_Data_collection_40_'+ticker+'_TRADINGVIEW.csv'
            shutil.move(original, target)
        
         
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\tradingview_'+ticker+'_data.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\tradingview_'+ticker+'_data.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\tradingview_'+ticker+'_data.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\training_data_compiled_'+ticker+'.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\training_data_compiled_'+ticker+'.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\training_data_compiled_'+ticker+'.csv'
            shutil.move(original, target)
        
        #original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\backtest_'+ticker+'_PMAX_alert_source_tradingview_data.csv'
        #target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\backtest_'+ticker+'_PMAX_alert_source_tradingview_data.csv'
        #shutil.move(original, target)
        
        place_holder = 0
    
    parameter_ticker_list = pd.read_csv('ticker_list_today.csv')  
        
    for ticker in parameter_ticker_list['Tickers']:
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\new_alpaca_tv_data_'+ticker+'.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\new_alpaca_tv_data_'+ticker+'.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\new_alpaca_tv_data_'+ticker+'.csv'
            shutil.move(original, target)
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\PMAX_'+ticker+'_alert_source_tradingview_data.csv') == True):
            original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\PMAX_'+ticker+'_alert_source_tradingview_data.csv'
            target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\PMAX_'+ticker+'_alert_source_tradingview_data.csv'
            shutil.move(original, target)
        
        #original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\modified_start_exit_times_'+ticker+'.csv'
        #target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\modified_start_exit_times_'+ticker+'.csv'
        #shutil.move(original, target)
    

        
        
     
    #original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\entry_exit_time_simmualtor.csv'
    #target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\entry_exit_time_simmualtor.csv'
    #shutil.move(original, target)
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\ticker_parameter_grades.csv'
        shutil.move(original, target)
        
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_list_today.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_list_today.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\ticker_list_today.csv'
        shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\all_AAA_points.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\all_AAA_points.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\all_AAA_points.csv'
        shutil.move(original, target)
    
    
    today_initial_data = date.today()
    y = today_initial_data.strftime("%m-%d-%Y")
    NY = 'America/los_angeles'
    end=pd.Timestamp(y, tz=NY)   
    today = y
    #print("Record Date:", today)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\summary_report_'+str(today)+'.docx') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\summary_report_'+str(today)+'.docx'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\summary_report_'+str(today)+'.docx'
        shutil.move(original, target)



    
    
    original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Master Documents\ticker_list_today.csv'
    target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_list_today.csv'
    shutil.copy(original, target)


    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\vix_amounts.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\vix_amounts.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\vix_amounts.csv'
        shutil.move(original, target)


    #original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\updated_earnings.csv'
    #target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\updated_earnings.csv'
    #shutil.move(original, target)
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\nasdaq_amounts.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\nasdaq_amounts.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\nasdaq_amounts.csv'
        shutil.move(original, target)
    
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\stop_loss_variable.csv'
        shutil.move(original, target)
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\DID_NOT_TRADE.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\DID_NOT_TRADE.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\DID_NOT_TRADE.csv'
        shutil.move(original, target)
    
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\portfolio_view_micro_view.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\portfolio_view_micro_view.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\portfolio_view_micro_view.csv'
        shutil.move(original, target)
    
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\aws_logic.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\aws_logic.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\aws_logic.csv'
        shutil.move(original, target)
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\daily_selector_logic.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\daily_selector_logic.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\daily_selector_logic.csv'
        shutil.move(original, target)
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\conviction_logic.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\conviction_logic.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\conviction_logic.csv'
        shutil.move(original, target)
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\kill_code_liquidation.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\kill_code_liquidation.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\kill_code_liquidation.csv'
        shutil.move(original, target)
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\opening_simmulation_results.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\opening_simmulation_results.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\opening_simmulation_results.csv'
        shutil.move(original, target)
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\trading_approved.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\trading_approved.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\trading_approved.csv'
        shutil.move(original, target)
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\trading_not_approved.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\trading_not_approved.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\trading_not_approved.csv'
        shutil.move(original, target)
        
        
        
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable_810_859.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable_810_859.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\stop_loss_variable_810_859.csv'
        shutil.move(original, target)   
    
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable_900_959.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable_900_959.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\stop_loss_variable_900_959.csv'
        shutil.move(original, target)
        
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable_1000_1059.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable_1000_1059.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\stop_loss_variable_1000_1059.csv'
        shutil.move(original, target)
    
    
    
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable_1100_1159.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable_1100_1159.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\stop_loss_variable_1100_1159.csv'
        shutil.move(original, target)
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\company_wide_stop_loss_indicator.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\company_wide_stop_loss_indicator.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\company_wide_stop_loss_indicator.csv'
        shutil.move(original, target)
        
        
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\forced_liquidation_variable.csv') == True):
        original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\forced_liquidation_variable.csv'
        target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\forced_liquidation_variable.csv'
        shutil.move(original, target)
        
        
    
        
        
        
    

    print("RECORD TRANSFERS COMPLETE")    
    
record_transfers()   
    




