

import boto
import pandas as pd
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto3
from botocore.errorfactory import ClientError
import os
from datetime import date





def aws_upload_api():
    
    print("TERMINAL API CLOUD UPLOADER COMMENCING")
    
    api_information = pd.read_csv('alpaca_api_information.csv')
    terminal_bucket = api_information['Terminal Bucket'].to_numpy().tolist()
    terminal_number = api_information['Terminal Number'].to_numpy().tolist()
    
    today_initial_data = date.today()
    y = today_initial_data.strftime("%m-%d-%Y")
    NY = 'America/los_angeles'
    end=pd.Timestamp(y, tz=NY)   
    record_date = y
    #print("Record Date:", record_date)


    aws_connection = S3Connection('XXXXXXX','XXXXXXX')
    bucket = aws_connection.get_bucket(terminal_bucket[0])
    k = Key(bucket)
    k.key = 'alpaca_api_information_'+terminal_number[0]+'.csv'
    k.set_contents_from_filename(r"C:\Users\jacks\Desktop\PMax Algorithm Software - L\alpaca_api_information.csv")
    
    print("TERMINAL API CLOUD UPLOADER COMPLETE")
    
    
aws_upload_api()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








