

import boto
import pandas as pd
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto3
from botocore.errorfactory import ClientError
import os
from datetime import date





def all_terminal_liquidation_download_aws():
    
    
    print("ALL TERMINAL LIQUIDATION DOWNLOADER COMMENCING")
    
    
    # Creating the low level functional client
    client = boto3.client(
        's3',
        aws_access_key_id = 'XXXXXXX',
        aws_secret_access_key = 'XXXXXXX',
        region_name = 'XXXXXXX'
    )


    #print('yes')
    
    client.download_file(
        Filename=r"C:\Users\jacks\Desktop\PMax Algorithm Software - L\company_wide_stop_loss_indicator.csv",
        Bucket='stoplossindicator',
        Key='company_wide_stop_loss_indicator.csv'
    )
    
    
    
    
    print("ALL TERMINAL LIQUIDATION DOWNLOADER COMPLETE")
    

       
     
    
all_terminal_liquidation_download_aws()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








