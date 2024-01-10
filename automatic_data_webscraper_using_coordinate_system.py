

import webbrowser
import time
import keyboard
import pyautogui
import urllib.request
import pandas as pd
import os
import shutil

def csv_auto_download():

    print("CSV DATA DOWNLOAD COMMENCING")
    
    while True:
        
        try:
        
            
            ticker_exchange_csv_data = pd.read_csv('ticker_list_today.csv')
            #print(ticker_exchange_csv_data)
            
            tickers = ticker_exchange_csv_data['Tickers'].to_numpy().tolist()
            #print(tickers)
            
            exchange = ticker_exchange_csv_data['Exchange'].to_numpy().tolist()
            #print(exchange)
            
            length_of_tradingview_tickers = len(tickers)
            #print("Length of Tradingview Tickers:", length_of_tradingview_tickers)
            
            #print('----------------------------------')
            
            for items_ticker, items_exchange in zip(tickers, exchange):
            
                if(os.path.exists(r'C:\Users\jacks\Downloads\\'+items_exchange+'_'+items_ticker+', 1.csv')):
                    
                    #print(items_ticker+" in downloads folder, removing now")
                    
                    ticker_file_path = r'C:\Users\jacks\Downloads\\'+items_exchange+'_'+items_ticker+', 1.csv'
        
                    os.remove(ticker_file_path)
                    
                else:
                    nothing = 0
                    #print("No "+items_ticker+" in downloads folder")
                    
                    
            #print('----------------------------------')
                    
                    
            for current_tickers in tickers:
                    
                if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\tradingview_'+current_tickers+'_data.csv')):
                   
                    #print("Removing "+current_tickers+" from list")
                    
                    tickers = list(filter(lambda num: num != current_tickers,
                                  tickers)
                           )
                   
                else:
                    nothing = 0
                    #print("Leaving "+current_tickers+" in list")
                    
            #print(tickers)
        
            
            #url = "https://www.tradingview.com/chart/NBdsDwOp/"
            # Open URL in a new tab, if a browser window is already open.
            #webbrowser.open_new(url)
            #time.sleep(10)
            
            for ticker, download_exchange in zip(tickers,exchange):
                
                url = "https://www.tradingview.com/chart/NBdsDwOp/"
                webbrowser.open_new(url)
                time.sleep(10)
                
                #print(ticker)
                #pyautogui.click(x=107, y=124)
                #time.sleep(3)
                keyboard.write(ticker)
                time.sleep(3)
                pyautogui.press('enter') 
                time.sleep(3)
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('down')
                pyautogui.keyUp('ctrl')
                pyautogui.keyUp('down')
                
                pyautogui.keyDown('alt')
                pyautogui.keyDown('left')
                time.sleep(15)
                pyautogui.keyUp('alt')
                pyautogui.keyUp('left')
                time.sleep(1)
                
                side_button = pyautogui.click(3191, 124)
                # For big 1900x1080 screens 1668 119
                # For big 2280 1080 screens 2305 119
                # For REALLY big 3440x1440 screens 3191 124
                time.sleep(3)
                
                csv_button = pyautogui.click(3291, 331)
                # For big 1900x1080 screens 1774 326
                # For big 2280 1080 screens 2387 326
                # For REALLY big 3440x1440 screens 3291 331
                time.sleep(2)
                
                pyautogui.press('tab') 
                pyautogui.press('tab') 
                pyautogui.press('tab') 
                #time_type_change = pyautogui.click(1065,611)
                time.sleep(2)
                   
                #time_type_change = pyautogui.click(974,649)
                pyautogui.press('enter')   
                time.sleep(2)
                    
                #export_csv = pyautogui.click(1105,700)
                pyautogui.press('up') 
                time.sleep(2)
                
                pyautogui.press('enter')   
                time.sleep(3)
                
                original = r'C:\Users\jacks\Downloads\\'+download_exchange+'_'+ticker+', 1.csv'
                #print(original)
                target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\tradingview_'+ticker+'_data.csv'
                #print(target)
                shutil.move(original, target)
                #print(ticker, "CSV data scraped")
                time.sleep(2)
                
                downloads_task_bar_close = pyautogui.click(3423, 1364)
                # For big 1900x1080 screens 1898 1000
                # For REALLY big 3440x1440 screens 3423 1364
                time.sleep(3)
            
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(3)  
                pyautogui.press('enter') 
                time.sleep(1)  
            
            print("CSV DATA DOWNLOAD COMPLETE")
            
            break
            
            
        
            
        
        except:
                
            print("No Internet Connection, Attempting Reconnection... - CSV Auto Downloader")
            time.sleep(0.5)
    
    
csv_auto_download()






















