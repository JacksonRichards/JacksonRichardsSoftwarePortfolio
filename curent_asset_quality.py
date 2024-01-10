

import yfinance as yf
import pandas as pd
import urllib.request
import time

def quality_assurance_new_assets():
    print("ASSET QUALITY INFORMATION PROCCESS COMMENCING")
    
    #ticker_symbols = pd.read_csv('ticker_list_today.csv')
    ticker_symbols = pd.read_csv('shortable_stocks.csv')
    ticker_symbols_np = ticker_symbols['Ticker'].to_numpy().tolist()
    #exchange_symbols_np = ticker_symbols['Exchange'].to_numpy().tolist()
    #print(ticker_symbols_np)
    #print(exchange_symbols_np)
    #print('-----------------------')
    #ticker_symbols_np = ['AAPL','NVDA']
    #exchange_symbols_np = ['NASDAQ','NASDAQ']
    average_3m_volume = []
    stock_beta = []
    tickers_3m_volume = []
    #exchange_3m_volume = []
    market_cap_append = []
    shares_outstanding_append = []
    number_shares_shortable_append = []
    per_shares_short_append = []
    for item_tickers in ticker_symbols_np:
        
        try:
            
            urllib.request.urlopen('http://google.com') #Python 3.x
            #print("Internet Connection Detected - Asset Quality Information")
        
            #print("Ticker Symbol:", item_tickers)
            
            symbol = yf.Ticker(item_tickers)
            
            # get stock info
            info = symbol.info
            #print(info)
            #print(info['averageVolume'])
            
            for items in info:
                #print(items)
                if(items == 'averageVolume'):
                    available_info = 1
                    #print('yes')
                if(items == 'beta'):
                    available_info = 1
                    #print('yes')
                if(items == 'marketCap'):
                    available_info = 1
                    #print('yes')
                if(items == 'sharesOutstanding'):
                    available_info = 1
                    #print('yes')
                if(items == 'sharesShort'):
                    available_info = 1
                    #print('yes')
                if(items == 'sharesPercentSharesOut'):
                    available_info = 1
                    #print('yes')
                
            sum_avail_items = available_info+available_info+available_info+available_info+available_info+available_info
            #print("Amount of Important Items:", sum_avail_items)
            
            
            if(sum_avail_items == 6):
                if(info['averageVolume'] == None and info['beta'] == None):
                    #print("Nothing variables detected")
                    nothing = 0
                elif(info['averageVolume'] != None and info['beta'] != None):
                    if(info['averageVolume'] >= 800000 and info['beta'] >= 0.8):
                        #print("Yes")
                        #print(info['averageVolume'])
                        average_3m_volume.append(info['averageVolume'])
                        stock_beta.append(info['beta'])
                        tickers_3m_volume.append(item_tickers)
                        #exchange_3m_volume.append(items_exchange)
                        market_cap_append.append(info['marketCap'])
                        shares_outstanding_append.append(info['sharesOutstanding'])
                        number_shares_shortable_append.append(info['sharesShort'])
                        per_shares_short_append.append(info['sharesPercentSharesOut'])
                        
                        #print(average_3m_volume)
                        #print(tickers_3m_volume)
                        #print(exchange_3m_volume)
                        average_3m_volume_df = pd.DataFrame(average_3m_volume)
                        stock_beta_df = pd.DataFrame(stock_beta)
                        tickers_3m_volume_df = pd.DataFrame(tickers_3m_volume)
                        #exchange_3m_volume_df = pd.DataFrame(exchange_3m_volume)
                        market_cap_df = pd.DataFrame(market_cap_append)
                        shares_outstanding_df = pd.DataFrame(shares_outstanding_append)
                        number_short_shares_outstanding = pd.DataFrame(number_shares_shortable_append)
                        shares_short_df = pd.DataFrame(per_shares_short_append)
                        concat_3m_volume = pd.concat([tickers_3m_volume_df,average_3m_volume_df,stock_beta_df,market_cap_df,shares_outstanding_df,number_short_shares_outstanding,shares_short_df], axis = 1)
                        concat_3m_volume.columns = ["Ticker","Average Volume 3m","Beta","Market Cap","Shares Outstanding","Short Shares Outstanding","Percent Shares Short Outstanding"]
                        concat_3m_volume.to_csv("approved_stocks.csv")
                        #print('-----------------------')
                        #print('-----------------------')
                        #print(concat_3m_volume)
                        
                        #print("Qualifications detected")
                    
                    else:
                        nothing = 0
                        #print("Does not meet volume and beta qualifications")
                        
                else:
                    nothing = 0
                    #print('Does not meet volume and beta qualifications')
                        
            else:
                nothing = 0
                #print("Not enough available items")
                
                
        except:
            
            print("No Internet Connection, Attempting Reconnection... - Asset Quality Information")
            time.sleep(0.5)
        
        #print('-------------------------')
            
    
    print("ASSET QUALITY ASSURANCE PROCESS COMPLETE")
    
quality_assurance_new_assets()


