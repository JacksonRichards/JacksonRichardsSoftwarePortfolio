
import datetime
import time
import keyboard
import pandas as pd
import os.path
from datetime import timedelta
from datetime import date




e = datetime.datetime.now()
print("Current Datetime:", e)
d1 = datetime.datetime(e.year, e.month, e.day, 13, 1) 
print("Target Datetime One:", d1)
d2 = datetime.datetime(e.year, e.month, e.day, 23, 59) 
print("Target Datetime Two:", d2)

weekday = e.strftime('%A')
print('Day Of The Week Is:', weekday)

print('--------------------------------')

today_initial_data = date.today()
y = today_initial_data.strftime("%m-%d-%Y")
NY = 'America/los_angeles'
end=pd.Timestamp(y, tz=NY)   
record_date = y
print("Record Date:", record_date)

part_conf_1 = 1
part_conf_2 = 1

while True:
    
    if(d1 <= e and e <= d2 and weekday != 'Saturday' and weekday != 'Sunday'):
             
        print("Setup Proccess Initiated #1")
        
        
        
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\Conviction Trading\Trading Records\stock_activities.csv') != True):    
            #print("Record Transfer file here")
            from record_keeping import *
            
        else:
            print("RECORD TRANSFER ALREADY COMPLETE")
            
        
        
        
        
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\Conviction Trading\Trading Records\portfolio_data.csv') != True):    
            #print("Record Transfer file here")
            from portfolio_data_scraper import *
            
        else:
            print("RECORD TRANSFER ALREADY COMPLETE")
            
            
            
            
            
                
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\Trading Records\0'+record_date+'\\ticker_list_today.csv') != True):    
            #print("Record Transfer file here")
            from record_transfers import *
            break
        else:
            print("RECORD TRANSFER ALREADY COMPLETE")
            
            
            
            
                
        
    elif(part_conf_1 == part_conf_2 or weekday == 'Saturday' or weekday == 'Sunday'):
        
        if(os.path.exists(r'C:\Users\jacks\Desktop\Conviction Trading\Trading Records\stop_loss_variable.csv') == True or os.path.exists(r'C:\Users\jacks\Desktop\Conviction Trading\Trading Records\cap_gain_variable.csv') == True):   
            print('GAIN CAP OR STOP LOSS ALREADY HIT')
            break
        elif(os.path.exists(r'C:\Users\jacks\Desktop\Conviction Trading\Trading Records\stop_loss_variable.csv') != True or os.path.exists(r'C:\Users\jacks\Desktop\Conviction Trading\Trading Records\cap_gain_variable.csv') != True):
            #print('Live Trading Bot Here')
            from conviction_trading_bot import *
            break
        
    else:
        print("Not Ready to Initiate Setup Proccess")
        time.sleep(2)

            
            
            
        
        
        
        






















