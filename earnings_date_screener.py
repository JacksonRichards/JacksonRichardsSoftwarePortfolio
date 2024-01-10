


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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import shutil
import pandas as pd
import os
import warnings
import requests
import glob
import os
from datetime import date
import shutil
import re
import urllib.request

def earnings_date_updater():
    
    try:
        
        urllib.request.urlopen('http://google.com') #Python 3.x
        #print("Internet Connection Detected - Earnings Screener")
        #time.sleep(1)
    
        while True:
            
            print("EARNINGS DATE SCREENER COMMENCING")
            
            start = time.time()
            
            warnings.filterwarnings('ignore')
            
            options = Options()
            options.headless = True
                  
            driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\jacks\Downloads\chromedriver.exe")
            
    
            url = driver.get("https://www.tradingview.com/screener/#signin")
            driver.maximize_window()
            time.sleep(3)
                 
                
            button = driver.find_element(By.CLASS_NAME, 'js-show-email')
            button.click()
     
            time.sleep(2)
            
            username = driver.find_element(By.NAME, "username")
            password = driver.find_element(By.NAME, "password")
            
            
            username.send_keys("jacksonw911@gmail.com")
            password.send_keys("$JenkinsChia9119")
    
            button_sign = driver.find_element(By.CLASS_NAME, "tv-button__loader-item")
            button_sign.click()
       
            time.sleep(5)
            
            #tickers = driver.find_elements(By.CLASS_NAME, "tv-screener__symbol")
            #print(button_sign)
            #print([my_elem.text for my_elem in driver.find_elements(By.CLASS_NAME, "tv-screener__symbol")])
            
            amount_of_results = driver.find_element(By.CLASS_NAME, "js-field-total")
            amount_int = amount_of_results.text
            amount_int = re.sub('[MATCHES]', '', amount_int)
            #print("Amount of Returned Results", amount_int)
            #print(type(amount_of_results))
            
            
            ##print('Finshed Getting Website')
            
            
            end = time.time()
            ##print(end - start)    
            
            start = time.time()
            
            SCROLL_PAUSE_TIME = 5
    
            # Get scroll height
            last_height = driver.execute_script("return document.body.scrollHeight")
            
            "METHOD 1:"
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(SCROLL_PAUSE_TIME)
                
                new_height = driver.execute_script("return document.body.scrollHeight")
                if(new_height == last_height):
                    break
                last_height = new_height
                #print("Recent:", last_height)
            #print("Final:", last_height)
            
            ##print('Finshed Page Scrolling')
            
            end = time.time()
            ##print(end - start)  
            
            start = time.time()
            
            #elements = driver.find_elements(By.CLASS_NAME, "tv-screener__symbol")
            elements_tickers=driver.find_elements(By.CLASS_NAME, "tv-screener__symbol")
            ##print('Finshed Scraping Tickers')
            
            end = time.time()
            ##print(end - start) 
            
            
            start = time.time()
            
            elements_next_earnings_date=driver.find_elements(By.XPATH, "//td[@data-field-key='earnings_release_next_date']")
            ##print('Finshed Scraping Earnings Dates')
            
            
            end = time.time()
            ##print(end - start) 
            
            
            
            
            start = time.time()
    
            tickers_append=[]
            next_earnings_date_append = []
            for review_tickers, review_next_earnings_date in zip(elements_tickers,elements_next_earnings_date):
                tickers_append.append(review_tickers.text)
                next_earnings_date_append.append(review_next_earnings_date.text)
            #print(allreview)
            #print(type(allreview))
            
            #print(exchange_append)
            ##print('Finshed Appending')
            
            end = time.time()
            ##print(end - start) 
            
            
            
            
            
            start = time.time()
            
            tickers_df = pd.DataFrame(tickers_append)
            tickers_df.columns = ['Tickers']
            
            next_earnings_date_df = pd.DataFrame(next_earnings_date_append)
            next_earnings_date_df.columns = ['Next Earnings Date']
            
            #print(exchange_df)
            
            screener_concat = pd.concat([tickers_df, next_earnings_date_df], axis = 1)
            
            screener_concat.to_csv('updated_earnings.csv')   
            
            ##print('Finshed DataFrame')
            #print(allreview)
            #print(len(allreview))
                
            #for elements_ticker in tickers:
                #print(elements_ticker.text)
                #time.sleep(5)
            
            end = time.time()
            ##print(end - start) 
            
            
            
            
            
            
            
            print("EARNING DATES SCREENER COMPLETE")
            
            break
        
        
    except:
        print("No Internet Connection, Attempting Reconnection... - Earnings Screener")
        time.sleep(0.5)
      
      
earnings_date_updater()





