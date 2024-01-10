

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date



def relevant_earnings_dates():
    
    
    print("EARNINGS DATE UPDATER COMMENCING")


    today_initial_data = date.today()
    today_initial_data = today_initial_data.strftime("%Y-%m-%d")
    #print(today_initial_data)
    
    earnings_dates = pd.read_csv('updated_earnings.csv')  
    master_ticker_sheet = pd.read_csv('ticker_list_today.csv')
    
    earnings_dates.pop('Unnamed: 0')
    
    #print(master_ticker_sheet)
    #print('-----------------------------')
    
    if('Next Earnings Date' in master_ticker_sheet and 'Days Until Earnings Date' in master_ticker_sheet):
        #print("Yes, it does exist.")
        master_ticker_sheet.pop('Next Earnings Date')
        master_ticker_sheet.pop('Days Until Earnings Date')
        master_ticker_sheet.pop('Unnamed: 0')
        #master_ticker_sheet.drop(columns = master_ticker_sheet.columns[0], axis = 1, inplace= True)
        
    else:
        nothing = 0


    #print(earnings_dates)
    #print(master_ticker_sheet)

    mergedStuff = pd.merge(earnings_dates, master_ticker_sheet, on=['Tickers'], how='inner')
    #print(mergedStuff)
    
    
    delta_date_append = []
    for items_date, items_ticker in zip(mergedStuff['Next Earnings Date'], mergedStuff['Tickers']):
    
        d1 = datetime.strptime(today_initial_data, "%Y-%m-%d")
        #print(d1)
        #print(type(d1))
        
        
        #earnings_date = mergedStuff['Next Earnings Date'][0]    
        d2 = datetime.strptime(items_date, "%Y-%m-%d")
        #print(d2)
        #print(type(d2))
        
        
        delta_date = d2 - d1
        #print('Days Until Next Earnings Date:', delta_date.days, items_ticker)
        #print(type(delta_date.days))
        #print(delta_date)
        delta_date_append.append(delta_date.days)
        
    #print(delta_date_append)
    
    delta_date_df = pd.DataFrame(delta_date_append)
    delta_date_df.columns = ['Days Until Earnings Date']
    
    dued_index_values = delta_date_df[delta_date_df['Days Until Earnings Date'] <= -1].index.values
    #print(dued_index_values)
    delta_date_df.drop(dued_index_values, inplace=True)
    #print(delta_date_df)
    
    
    
    
    
    final_merged = pd.concat([mergedStuff, delta_date_df], axis = 1)
    final_merged.dropna(inplace=True)
    #print(final_merged)
    
    final_merged.to_csv('ticker_list_today.csv')
    
    
    print("EARNING DATES UPDATER COMPLETE")
    
       
    '''
    # dates in string format
    str_d1 = '2021-10-20'
    str_d2 = '2022-2-20'
    
    # convert string to date object
    d1 = datetime.strptime(str_d1, "%Y-%m-%d")
    d2 = datetime.strptime(str_d2, "%Y-%m-%d")
    
    # difference between dates in timedelta
    delta = d2 - d1
    print(f'Difference is {delta.days} days')
    '''



    '''
    datetimes_next_earnings_dates = pd.DataFrame(next_earnings_date_append)
    datetimes_next_earnings_dates.columns = ['Next Earnings Date']
    #print(datetimes_next_earnings_dates)
    #print('-----------------------------')
    concat_master_and_earndate = pd.concat([master_ticker_sheet,datetimes_next_earnings_dates], axis = 1)
    '''




relevant_earnings_dates()


