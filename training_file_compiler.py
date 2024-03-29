
import pandas as pd
import numpy as np



def training_record_compiler():

    print("TRAINING RECORD COMPILER COMMENCING")
    
    ticker_list = pd.read_csv('ticker_list_today.csv')
    ticker_csv_data = ticker_list['Tickers'].to_numpy().tolist()
    #print(ticker_csv_data)
    
    for ticker in ticker_csv_data:
    
        training_file_1 = pd.read_csv('Pmax_Algo_Data_collection_1_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_1)
        #print('-------------------------')
        training_file_2 = pd.read_csv('Pmax_Algo_Data_collection_2_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_2)
        #print('-------------------------')
        training_file_3 = pd.read_csv('Pmax_Algo_Data_collection_3_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_3)
        #print('-------------------------')
        training_file_4 = pd.read_csv('Pmax_Algo_Data_collection_4_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_5 = pd.read_csv('Pmax_Algo_Data_collection_5_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_6 = pd.read_csv('Pmax_Algo_Data_collection_6_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_7 = pd.read_csv('Pmax_Algo_Data_collection_7_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_8 = pd.read_csv('Pmax_Algo_Data_collection_8_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_9 = pd.read_csv('Pmax_Algo_Data_collection_9_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_10 = pd.read_csv('Pmax_Algo_Data_collection_10_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_11 = pd.read_csv('Pmax_Algo_Data_collection_11_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_12 = pd.read_csv('Pmax_Algo_Data_collection_12_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_13 = pd.read_csv('Pmax_Algo_Data_collection_13_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_14 = pd.read_csv('Pmax_Algo_Data_collection_14_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_15 = pd.read_csv('Pmax_Algo_Data_collection_15_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_16 = pd.read_csv('Pmax_Algo_Data_collection_16_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_17 = pd.read_csv('Pmax_Algo_Data_collection_17_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_18 = pd.read_csv('Pmax_Algo_Data_collection_18_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_19 = pd.read_csv('Pmax_Algo_Data_collection_19_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_20 = pd.read_csv('Pmax_Algo_Data_collection_20_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_21 = pd.read_csv('Pmax_Algo_Data_collection_21_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_22 = pd.read_csv('Pmax_Algo_Data_collection_22_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_23 = pd.read_csv('Pmax_Algo_Data_collection_23_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_24 = pd.read_csv('Pmax_Algo_Data_collection_24_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_25 = pd.read_csv('Pmax_Algo_Data_collection_25_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_26 = pd.read_csv('Pmax_Algo_Data_collection_26_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_27 = pd.read_csv('Pmax_Algo_Data_collection_27_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_28 = pd.read_csv('Pmax_Algo_Data_collection_28_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_29 = pd.read_csv('Pmax_Algo_Data_collection_29_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_30 = pd.read_csv('Pmax_Algo_Data_collection_30_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_31 = pd.read_csv('Pmax_Algo_Data_collection_31_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_32 = pd.read_csv('Pmax_Algo_Data_collection_32_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_33 = pd.read_csv('Pmax_Algo_Data_collection_33_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_34 = pd.read_csv('Pmax_Algo_Data_collection_34_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_35 = pd.read_csv('Pmax_Algo_Data_collection_35_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_36 = pd.read_csv('Pmax_Algo_Data_collection_36_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_37 = pd.read_csv('Pmax_Algo_Data_collection_37_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_38 = pd.read_csv('Pmax_Algo_Data_collection_38_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_39 = pd.read_csv('Pmax_Algo_Data_collection_39_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        training_file_40 = pd.read_csv('Pmax_Algo_Data_collection_40_'+ticker+'_TRADINGVIEW.csv')
        #print(training_file_4)
        #print('-------------------------')
        
        
        
        final_compiler = pd.concat([training_file_1, training_file_2, training_file_3, training_file_4, training_file_5, training_file_6, training_file_7, training_file_8, training_file_9, training_file_10, training_file_11, training_file_12, training_file_13, training_file_14, training_file_15, training_file_16, training_file_17, training_file_18, training_file_19, training_file_20, training_file_21, training_file_22, training_file_23, training_file_24, training_file_25, training_file_26, training_file_27, training_file_28, training_file_29, training_file_30, training_file_31, training_file_32, training_file_33, training_file_34, training_file_35, training_file_36, training_file_37, training_file_38, training_file_39, training_file_40], axis = 0)
        #print(final_compiler)
        final_compiler.to_csv('training_data_compiled_'+ticker+'.csv')
    
    print("TRAINING RECORD COMPILER COMPLETE")

training_record_compiler()