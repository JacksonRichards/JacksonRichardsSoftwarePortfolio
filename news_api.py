
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import numpy as np
import re
import time
import warnings
from datetime import datetime
import pytz
import random
import os

warnings.filterwarnings('ignore')

##tickers = ['aapl']
##description = ['Apple, Inc.']

ticker_master_sheet = pd.read_csv('ticker_list_today.csv')

ticker_master_sheet['Market capitalization'] = ticker_master_sheet['Market capitalization'].str.replace(r'-', '0', regex=True)
ticker_master_sheet['Market capitalization'] = ticker_master_sheet['Market capitalization'].astype(float)
ticker_master_sheet = ticker_master_sheet[ticker_master_sheet['Market capitalization'] > 100000000000]  

ticker_master_sheet = ticker_master_sheet.sample(frac = 1)
tickers = ticker_master_sheet['Tickers'].to_numpy().tolist()
description = ticker_master_sheet['Description'].to_numpy().tolist()
volume = ticker_master_sheet['Description'].to_numpy().tolist()




# TICKER BASED URL: "https://www.google.com/search?q="+ticker.lower()+"+stock+news&sca_esv=4c1f4100c44949b9&sca_upv=1&rlz=1C1VDKB_enUS1051US1051&tbm=nws&sxsrf=ADLYWIIZOGK-6409ne0321rMStXeQ-vsSQ:1719027103163&source=lnt&tbs=sbd:1&sa=X&ved=2ahUKEwjpo9_-ou6GAxV5MDQIHeivCtoQpwV6BAgCEBQ&biw=969&bih=941&dpr=1.5"
# FULL COMPANY NAME: "https://www.google.com/search?q=ChinaNaturalResourcesInc.%0D%0Astock+news&sca_esv=4c1f4100c44949b9&sca_upv=1&rlz=1C1VDKB_enUS1051US1051&biw=1664&bih=941&tbs=sbd%3A1&tbm=nws&sxsrf=ADLYWIIF1eBL5pO0FiCPTde5h320zDK_Vw%3A1719216408980&ei=GCl5ZsTGO6Ti0PEPkI230A4&ved=0ahUKEwjEsuWa5POGAxUkMTQIHZDGDeoQ4dUDCA0&uact=5&oq=China+Natural+Resources%2C+Inc.%0D%0Astock+news&gs_lp=Egxnd3Mtd2l6LW5ld3MiKENoaW5hIE5hdHVyYWwgUmVzb3VyY2VzLCBJbmMuCnN0b2NrIG5ld3MyChAAGIAEGEMYigUyBRAAGIAEMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESN4OUO0CWO0CcAB4AJABAZgBa6ABuwGqAQMxLjG4AQPIAQD4AQL4AQGYAgGgAlaYAwCIBgGSBwExoAe6Cw&sclient=gws-wiz-news"

class_name = "SoaBEf"
# "MjjYud" - USED FOR ALL CURRENTLY VISIBLE ARTICLES
# "SoaBEf" - USED FOR MOST RECENT ARTICLE

options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
options.add_argument('excludeSwitch')
#options.add_argument("start-maximized")
options.add_argument("--window-position=-9999999,0")
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
#print('----------------')

def StockNewsAPI():

    ###time.sleep(1)

    #driver.get("https://www.google.com/search?q="+descriptions+"%0D%0Astock+news&sca_esv=4c1f4100c44949b9&sca_upv=1&rlz=1C1VDKB_enUS1051US1051&biw=1664&bih=941&tbs=sbd%3A1&tbm=nws&sxsrf=ADLYWIIF1eBL5pO0FiCPTde5h320zDK_Vw%3A1719216408980&ei=GCl5ZsTGO6Ti0PEPkI230A4&ved=0ahUKEwjEsuWa5POGAxUkMTQIHZDGDeoQ4dUDCA0&uact=5&oq=China+Natural+Resources%2C+Inc.%0D%0Astock+news&gs_lp=Egxnd3Mtd2l6LW5ld3MiKENoaW5hIE5hdHVyYWwgUmVzb3VyY2VzLCBJbmMuCnN0b2NrIG5ld3MyChAAGIAEGEMYigUyBRAAGIAEMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESN4OUO0CWO0CcAB4AJABAZgBa6ABuwGqAQMxLjG4AQPIAQD4AQL4AQGYAgGgAlaYAwCIBgGSBwExoAe6Cw&sclient=gws-wiz-news")

    driver.get("https://www.google.com/search?q="+ticker+"+stock+news&sca_esv=28f8fab5923385a6&rlz=1C1ONGR_enUS1036US1036&biw=1248&bih=1270&tbs=sbd%3A1&tbm=nws&sxsrf=ADLYWIISAzbuToPdJ6W93y2ehpTds7np-A%3A1729032297691&ei=afAOZ4L0KfWt0PEPv4CfkAI&ved=0ahUKEwjCzKKfu5GJAxX1FjQIHT_AByIQ4dUDCA0&uact=5&oq=JNJ+stock+news&gs_lp=Egxnd3Mtd2l6LW5ld3MiDkpOSiBzdG9jayBuZXdzMhEQABiABBiRAhixAxiDARiKBTIREAAYgAQYkQIYsQMYgwEYigUyBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMggQABiABBiiBEiZHVDQEliIFXAAeACQAQCYAfIBoAGbBKoBBTIuMS4xuAEDyAEA-AEBmAIEoAKjBMICCxAAGIAEGJECGIoFwgIFEAAYgATCAgYQABgHGB7CAggQABgHGAgYHpgDAIgGAZIHBTIuMS4xoAfDGA&sclient=gws-wiz-news")

    search_box = driver.find_element(By.CLASS_NAME, class_name).text
    search_box = search_box.replace('...', '')
    search_box = search_box.replace(',', '')
    article_headline = search_box.split()
    article_headline = " ".join(article_headline[0:len(article_headline)-4])
        
    timeframe_information = search_box.split()[-3:-1]
    elapsed_time = timeframe_information[0]
    unit_of_time = timeframe_information[1]

    tz_LA = pytz.timezone('America/Los_Angeles') 
    datetime_LA = datetime.now(tz_LA)

    ticker_symbol = []
    descpt = []
    est_amt_of_elapsed_time = []
    uot = []
    est_post_time = []
    article_headline_tone = []
    tone_score = []
    impact_score = []
    potential_value_score = []
    current_price_per_share = []
    current_volume = []
    time_recorded = []
    art_headline = []

    ticker_symbol.append(ticker)
    descpt.append(descriptions)
    est_amt_of_elapsed_time.append(elapsed_time)
    uot.append(unit_of_time)
    if(unit_of_time == 'hours'):
        current_hour = datetime_LA.hour
        ept_calc = current_hour-int(elapsed_time)
        if(ept_calc < 0):
            #ept_calc = (24-int(elapsed_time))
            ept_calc = (24-int(elapsed_time))+6+12
        est_post_time.append(str(ept_calc)+':00')
    else:
        est_post_time.append('NAN')
    article_headline_tone.append('NAN')
    tone_score.append('NAN')
    impact_score.append('NAN')
    potential_value_score.append('NAN')
    time_recorded.append(datetime_LA)
    current_price_per_share.append('NAN')
    current_volume.append('NAN')
    art_headline.append(article_headline)

    ticker_symbol = pd.DataFrame(ticker_symbol)
    descpt = pd.DataFrame(descpt)
    est_amt_of_elapsed_time = pd.DataFrame(est_amt_of_elapsed_time)
    unit_of_time = pd.DataFrame(uot)
    est_post_time = pd.DataFrame(est_post_time)
    article_headline_tone = pd.DataFrame(article_headline_tone)
    tone_score = pd.DataFrame(tone_score)
    impact_score = pd.DataFrame(impact_score)
    potential_value_score = pd.DataFrame(potential_value_score)
    time_recorded = pd.DataFrame(time_recorded)
    current_price_per_share = pd.DataFrame(current_price_per_share)
    current_volume = pd.DataFrame(current_volume)
    article_headline = pd.DataFrame(art_headline)

    final_concat = pd.concat([ticker_symbol,descpt,est_amt_of_elapsed_time,unit_of_time,est_post_time,article_headline_tone,tone_score,impact_score,potential_value_score,time_recorded,current_price_per_share,current_volume,article_headline], axis=1)
    final_concat.columns = ['Ticker Symbol','Description','Est. Amt. of Elapsed Time','Unit of Time','Est. Post Time','Article Headline Tone','Tone Score','Impact Score','Potential Value Score','Time Recorded','Current PPS','Current Volume','Article Headline']
    final_concat.to_csv('article_database.csv', mode='a', header=False, index=False)

    ##print(article_headline)
    ##print("TICKER:", ticker.upper(),"-", "EST. AMOUNT OF ELAPSED TIME:", elapsed_time)
    ##print('----------------')

    #driver.close()



i = 0
for ticker, descriptions in zip(tickers, description):
    
    try:

        StockNewsAPI()
        
    except:
        while True:
            try:
                print("Unable to find element in first time, trying it again")

                #driver.close()

                #os.system('ipconfig/flushdns')

                StockNewsAPI()

                break
            except:
                continue
    i = i + 1
    print("ITERATION:", i)
    print('----------------')

#driver.quit()





