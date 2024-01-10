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

def stock_screener():
    
    while True:
        
        print("STOCK SCREENER COMMENCING")
        
        warnings.filterwarnings('ignore')
        
        options = Options()
        options.headless = True
              
        driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Jackson\Downloads\chromedriver.exe")
        

        url = driver.get("https://www.tradingview.com/screener/#signin")
        driver.maximize_window()
        time.sleep(3)
             
            
        button = driver.find_element(By.CLASS_NAME, 'js-show-email')
        button.click()
 
        time.sleep(2)
        
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        
        
        username.send_keys("XXXXXX@gmail.com")
        password.send_keys("XXXXXX")

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
        #elements = driver.find_elements(By.CLASS_NAME, "tv-screener__symbol")
        elements_tickers=driver.find_elements(By.CLASS_NAME, "tv-screener__symbol")
        elements_value_traded=driver.find_elements(By.XPATH, "//td[@data-field-key='Value.Traded']")
        elements_volume=driver.find_elements(By.XPATH, "//td[@data-field-key='volume']")
        elements_close=driver.find_elements(By.XPATH, "//td[@data-field-key='close']")
        elements_beta_1y=driver.find_elements(By.XPATH, "//td[@data-field-key='beta_1_year']")
        elements_market_cap=driver.find_elements(By.XPATH, "//td[@data-field-key='market_cap_basic']")
        elements_exchange=driver.find_elements(By.XPATH, "//td[@data-field-key='exchange']")
        elements_90d_avg=driver.find_elements(By.XPATH, "//td[@data-field-key='average_volume_90d_calc']")
        elements_next_earnings_date=driver.find_elements(By.XPATH, "//td[@data-field-key='earnings_release_next_date']")
        #print(elements_tickers)
        #print('---------')
        #print(len(elements_tickers))
        #if(len(elements_tickers) >= int(amount_int)):
            #break
        
        
        
        
        

        tickers_append=[]
        value_traded_append = []
        volume_append = []
        close_price_append = []
        beta_1y_append = []
        market_cap_append = []
        exchange_append = []
        NinetyD_avg_append = []
        next_earnings_date_append = []
        for review_tickers, review_value_traded, review_volume, review_close_price, review_beta_1y, review_market_cap, review_exchange, review_90d_avg, review_next_earnings_date in zip(elements_tickers,elements_value_traded,elements_volume,elements_close,elements_beta_1y,elements_market_cap,elements_exchange,elements_90d_avg,elements_next_earnings_date):
            tickers_append.append(review_tickers.text)
            value_traded_append.append(review_value_traded.text)
            volume_append.append(review_volume.text)
            close_price_append.append(review_close_price.text)
            beta_1y_append.append(review_beta_1y.text)
            market_cap_append.append(review_market_cap.text)
            exchange_append.append(review_exchange.text)
            NinetyD_avg_append.append(review_90d_avg.text)
            next_earnings_date_append.append(review_next_earnings_date.text)
        #print(allreview)
        #print(type(allreview))
        
        #print(exchange_append)
        
        
        
        
        
        
        tickers_df = pd.DataFrame(tickers_append)
        tickers_df.columns = ['Tickers']
        value_traded_df = pd.DataFrame(value_traded_append)
        value_traded_df.columns = ['Value Traded']
        volume_df = pd.DataFrame(volume_append)
        volume_df.columns = ['Current Volume']
        close_price_df = pd.DataFrame(close_price_append)
        close_price_df.columns = ['Close Price']
        beta_1y_df = pd.DataFrame(beta_1y_append)
        beta_1y_df.columns = ['Beta 1yr']
        market_cap_df = pd.DataFrame(market_cap_append)
        market_cap_df.columns = ['Market CAP']
        exchange_df = pd.DataFrame(exchange_append)
        exchange_df.columns = ['Exchange']
        NinetyD_avg_df = pd.DataFrame(NinetyD_avg_append)
        NinetyD_avg_df.columns = ['Volume 90d Average']
        next_earnings_date_df = pd.DataFrame(next_earnings_date_append)
        next_earnings_date_df.columns = ['Next Earnings Date']
        
        #print(exchange_df)
        
        screener_concat = pd.concat([tickers_df, exchange_df, market_cap_df, NinetyD_avg_df, beta_1y_df, value_traded_df, volume_df, close_price_df, next_earnings_date_df], axis = 1)
        
        screener_concat.to_csv('stock_screener_results.csv')   
        
        
        #print(allreview)
        #print(len(allreview))
            
        #for elements_ticker in tickers:
            #print(elements_ticker.text)
            #time.sleep(5)
        
            
        
        '''  
        METHOD 2:
        
        screener_button = driver.find_element(By.CLASS_NAME, 'tv-screener-toolbar__button--export')
        screener_button.click()
        
        time.sleep(5)
        
        driver.close()
        
        
        today_initial_data = date.today()
        current_date = today_initial_data.strftime("%Y-%m-%d")


        ADD TRASNFERRING DATA FILE FROM DOWNLOADS TO DESIRED PATH
        '''
        
        
        
        
        
        print("STOCK SCREENER COMPLETE")
        
        break
      
      
stock_screener()





