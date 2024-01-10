

import pandas as pd
from statistics import mean
import numpy as np
from datetime import datetime
import csv

def record_analysis():
    
    print("RECORD ANALYSIS COMMENCING")
    
    filename = "macro_overview.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()
    
    '''
    csv_setup_macro = pd.read_csv('macro_overview.csv')
    csv_setup_macro.columns = ['Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable']
    csv_setup_macro.to_csv("macro_overview.csv")
    '''
    
    with open(filename, 'a', newline='') as csvfile:
        my_writer = csv.writer(csvfile)
        my_writer.writerow(('Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable'))
        
    
    
    now = datetime.now()
    current_date = now.strftime('%m/%d/%Y')
    #print("Current Date:", current_date)
    
    trading_records_master_sheet = pd.read_csv('overall_records.csv')
    pd.set_option('display.max_columns', 10000)
    #print(trading_records_master_sheet)
    
    all_total_closed_trades = trading_records_master_sheet['Average_Closed_Trades - BT']
    all_total_closed_trades = all_total_closed_trades[all_total_closed_trades.notna()]
    all_total_closed_trades.dropna(axis=0)
    #print(all_total_closed_trades)
    all_total_closed_trades.to_numpy().tolist()
    #print(all_total_closed_trades)
    
    #print('------------------------------')
    
    all_predic_numbers = trading_records_master_sheet['Predictive_Model_Average']
    all_predic_numbers = all_predic_numbers[all_predic_numbers.notna()]
    all_predic_numbers.dropna(axis=0)
    #print(all_predic_numbers)
    all_predic_numbers.to_numpy().tolist()
    #print(all_predic_numbers)
    
    
    all_percentage_numbers = trading_records_master_sheet['Percentage_Change']
    all_percentage_numbers = all_percentage_numbers[all_percentage_numbers.notna()]
    all_percentage_numbers.dropna(axis=0)
    #print(all_predic_numbers)
    all_percentage_numbers.to_numpy().tolist()
    #print(all_predic_numbers)
    
    
    all_binary_profit_loss = trading_records_master_sheet['gain_loss']
    all_binary_profit_loss = all_binary_profit_loss[all_binary_profit_loss.notna()]
    all_binary_profit_loss.dropna(axis=0)
    #print(all_predic_numbers)
    all_binary_profit_loss.to_numpy().tolist()
    #print(all_predic_numbers)
    
    
    total_number_closed_trades_average = all_total_closed_trades[len(all_total_closed_trades)]
    #print(total_number_closed_trades_average)
    total_point_average = all_predic_numbers[len(all_predic_numbers)]
    #print(total_point_average)
    
    '''
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    
    for items_all_total_closed_trades in all_total_closed_trades:
        
        
        if(total_point_average < 7 and total_number_closed_trades_average < 169.5 and total_number_closed_trades_average >= 150):
            #print('Vanilla Settings')
            
            print('total_point_average < 7 and total_number_closed_trades_average < 169.5 and total_number_closed_trades_average >= 150')
            #print("TOP: NORMAL, BOTTOM: SWITCH")
            one.append(items_all_total_closed_trades)
                        
                 
        elif(total_point_average < 7 and total_number_closed_trades_average >= 179):
            #print('720 Settings Low TPA')
            
            print('total_point_average < 7 and total_number_closed_trades_average >= 17')
            #print("TOP: NORMAL, BOTTOM: SWITCH")
            two.append(items_all_total_closed_trades)
                  
                        
        elif(total_point_average >= 7 and total_number_closed_trades_average >= 179):
            #print('720 Settings High TPA')
            
            print('total_point_average >= 7 and total_number_closed_trades_average >= 179')
            #print("TOP: SWITCH, BOTTOM: NORMAL")
            three.append(items_all_total_closed_trades)       
                     
        elif(total_point_average >= 7 and total_number_closed_trades_average < 169.5 and total_number_closed_trades_average >= 150):
            #print('360 Settings High TPA')
            
            print('total_point_average >= 7 and total_number_closed_trades_average < 169.5 and total_number_closed_trades_average >= 150')
            #print("TOP: SWITCH, BOTTOM: NORMAL")
            four.append(items_all_total_closed_trades)
                      
                        
        elif(total_point_average < 7 and total_number_closed_trades_average >= 169.5 and total_number_closed_trades_average < 179):
            #print('360 Settings High TCT')
            
            print('total_point_average < 7 and total_number_closed_trades_average >= 169.5 and total_number_closed_trades_average < 179')
            #print("TOP: SWITCH, BOTTOM: NORMAL")
            five.append(items_all_total_closed_trades)   
            
                    
        elif(total_point_average >= 7 and total_number_closed_trades_average >= 169.5 and total_number_closed_trades_average < 179):
            #print('360 Settings High Both TPA and TCT')
            
            print('total_point_average >= 7 and total_number_closed_trades_average >= 169.5 and total_number_closed_trades_average < 179')
            #print("TOP: SWITCH, BOTTOM: NORMAL")
            six.append(items_all_total_closed_trades)
    
        elif(total_point_average < 7 and total_number_closed_trades_average < 150 and total_number_closed_trades_average >= 140):
            #print('Vanilla Settings')
            
            print('total_point_average < 7 and total_number_closed_trades_average < 150 and total_number_closed_trades_average >= 140')
            #print("TOP: NORMAL, BOTTOM: SWITCH")
            seven.append(items_all_total_closed_trades)         
                    
        elif(total_point_average >= 7 and total_number_closed_trades_average < 150 and total_number_closed_trades_average >= 140):
            #print('Vanilla Settings')
            
            print('total_point_average >= 7 and total_number_closed_trades_average < 150 and total_number_closed_trades_average >= 140')
            #print("TOP: SWITCH, BOTTOM: NORMAL")
            eight.append(items_all_total_closed_trades)          
                 
        elif(total_point_average < 7 and total_number_closed_trades_average >= 126 and total_number_closed_trades_average < 140):
            #print('Vanilla Settings')
            
            print('total_point_average < 7 and total_number_closed_trades_average >= 126 and total_number_closed_trades_average < 140')
            #print("TOP: NORMAL, BOTTOM: SWITCH")
            nine.append(items_all_total_closed_trades)          
                        
        elif(total_point_average >= 7 and total_number_closed_trades_average >= 126 and total_number_closed_trades_average < 140):
            #print('Vanilla Settings')
            
            print('total_point_average >= 7 and total_number_closed_trades_average >= 126 and total_number_closed_trades_average < 140')
            #print("TOP: SWITCH, BOTTOM: NORMAL")
            ten.append(items_all_total_closed_trades)
    
        elif(total_point_average < 7 and total_number_closed_trades_average < 126):
            #print('Vanilla Settings')
            
            print('total_point_average < 7 and total_number_closed_trades_average < 126')
            #print("TOP: SWITCH, BOTTOM: NORMAL")
            eleven.append(items_all_total_closed_trades)
            
        elif(total_point_average >= 7 and total_number_closed_trades_average < 126):
            #print('Vanilla Settings')
            
            print('total_point_average >= 7 and total_number_closed_trades_average < 126')
            #print("TOP: NORMAL, BOTTOM: SWITCH") 
            twelve.append(items_all_total_closed_trades)
            
    '''
    num_179_200 = []
    perc_num_179_200 = []
    binary_profit_loss_num_179_200 = []
    
    num_1695_17899 = []
    perc_num_1695_17899 = []
    binary_profit_loss_num_1695_17899 = []
    
    num_160_16949 = []
    perc_num_160_16949= []
    binary_profit_loss_num_160_16949 = []
    
    num_150_15999 = []
    perc_num_150_15999 = []
    binary_profit_loss_num_150_15999 = []
    
    num_140_14999 = []
    perc_num_140_14999 = []
    binary_profit_loss_num_140_14999 = []
    
    num_126_13999 = []
    perc_num_126_13999 = []
    binary_profit_loss_num_126_13999 = []
    
    num_100_12599 = []
    perc_num_100_12599 = []
    binary_profit_loss_num_100_12599 = []
    
    
    for items_all_total_closed_trades, items_all_percentage_numbers, items_all_binary_profit_loss in zip(all_total_closed_trades, all_percentage_numbers, all_binary_profit_loss):      
            
        if(items_all_total_closed_trades >= 179 and items_all_total_closed_trades <= 200):
            num_179_200.append(items_all_total_closed_trades)
            perc_num_179_200.append(items_all_percentage_numbers)
            binary_profit_loss_num_179_200.append(items_all_binary_profit_loss)
            
        if(items_all_total_closed_trades >= 169.5 and items_all_total_closed_trades <= 178.99):
            num_1695_17899.append(items_all_total_closed_trades)
            perc_num_1695_17899.append(items_all_percentage_numbers)
            binary_profit_loss_num_1695_17899.append(items_all_binary_profit_loss)
            
        if(items_all_total_closed_trades >= 160 and items_all_total_closed_trades <= 169.49):
            num_160_16949.append(items_all_total_closed_trades)
            perc_num_160_16949.append(items_all_percentage_numbers)
            binary_profit_loss_num_160_16949.append(items_all_binary_profit_loss)
            
        if(items_all_total_closed_trades >= 150 and items_all_total_closed_trades <= 159.99):
            num_150_15999.append(items_all_total_closed_trades)
            perc_num_150_15999.append(items_all_percentage_numbers)
            binary_profit_loss_num_150_15999.append(items_all_binary_profit_loss)
            
        if(items_all_total_closed_trades >= 140 and items_all_total_closed_trades <= 149.99):
            num_140_14999.append(items_all_total_closed_trades)
            perc_num_140_14999.append(items_all_percentage_numbers)
            binary_profit_loss_num_140_14999.append(items_all_binary_profit_loss)
            
        if(items_all_total_closed_trades >= 126 and items_all_total_closed_trades <= 139.99):
            num_126_13999.append(items_all_total_closed_trades)
            perc_num_126_13999.append(items_all_percentage_numbers)
            binary_profit_loss_num_126_13999.append(items_all_binary_profit_loss)
            
        if(items_all_total_closed_trades >= 100 and items_all_total_closed_trades <= 125.99):
            num_100_12599.append(items_all_total_closed_trades)
            perc_num_100_12599.append(items_all_percentage_numbers)
            binary_profit_loss_num_100_12599.append(items_all_binary_profit_loss)
            
    
    #print(perc_num_179_200) 
    #print(perc_num_1695_17899) 
    #print(perc_num_160_16949) 
    #print(perc_num_150_15999)         
    #print(perc_num_140_14999)       
    #print(perc_num_126_13999)       
    #print(perc_num_100_12599) 
    
    
    
    
    
    
    
    
    if(len(num_179_200)-1 == -1):
        nothing = 0
    else:
        mean_num_179_200 = mean(num_179_200)
        #print("Average mean:", mean_num_179_200)
        mean_num_179_200_df = pd.DataFrame([mean_num_179_200])
        #print(mean_num_179_200_df)
        
        sum_num_179_200 = sum(perc_num_179_200)*100
        #print("Percentage Summation:", sum_num_179_200)
        sum_num_179_200_df = pd.DataFrame([sum_num_179_200])
        #print(sum_num_179_200_df)
          
        binary_sum_num_179_200 = sum(binary_profit_loss_num_179_200)
        #print("Win Amount:", binary_sum_num_179_200)
             
        length_binary_sum_num_179_200 = len(binary_profit_loss_num_179_200)
        #print("Amount of Records:", length_binary_sum_num_179_200)
        
        percentage_profit_loss_num_179_200 = (binary_sum_num_179_200/length_binary_sum_num_179_200)*100
        #print("Percentage of Trades Profitable:", percentage_profit_loss_num_179_200)
        percentage_profit_loss_num_179_200_df = pd.DataFrame([percentage_profit_loss_num_179_200])
        #print(percentage_profit_loss_num_179_200_df)
        
        
        date_updated_df = pd.DataFrame([current_date])
        zone_df = pd.DataFrame(['179_200'])
        macro_overview = pd.read_csv('macro_overview.csv')
        #print(macro_overview)
        macro_concat_179_200 = pd.concat([date_updated_df,zone_df,mean_num_179_200_df,zone_df,sum_num_179_200_df,percentage_profit_loss_num_179_200_df], axis=1)
        macro_concat_179_200.columns = ['Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable']
        #print(macro_concat_179_200)
        macro_concat_179_200.to_csv('macro_overview.csv', mode='a', index=False, header=False)
        
        
           
    if(len(num_1695_17899)-1 == -1):
        nothing = 0
    else:
        mean_num_1695_17899 = mean(num_1695_17899)
        #print("Average mean:", mean_num_1695_17899)
        mean_num_1695_17899_df = pd.DataFrame([mean_num_1695_17899])
        #print(mean_num_1695_17899_df)
        
        sum_num_1695_17899 = sum(perc_num_1695_17899)*100
        #print("Percentage Summation:", sum_num_1695_17899)
        sum_num_1695_17899_df = pd.DataFrame([sum_num_1695_17899])
        #print(sum_num_1695_17899_df)
        
        binary_sum_num_1695_17899 = sum(binary_profit_loss_num_1695_17899)
        #print("Win Amount:", binary_sum_num_1695_17899)
        
        length_binary_sum_num_1695_17899 = len(binary_profit_loss_num_1695_17899)
        #print("Amount of Records:", length_binary_sum_num_1695_17899)
        
        percentage_profit_loss_num_1695_17899 = (binary_profit_loss_num_1695_17899/length_binary_sum_num_1695_17899)*100
        #print("Percentage of Trades Profitable:", percentage_profit_loss_num_1695_17899)
        percentage_profit_loss_num_1695_17899_df = pd.DataFrame([percentage_profit_loss_num_1695_17899])
        #print(percentage_profit_loss_num_1695_17899_df)
        
        
        date_updated_df = pd.DataFrame([current_date])
        zone_df = pd.DataFrame(['1695-17899'])
        macro_overview = pd.read_csv('macro_overview.csv')
        #print(macro_overview)
        macro_concat_1695_17899 = pd.concat([date_updated_df,zone_df,mean_num_1695_17899_df,zone_df,sum_num_1695_17899_df,percentage_profit_loss_num_1695_17899_df], axis=1)
        macro_concat_1695_17899.columns = ['Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable']
        #print(macro_concat_1695_17899)
        macro_concat_1695_17899.to_csv('macro_overview.csv', mode='a', index=False, header=False)
        
        
        
        
    if(len(num_160_16949)-1 == -1):
        nothing = 0
    else:
        mean_num_160_16949 = mean(num_160_16949)
        #print("Average mean:", mean_num_160_16949)
        mean_num_160_16949_df = pd.DataFrame([mean_num_160_16949])
        #print(mean_num_160_16949_df)
        
        
        sum_num_160_16949 = sum(perc_num_160_16949)*100
        #print("Percentage Summation:", sum_num_160_16949)
        sum_num_160_16949_df = pd.DataFrame([sum_num_160_16949])
        #print(sum_num_160_16949_df)
        
        binary_sum_num_160_16949 = sum(binary_profit_loss_num_160_16949)
        #print("Win Amount:", binary_sum_num_160_16949)
        
        length_binary_sum_num_160_16949 = len(binary_profit_loss_num_160_16949)
        #print("Amount of Records:", length_binary_sum_num_160_16949)
        
        percentage_profit_loss_num_160_16949 = (binary_sum_num_160_16949/length_binary_sum_num_160_16949)*100
        #print("Percentage of Trades Profitable:", percentage_profit_loss_num_160_16949)
        percentage_profit_loss_num_160_16949_df = pd.DataFrame([percentage_profit_loss_num_160_16949])
        #print(percentage_profit_loss_num_160_16949_df)
        
        
        
        
        
        date_updated_df = pd.DataFrame([current_date])
        zone_df = pd.DataFrame(['160_16949'])
        macro_overview = pd.read_csv('macro_overview.csv')
        #print(macro_overview)
        macro_concat_160_16949 = pd.concat([date_updated_df,zone_df,mean_num_160_16949_df,zone_df,sum_num_160_16949_df,percentage_profit_loss_num_160_16949_df], axis=1)
        macro_concat_160_16949.columns = ['Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable']
        #print(macro_concat_160_16949)
        macro_concat_160_16949.to_csv('macro_overview.csv', mode='a', index=False, header=False)
        
        
        
        
        
        
        
    if(len(num_150_15999)-1 == -1):
        nothing = 0
    else:
        mean_num_150_15999 = mean(num_150_15999)
        #print("Average mean:", mean_num_150_15999)
        mean_num_150_15999_df = pd.DataFrame([mean_num_150_15999])
        #print(mean_num_150_15999_df)
             
        sum_num_150_15999 = sum(perc_num_150_15999)*100
        #print("Percentage Summation:", sum_num_150_15999)
        sum_num_150_15999_df = pd.DataFrame([sum_num_150_15999])
        #print(sum_num_150_15999_df)
         
        binary_sum_num_150_15999 = sum(binary_profit_loss_num_150_15999)
        #print("Win Amount:", binary_sum_num_150_15999)
        
        length_binary_sum_num_150_15999 = len(binary_profit_loss_num_150_15999)
        #print("Amount of Records:", length_binary_sum_num_150_15999)
        
        percentage_profit_loss_num_150_15999 = (binary_sum_num_150_15999/length_binary_sum_num_150_15999)*100
        #print("Percentage of Trades Profitable:", percentage_profit_loss_num_150_15999)
        percentage_profit_loss_num_150_15999_df = pd.DataFrame([percentage_profit_loss_num_150_15999])
        #print(percentage_profit_loss_num_150_15999_df)
        
        
        
        date_updated_df = pd.DataFrame([current_date])
        zone_df = pd.DataFrame(['150-159.99'])
        macro_overview = pd.read_csv('macro_overview.csv')
        #print(macro_overview)
        macro_concat_150_15999 = pd.concat([date_updated_df,zone_df,mean_num_150_15999_df,zone_df,sum_num_150_15999_df,percentage_profit_loss_num_150_15999_df], axis=1)
        macro_concat_150_15999.columns = ['Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable']
        #print(macro_concat_150_15999)
        macro_concat_150_15999.to_csv('macro_overview.csv', mode='a', index=False, header=False)
        
        
    
    
    if(len(num_140_14999)-1 == -1):
        nothing = 0
    else:
        
        mean_num_140_14999 = mean(num_140_14999)
        #print("Average mean:", mean_num_140_14999)
        mean_num_140_14999_df = pd.DataFrame([mean_num_140_14999])
        #print(mean_num_140_14999_df)
         
        sum_num_140_14999 = sum(perc_num_140_14999)*100
        #print("Percentage Summation:", sum_num_140_14999)
        sum_num_140_14999_df = pd.DataFrame([sum_num_140_14999])
        #print(sum_num_140_14999_df)

        binary_sum_num_140_14999 = sum(binary_profit_loss_num_140_14999)
        #print("Win Amount:", binary_sum_num_140_14999)
        
        length_binary_sum_num_140_14999 = len(binary_profit_loss_num_140_14999)
        #print("Amount of Records:", length_binary_sum_num_140_14999)
        
        percentage_profit_loss_num_140_14999 = (binary_sum_num_140_14999/length_binary_sum_num_140_14999)*100
        #print("Percentage of Trades Profitable:", percentage_profit_loss_num_140_14999)
        percentage_profit_loss_num_140_14999_df = pd.DataFrame([percentage_profit_loss_num_140_14999])
        #print(percentage_profit_loss_num_140_14999_df)
        
        
        
        
        
        date_updated_df = pd.DataFrame([current_date])
        zone_df = pd.DataFrame(['140_14999'])
        macro_overview = pd.read_csv('macro_overview.csv')
        #print(macro_overview)
        macro_concat_140_14999 = pd.concat([date_updated_df,zone_df,mean_num_140_14999_df,zone_df,sum_num_140_14999_df,percentage_profit_loss_num_140_14999_df], axis=1)
        macro_concat_140_14999.columns = ['Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable']
        #print(macro_concat_140_14999)
        macro_concat_140_14999.to_csv('macro_overview.csv', mode='a', index=False, header=False)
        
        
        
        
        
        
          
    if(len(num_126_13999)-1 == -1):
        nothing = 0
    else:
        mean_num_126_13999 = mean(num_126_13999)
        #print("Average mean:", mean_num_126_13999)
        mean_num_126_13999_df = pd.DataFrame([mean_num_126_13999])
        #print(mean_num_126_13999_df)
          
        sum_num_126_13999 = sum(perc_num_126_13999)*100
        #print("Percentage Summation:", sum_num_126_13999)   
        sum_num_126_13999_df = pd.DataFrame([sum_num_126_13999])
        #print(sum_num_126_13999_df)
        
        binary_sum_num_126_13999 = sum(binary_profit_loss_num_126_13999)
        #print("Win Amount:", binary_sum_num_126_13999)
        
        length_binary_sum_num_126_13999 = len(binary_profit_loss_num_126_13999)
        #print("Amount of Records:", length_binary_sum_num_126_13999)
        
        percentage_profit_loss_num_126_13999 = (binary_sum_num_126_13999/length_binary_sum_num_126_13999)*100
        #print("Percentage of Trades Profitable:", percentage_profit_loss_num_126_13999)
        percentage_profit_loss_num_126_13999_df = pd.DataFrame([percentage_profit_loss_num_126_13999])
        #print(percentage_profit_loss_num_126_13999_df)
        
        
        
        
        date_updated_df = pd.DataFrame([current_date])
        zone_df = pd.DataFrame(['126_13999'])
        macro_overview = pd.read_csv('macro_overview.csv')
        #print(macro_overview)
        macro_concat_126_13999 = pd.concat([date_updated_df,zone_df,mean_num_126_13999_df,zone_df,sum_num_126_13999_df,percentage_profit_loss_num_126_13999_df], axis=1)
        macro_concat_126_13999.columns = ['Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable']
        #print(macro_concat_126_13999)
        macro_concat_126_13999.to_csv('macro_overview.csv', mode='a', index=False, header=False)
        
        
        
        
        
        
    if(len(num_100_12599)-1 == -1):
        nothing = 0
    else:
        mean_num_100_12599 = mean(num_100_12599)
        #print("Average mean:", mean_num_100_12599)
        mean_num_100_12599_df = pd.DataFrame([mean_num_100_12599])
        #print(mean_num_100_12599_df)
        
        sum_num_100_12599 = sum(perc_num_100_12599)*100
        #print("Percentage Summation:", sum_num_100_12599)
        sum_num_100_12599_df = pd.DataFrame([sum_num_100_12599])
        #print(sum_num_100_12599_df)
        
        binary_sum_num_num_100_12599 = sum(binary_profit_loss_num_100_12599)
        #print("Win Amount:", binary_sum_num_num_100_12599)
    
        length_binary_sum_num_num_100_12599 = len(binary_profit_loss_num_100_12599)
        #print("Amount of Records:", length_binary_sum_num_num_100_12599)
        
        percentage_profit_loss_num_100_12599 = (binary_sum_num_num_100_12599/length_binary_sum_num_num_100_12599)*100
        #print("Percentage of Trades Profitable:", percentage_profit_loss_num_100_12599)
        percentage_profit_loss_num_100_12599_df = pd.DataFrame([percentage_profit_loss_num_100_12599])
        #print(percentage_profit_loss_num_100_12599_df)
    
    
    
        date_updated_df = pd.DataFrame([current_date])
        zone_df = pd.DataFrame(['100_12599'])
        macro_overview = pd.read_csv('macro_overview.csv')
        #print(macro_overview)
        macro_concat_100_12599 = pd.concat([date_updated_df,zone_df,mean_num_100_12599_df,zone_df,sum_num_100_12599_df,percentage_profit_loss_num_100_12599_df], axis=1)
        macro_concat_100_12599.columns = ['Date_Updated','Zone','Average_Mean','Percentage_Summation','Win_Amount','Percentage_of_Trades_Profitable']
        #print(macro_concat_100_12599)
        macro_concat_100_12599.to_csv('macro_overview.csv', mode='a', index=False, header=False)
    
        
        
    
    print("RECORD ANALYSIS COMPLETE")
    
    return()

record_analysis()    
    
    