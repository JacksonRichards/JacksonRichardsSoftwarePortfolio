
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import pyautogui
import shutil
import pandas as pd
import schedule
import os
import urllib.request

def csv_auto_download():
    print("CSV DATA DOWNLOAD COMMENCING")
    
    while True:
    
        try:
            
            urllib.request.urlopen('http://google.com') #Python 3.x
            print("Internet Connection Detected - CSV Auto Downloader")
            
            ticker_exchange_csv_data = pd.read_csv('ticker_list_today.csv')
            #print(ticker_exchange_csv_data)
            
            tickers = ticker_exchange_csv_data['Tickers'].to_numpy().tolist()
            #print(tickers)
            
            length_of_tradingview_tickers = len(tickers)
            #print("Length of Tradingview Tickers:", length_of_tradingview_tickers)
            
            #print('----------------------------------')
            
            for items_ticker in tickers:
            
                if(os.path.exists(r'C:\Users\jacks\Downloads\BATS_'+items_ticker+', 1.csv')):
                    
                    #print(items_ticker+" in downloads folder, removing now")
                    
                    ticker_file_path = r'C:\Users\jacks\Downloads\BATS_'+items_ticker+', 1.csv'
        
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
                   
                     
            
            
            driver = webdriver.Chrome(r"C:\Users\jacks\Downloads\chromedriver.exe")
            
            
            
            driver.get("https://www.tradingview.com/#signin")
            
            
            
            # get https://www.geeksforgeeks.org/
            driver.get("https://www.tradingview.com/#signin")
              
            # Maximize the window and let code stall 
            # for 10s to properly maximise the window.
            #driver.maximize_window()
            #time.sleep(3)
              
            # Obtain button by link text and click.
            button = driver.find_element(By.CLASS_NAME, 'js-show-email')
            button.click()
            
            #time.sleep(60)
            
            #button = driver.find_element_by_link_text("Sign in")
            #button.click()
            
            time.sleep(3)
            
            username = driver.find_element(By.NAME, "username")
            password = driver.find_element(By.NAME, "password")
            
            
            username.send_keys("nickcoch@gmail.com")
            password.send_keys("Testing2022!")
            
            # click login button
            button_sign = driver.find_element(By.CLASS_NAME, "tv-button__loader-item")
            button_sign.click()
            driver.maximize_window()
            time.sleep(7)
            query = driver.find_element(By.LINK_TEXT, 'Chart')
            query.click()
            #button.click()
            time.sleep(5)
            
            
            
            for ticker in tickers:
                symbol_search = driver.find_element(By.XPATH, '//div[@title="Symbol Search"]').click()
                time.sleep(5)
                backspace = driver.find_element(By.CLASS_NAME, "search-eYX5YvkT").send_keys(Keys.BACKSPACE)
                time.sleep(1)
                ticker_placement = driver.find_element(By.CLASS_NAME, "search-eYX5YvkT")
                ticker_placement.send_keys(ticker)
                time.sleep(0.5)
                return_key = driver.find_element(By.CLASS_NAME, "search-eYX5YvkT").send_keys(Keys.RETURN)
                time.sleep(2)
                pyautogui.press('1') 
                time.sleep(0.5)
                pyautogui.press('enter') 
                time.sleep(2)
                
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
                time.sleep(20)
                pyautogui.keyUp('alt')
                pyautogui.keyUp('left')
                time.sleep(1)
                
                #side_button = driver.find_element(By.CLASS_NAME, "js-save-load-menu-open-button")
                #side_button.click()
                #time.sleep(1)
                
                side_button = pyautogui.click(2305,119)
                # For small 1900x1080 screens 1608 155
                # For big 1900x1080 screens 1668 119
                # For big 2280 1080 screens 2305 119
                time.sleep(3)
                
                csv_button = pyautogui.click(2387,326)
                # For small 1900x1080 screens 1727 408
                # For big 1900x1080 screens 1774 326
                #For big 2280 1080 screens 2387 326
                time.sleep(3)
                
                time_format = driver.find_element(By.ID, "time-format-select")
                time_format.click()
                pyautogui.keyDown('up')
                pyautogui.keyUp('up')
                pyautogui.press('enter') 
                time.sleep(4)
                original = r'C:\Users\jacks\Downloads\BATS_'+ticker+', 1.csv'
                target = r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\tradingview_'+ticker+'_data.csv'
                shutil.move(original, target)
                #print(ticker, "CSV data scraped")
                time.sleep(1)
                driver.refresh()
                pyautogui.press('enter') 
                time.sleep(5)
                
            driver.close()
        
            print("CSV DATA DOWNLOAD COMPLETE")
            
            break
            
        except:
            
            print("No Internet Connection, Attempting Reconnection... - CSV Auto Downloader")
            time.sleep(0.5)
            
            driver.close()
            
            
csv_auto_download()






















