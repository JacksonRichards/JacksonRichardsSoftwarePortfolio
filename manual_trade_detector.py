


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
#print("Current Datetime:", e)
d1 = datetime.datetime(e.year, e.month, e.day, 13, 1) 
#print("Target Datetime One:", d1)
d2 = datetime.datetime(e.year, e.month, e.day, 23, 59) 
#print("Target Datetime Two:", d2)

weekday = e.strftime('%A')
#print('Day Of The Week Is:', weekday)

#print('--------------------------------')

today_initial_data = date.today()
y = today_initial_data.strftime("%m-%d-%Y")
NY = 'America/los_angeles'
end=pd.Timestamp(y, tz=NY)   
record_date = y
#print("Record Date:", record_date)





def conviction_detector():
    
    print("CONVICTION DETECTOR COMMENCING")
    
    all_buckets = ['terminal-one-blc','terminal-two-blc','terminal-three-blc','terminal-four-blc','terminal-five-blc','terminal-six-blc']
    all_numbers = ['terminal_1','terminal_2','terminal_3','terminal_4','terminal_5','terminal_6']
    
    max_net_profit_avg_append = []
    
    for items_all_buckets, items_all_numbers in zip(all_buckets, all_numbers):
        downloaded_terminal_csv = pd.read_csv('ticker_parameter_grades_'+record_date+'_'+items_all_numbers+'.csv')
        #print(downloaded_terminal_csv)
        downloaded_terminal = mean(downloaded_terminal_csv['Net Profit All'][0:4].to_numpy().tolist())
        #print('Net Profit Average:', downloaded_terminal)
        max_net_profit_avg_append.append(downloaded_terminal)
    max_np_avg = max(max_net_profit_avg_append)
    #print(max_np_avg)
    
    for items_all_buckets_check, items_all_numbers_check in zip(all_buckets, all_numbers):
        downloaded_terminal_csv = pd.read_csv('ticker_parameter_grades_'+record_date+'_'+items_all_numbers_check+'.csv')
        #print(downloaded_terminal_csv)
        #print(items_all_numbers_check)
        downloaded_terminal = mean(downloaded_terminal_csv['Net Profit All'][0:4].to_numpy().tolist())
        #print('Net Profit Average:', downloaded_terminal)
        if(downloaded_terminal == max_np_avg):
           
            if(max_np_avg > 71999):
                #print('yes')
                os.rename('ticker_parameter_grades_'+record_date+'_'+items_all_numbers_check+'.csv', "ticker_parameter_grades.csv")
                #print('ticker_parameter_grades_'+record_date+'_'+items_all_numbers_check,"-","Chosen")
                coniction_logic_df = pd.DataFrame([True])
                coniction_logic_df.columns = ['Conviction Logic']
                coniction_logic_df.to_csv('conviction_logic.csv')
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\yesterday_ticker_parameter_grades.csv') == True):
                    os.remove("yesterday_ticker_parameter_grades.csv")
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\portfolio_view_micro_view.csv') == True):
                    os.remove("portfolio_view_micro_view.csv")
            else:
                #print("NO CONVICTION PARAMETERS DETECTED")
                os.remove('ticker_parameter_grades_'+record_date+'_'+items_all_numbers_check+'.csv')
            #break
            
        else:
            os.remove('ticker_parameter_grades_'+record_date+'_'+items_all_numbers_check+'.csv')
            #print('ticker_parameter_grades_'+record_date+'_'+items_all_numbers,"-","Not Chosen")
        

    print("CONVICTION DETECTOR COMPLETE")
    
conviction_detector()
































