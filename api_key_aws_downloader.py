


import boto
import pandas as pd
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto3
from botocore.errorfactory import ClientError
import os
from datetime import date





def aws_download_api():
    
    print("AMAZON WEB SERVICES CLOUD DOWNLOADER COMMENCING")
    all_buckets = ['terminal-one-blc','terminal-two-blc','terminal-three-blc','terminal-four-blc','terminal-five-blc','terminal-six-blc']
    all_numbers = ['terminal_1','terminal_2','terminal_3','terminal_4','terminal_5','terminal_6']
    
    #api_information = pd.read_csv('alpaca_api_information.csv')
    #terminal_bucket = api_information['Terminal Bucket'].to_numpy().tolist()
    #print(terminal_bucket)
    #terminal_number = api_information['Terminal Number'].to_numpy().tolist()
    
    for items_all_buckets, items_all_numbers in zip(all_buckets, all_numbers):

       
        
        # Creating the low level functional client
        client = boto3.client(
            's3',
            aws_access_key_id = 'XXXXXXX',
            aws_secret_access_key = 'XXXXXXXX',
            region_name = 'XXXXXXXX'
        )
    
    
        #print('yes')
        
        client.download_file(
            Filename=r"C:\Users\jacks\Desktop\PMax Algorithm Software - L\alpaca_api_information_"+items_all_numbers+".csv",
            Bucket=items_all_buckets,
            Key='alpaca_api_information_'+items_all_numbers+'.csv'
        )
        
        #print('yes')
    
    
    print("AMAZON WEB SERVICES CLOUD DOWNLOADER COMPLETE")
    
    
aws_download_api()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








