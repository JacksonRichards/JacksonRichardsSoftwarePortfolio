
import pandas as pd
import numpy as np
import os


def daily_selector_function():
    
    print("DAILY SELECTOR COMMENCING")

    #print("Initiating Automated Daily Selector")
    if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') == True):
        os.remove("ticker_parameter_grades.csv")
    os.rename("yesterday_ticker_parameter_grades.csv", "ticker_parameter_grades.csv")
    parameter_set_selector = pd.read_csv('portfolio_view_micro_view.csv')
    parameter_set_selector_percentage_history = parameter_set_selector['Percentage History'].to_numpy().tolist()
    ending_percentage = parameter_set_selector_percentage_history[len(parameter_set_selector_percentage_history)-1]         
    if(ending_percentage > 0):
        daily_selector_df = pd.DataFrame([True])
        daily_selector_df.columns = ['Daily Selector']
        daily_selector_df.to_csv('daily_selector_logic.csv')
    else:
        if(os.path.exists(r'C:\Users\jacks\Desktop\PMax Algorithm Software - L\ticker_parameter_grades.csv') == True):
            os.remove("ticker_parameter_grades.csv")


    print("DAILY SELECTOR COMPLETE")


daily_selector_function()
