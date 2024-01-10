
import yfinance as yf
import pandas as pd
import urllib.request
import time

print("TICKER MASTER SHEET QUALITY ASSURANCE COMMENCING")

while True:

    try:
        
        urllib.request.urlopen('http://google.com') #Python 3.x
        #print("Internet Connection Detected - Ticker Master Sheet Quality Assurance")
        #time.sleep(1)
    
        def quality_assurance_current_assets():
            ticker_symbols = pd.read_csv('ticker_list_today.csv')
            #ticker_symbols = pd.read_csv('shortable_stocks.csv')
            ticker_symbols_np = ticker_symbols['Tickers'].to_numpy().tolist()
            #exchange_symbols_np = ticker_symbols['Exchange'].to_numpy().tolist()
            #print(ticker_symbols_np)
            #print(exchange_symbols_np)
            #print('-----------------------')
            
            if("Average Volume 3m" in ticker_symbols and "Beta" in ticker_symbols and "Market Cap" in ticker_symbols and "Shares Outstanding" in ticker_symbols and "Short Shares Outstanding" in ticker_symbols and "Percent Shares Short Outstanding" in ticker_symbols):
                #print("Yes, it does exist.")
                ticker_symbols.pop('Average Volume 3m')
                ticker_symbols.pop('Beta')
                ticker_symbols.pop('Market Cap')
                ticker_symbols.pop('Shares Outstanding')
                ticker_symbols.pop('Short Shares Outstanding')
                ticker_symbols.pop('Percent Shares Short Outstanding')
                ticker_symbols.pop('Unnamed: 0')
                #master_ticker_sheet.drop(columns = master_ticker_sheet.columns[0], axis = 1, inplace= True)
                
            else:
                nothing = 0
            
            
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
                #print("Ticker Symbol:", item_tickers)
                
                symbol = yf.Ticker(item_tickers)
                
                # get stock info
                info = symbol.info
                #print(info['averageVolume'])
                
                for items in info:
                    #print(items)
                    if(items == 'averageVolume'):
                        available_info = 1
                        average_3m_volume.append(info['averageVolume'])
                        #print('yes')
                    if(items == 'beta'):
                        available_info = 1
                        stock_beta.append(info['beta'])
                        #print('yes')
                    if(items == 'marketCap'):
                        available_info = 1
                        market_cap_append.append(info['marketCap'])
                        #print('yes')
                    if(items == 'sharesOutstanding'):
                        available_info = 1
                        shares_outstanding_append.append(info['sharesOutstanding'])
                        #print('yes')
                    if(items == 'sharesShort'):
                        available_info = 1
                        number_shares_shortable_append.append(info['sharesShort'])
                        #print('yes')
                    if(items == 'sharesPercentSharesOut'):
                        available_info = 1
                        per_shares_short_append.append(info['sharesPercentSharesOut'])
                        #print('yes')
                    
                sum_avail_items = available_info+available_info+available_info+available_info+available_info+available_info
                #print("Amount of Important Items:", sum_avail_items)
                #print('-----------------------')
        
             
                average_3m_volume_df = pd.DataFrame(average_3m_volume)
                average_3m_volume_df.columns = ["Average Volume 3m"]
                
                stock_beta_df = pd.DataFrame(stock_beta)
                stock_beta_df.columns = ["Beta"]
                
                
                market_cap_df = pd.DataFrame(market_cap_append)
                market_cap_df.columns = ["Market Cap"]
                
                shares_outstanding_df = pd.DataFrame(shares_outstanding_append)
                shares_outstanding_df.columns = ["Shares Outstanding"]
                
                number_short_shares_outstanding = pd.DataFrame(number_shares_shortable_append)
                number_short_shares_outstanding.columns = ["Short Shares Outstanding"]
                
                shares_short_df = pd.DataFrame(per_shares_short_append)
                shares_short_df.columns = ["Percent Shares Short Outstanding"]
                
                
                
                concat_3m_volume = pd.concat([ticker_symbols,average_3m_volume_df,stock_beta_df,market_cap_df,shares_outstanding_df,number_short_shares_outstanding,shares_short_df], axis = 1)
                
            
            
            vol_index_values = concat_3m_volume[concat_3m_volume["Average Volume 3m"] <= 800000].index.values
            #print(vol_index_values)
            concat_3m_volume.drop(vol_index_values, inplace=True)
            #print(concat_3m_volume)
                
            #print('-----------------------')
            
            beta_index_values = concat_3m_volume[concat_3m_volume["Beta"] <= 0.8].index.values
            #print(beta_index_values)
            concat_3m_volume.drop(beta_index_values, inplace=True)
            #print(concat_3m_volume)
            
            #print('-----------------------')
            
            share_short_index_values = concat_3m_volume[concat_3m_volume["Percent Shares Short Outstanding"] < 0].index.values
            #print(share_short_index_values)
            concat_3m_volume.drop(share_short_index_values, inplace=True)
            #print(concat_3m_volume)
            
            #print('-----------------------')
             
                
                
                
                
            concat_3m_volume.to_csv("ticker_list_today.csv")
                
               
            
            
            print("TICKER MASTER SHEET QUALITY ASSURANCE COMPLETE")
            
        quality_assurance_current_assets()
        
        break
        
    except:
        print("No Internet Connection, Attempting Reconnection... - Ticker Master Sheet Quality Assurance")
        time.sleep(0.5)
    
    
    
    
    
    
    
    

