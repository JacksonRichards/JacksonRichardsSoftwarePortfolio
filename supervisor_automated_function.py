
import datetime
import time
import keyboard
import pandas as pd
import os.path
from datetime import timedelta
from datetime import date
import os
import shutil
from statistics import *



e = datetime.datetime.now()
print("Current Datetime:", e)
d1 = datetime.datetime(e.year, e.month, e.day, 13, 1) 
#print("Target Datetime One:", d1)
d2 = datetime.datetime(e.year, e.month, e.day, 23, 59) 
#print("Target Datetime Two:", d2)

weekday = e.strftime('%A')
print('Day Of The Week Is:', weekday)

print('--------------------------------')

today_initial_data = date.today()
y = today_initial_data.strftime("%m-%d-%Y")
NY = 'America/los_angeles'
end=pd.Timestamp(y, tz=NY)   
record_date = y
#print("Record Date:", record_date)

part_conf_1 = 1
part_conf_2 = 1

while True:
    
    if(d1 <= e and e <= d2 and weekday != 'Saturday' and weekday != 'Sunday'):
             
        print("Setup Proccess Initiated #1")
        
   
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') == True): 
            ticker_param_grades = pd.read_csv('ticker_parameter_grades.csv')
            list_of_tickers = ticker_param_grades['Ticker'][0:4].to_numpy().tolist()
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\DID_NOT_TRADE.csv') != True): 
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\new_alpaca_tv_data_'+list_of_tickers[0]+'.csv') != True): 
                    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\new_alpaca_tv_data_'+list_of_tickers[0]+'.csv') != True): 
                        did_not_trade_df = pd.DataFrame(['TRUE'])
                        did_not_trade_df.to_csv('DID_NOT_TRADE.CSV')
                        
                        print("DID NOT TRADE PROTOCOL ACTIVATED:")

                        from record_transfers import *
                        print("DID NOT TRADE PROTOCOL COMPLETED")
                        break
                        #time.sleep(2)
                        

                        
                            
                        #time.sleep(2)
                        
                    else:
                        print("DID NOT TRADE PROTOCOL SKIPPED")
                        
            elif(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\DID_NOT_TRADE.csv') == True):
                print("DID NOT TRADE PROTOCOL COMPLETED")
                
            else:
                print("DID NOT TRADE PROTOCOL SKIPPED")
                
                
                
                
                
                
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\market_exit_time.csv') != True):
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv') != True):
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\DID_NOT_TRADE.csv') != True):
                    ticker_list_market_exit_time_df = pd.read_csv('ticker_parameter_grades.csv')
                    ticker_list_market_exit_time = ticker_list_market_exit_time_df['Ticker'].to_numpy().tolist()
                    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\new_alpaca_tv_data_'+ticker_list_market_exit_time[0]+'.csv') == True):
                        print("MARKET EXIT TIME RECORDER COMMENCING")
                        path_market_et = 'new_alpaca_tv_data_'+ticker_list_market_exit_time[0]+'.csv'
                        ti_m = os.path.getmtime(path_market_et)            
                        m_ti = time.ctime(ti_m)
                        #print(m_ti[11:19])
                        exit_market_time = pd.DataFrame([m_ti[11:19]])
                        exit_market_time.to_csv('market_exit_time.csv')
                        exit_market_time.columns = ['Market Exit Time']
                        print("MARKET EXIT TIME RECORDER COMPLETED")
                    
                    
                    
                    
                    
        

                
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\intraday_simmulation_summary_analysis.csv') != True):          
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\intraday_simmulation_summary_analysis.csv') != True):
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv') == True):
                    from one_day_strategy_simulation import *
                    time.sleep(2)
                    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_2_percentage_movements.csv') == True):
                        from simmulation_micro_analysis import *
                        time.sleep(2)
                    else:
                        print("NO TRADES EXECUTED")
                else:
                    print("CURRENT DAY SIMMUALTOR COMPLETE") 
                    print("PORTFOLIO SIMMULATION MICRO VIEW COMPLETE")
                    
            else:
                print("CURRENT DAY SIMMUALTOR COMPLETE") 
                print("PORTFOLIO SIMMULATION MICRO VIEW COMPLETE")

                
        else:
            print("CURRENT DAY SIMMUALTOR COMPLETE") 
            print("PORTFOLIO SIMMULATION MICRO VIEW COMPLETE")
            
                
        
                
                
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stock_activities.csv') != True):
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\stock_activities.csv') != True):
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv') == True):
                    #print(False)
                    from record_keeping import *
                    time.sleep(2) 
                else:
                    print("RECORD KEEPING COMPLETE")  
                    
            else:
                print("RECORD KEEPING COMPLETE") 
                
        else:
            print("RECORD KEEPING COMPLETE") 
                
                             
                
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\portfolio_data.csv') != True):
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\portfolio_data.csv') != True):
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv') == True):
                    from portfolio_data_scraper import*
                    time.sleep(2)
                
                else:
                    print("PORTFOLIO SCRAPING COMPLETE")  
                    
            else:
                print("PORTFOLIO SCRAPING COMPLETE")  
                
        else:
            print("PORTFOLIO SCRAPING COMPLETE")  
                
                
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\summary_report_'+record_date+'.docx') != True):
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\summary_report_'+record_date+'.docx') != True):
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv') == True):
                    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\one_day_2_percentage_movements.csv') == True):
                        from summary_report import *
                        time.sleep(2)
                    else:
                        print("NO SUMMARY REPORT GENERATED")
                        
                    from trading_record_compiler import *
                    time.sleep(2)
                    
                else:  
                    print("SUMMARY REPORT COMPLETE")
                    print("TRADING RECORDS COMPILER COMPLETE")
                    
            else:
                print("SUMMARY REPORT COMPLETE")
                print("TRADING RECORDS COMPILER COMPLETE")
                
        else:
            print("SUMMARY REPORT COMPLETE")
            print("TRADING RECORDS COMPILER COMPLETE")
                
                
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv') != True):
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\market_exit_time.csv') != True): 
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_list_today.csv') != True):
                    original = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Master Documents\ticker_list_today.csv'
                    target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_list_today.csv'
                    shutil.copy(original, target)
                    time.sleep(2)
                    break
                else:
                    print("RECORD TRANSFERS COMPLETE")  
                
            elif(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_list_today.csv') != True): 
                from record_transfers import *
                time.sleep(2)   
                break
                
            else:
                print("RECORD TRANSFERS COMPLETE") 
                
        elif(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\market_exit_time.csv') == True):
            from record_transfers import *
            time.sleep(2)
            break
        
        else:
            print("RECORD TRANSFERS COMPLETE")  
            
            
            
        ticker_list_master = pd.read_csv('ticker_list_today.csv')
        check_list = ticker_list_master['Tickers'].to_numpy().tolist()
        #print(check_list[0])
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\tradingview_'+str(check_list[len(check_list)-1])+'_data.csv') != True):
            from automatic_data_webscraper import *
            time.sleep(2)   
        else:
            print("CSV DATA DOWNLOAD COMPLETE")
            
            
        ticker_list_master = pd.read_csv('ticker_list_today.csv')
        check_list = ticker_list_master['Tickers'].to_numpy().tolist()
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_1_'+str(check_list[len(check_list)-1])+'_TRADINGVIEW.csv') != True):
            from initial_setup_training_algorithm import *
            time.sleep(2)
        else:
            print("DATA STORING SETUP COMPLETE")  
        
            
            
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_1_'+str(check_list[len(check_list)-1])+'_TRADINGVIEW.csv') == True):
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') != True):
                #print(False)
                from threading_algo_trainer import *
                time.sleep(2)            
                
            else:
                print("THREADING TRAINING PROCCESS COMPLETE")
                print("PARAMETER AUTOFILLER COMPLETE")
                
        else:
            print("THREADING TRAINING PROCCESS COMPLETE")
            print("PARAMETER AUTOFILLER COMPLETE")
            
            
            
            
            
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\training_data_compiled_'+str(check_list[len(check_list)-1])+'.csv') != True):
           from training_file_compiler import *
           time.sleep(2)
           
        else:
            print("TRAINING RECORD COMPILER COMPLETE")  
     
        
     
        
     
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') != True):
            from parameter_selector import *
            time.sleep(2)
            
        else:
            print("PARAMETER AUTOFILLER COMPLETE") 
            
            
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\error_records.csv') != True):
            from error_records_database import *
            time.sleep(2)
            break
        else:
            print("ERROR RECORDS DATABASE SETUP COMPLETE") 
            #print("STOCK POSITION UPDATER COMPLETE") 
        


            
    elif(part_conf_1 == part_conf_2 or weekday == 'Saturday' or weekday == 'Sunday'):
        
        
        print("Setup Proccess Initiated #2")
        
        
        ticker_list_master = pd.read_csv('ticker_list_today.csv')
        check_list = ticker_list_master['Tickers'].to_numpy().tolist()
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Pmax_Algo_Data_collection_1_'+str(check_list[len(check_list)-1])+'_TRADINGVIEW.csv') == True):
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') != True):
                #print(False)
                from threading_algo_trainer import *
                time.sleep(2)            
                
            else:
                print("THREADING TRAINING PROCCESS COMPLETE")
                
        else:
            print("THREADING TRAINING PROCCESS COMPLETE")
            
            
            
            
            
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\training_data_compiled_'+str(check_list[len(check_list)-1])+'.csv') != True):
           from training_file_compiler import *
           time.sleep(2)
           
        else:
            print("TRAINING RECORD COMPILER COMPLETE")  
     
        
     
        
     
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') != True):
            from parameter_selector import *
            time.sleep(2)
            
        else:
            print("PARAMETER AUTOFILLER COMPLETE") 
            
            
            
            
            
            
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\error_records.csv') != True):
            from error_records_database import *
            time.sleep(2)
            break
        else:
            print("ERROR RECORDS DATABASE SETUP COMPLETE") 
            #print("STOCK POSITION UPDATER COMPLETE") 
        
        
        
        
        
        
        
          
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\stop_loss_variable.csv') != True): 
            
            if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\forced_liquidation_variable.csv') != True): 
            
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') == True):
                    from trading_bot import *
                    time.sleep(2) 
                    break
    
                else:
                    skip = 0
                    print("Trading Bot NOT Initiated, parameters missing", False)
                    break
                
            else:
                print("FORCED LIQUIDATION ALREADY HIT")
                break 
            
        else:
            print("STOP LOSS ALREADY HIT")
            break   
            
            
                  
        
      
            
            
        
        
        
        
        
        
    else:
        print("Not Ready to Initiate Setup Proccess")
        time.sleep(2)

            
            
            
        
        
        
        






















