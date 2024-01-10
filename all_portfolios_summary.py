

import warnings
import urllib.request
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
import time
import pandas as pd
import datetime


warnings.filterwarnings('ignore')




all_accounts_array = []

while True:

    
    account_numbers = [1,2,3,4,5,6]
    trading_mode = [False,False,False,False,False,False]
    #trading_mode = [False,False,False,False,False,False]
    all_accounts_array = []
    for item_account_numbers, item_trading_mode in zip(account_numbers,trading_mode):
        
        ##print("Account Number:", item_account_numbers)    
    
        api_keys_csv = pd.read_csv('alpaca_api_information_terminal_'+str(item_account_numbers)+'.csv')
        
        trading_client = TradingClient(api_keys_csv['API KEY'][0], api_keys_csv['API SECRET KEY'][0], paper=item_trading_mode)
        
        account = trading_client.get_account()
        
        last_equity = account.last_equity
        ##print("Last Equity:", last_equity)
        current_equity = account.equity
        print("Current Equity:", current_equity)
        
        perc_change = (float(current_equity)-float(last_equity))/float(last_equity)*100
        print("Percentage Change:", perc_change, '%')
        
        all_accounts_array.append(perc_change)
        
        ##print('----------------------------')
    
    #print(sum(all_accounts_array))    
    
    print('----------------------------')
    
    now = datetime.datetime.now()
    #print(now)
    #print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    # 2015 5 6 8 53 40
    
    length_all_accounts_array = len(all_accounts_array)
    #print(length_all_accounts_array)
    
    print(sum(all_accounts_array)/length_all_accounts_array)
    
    time_df = pd.DataFrame([now])
    company_wide_portfolio_average = sum(all_accounts_array)/length_all_accounts_array
    #company_wide_portfolio_average = 1
    company_wide_portfolio_average_df = pd.DataFrame([company_wide_portfolio_average])
    terminal_1_df = pd.DataFrame([all_accounts_array[0]])
    #print(terminal_1_df)
    terminal_2_df = pd.DataFrame([all_accounts_array[1]])
    terminal_3_df = pd.DataFrame([all_accounts_array[2]])
    terminal_4_df = pd.DataFrame([all_accounts_array[3]])
    terminal_5_df = pd.DataFrame([all_accounts_array[4]])
    terminal_6_df = pd.DataFrame([all_accounts_array[5]])
    final_company_overview = pd.concat([time_df,company_wide_portfolio_average_df,terminal_1_df,terminal_2_df,terminal_3_df,terminal_4_df,terminal_5_df,terminal_6_df], axis=1)
    #final_company_overview.columns = ["Time","Overall Average","Terminal 1","Terminal 2","Terminal 4","Terminal5","Terminal 6"]
    final_company_overview.to_csv('company_wide_portfolio_average_'+str(now.month)+'_'+str(now.day)+'_'+str(now.year)+'.csv', mode='a', index=False)
    
    print('--------------------------')
    
    time.sleep(30)
        
    
        
    

    #break
    
    





