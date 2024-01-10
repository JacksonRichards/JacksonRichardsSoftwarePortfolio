


import boto
import pandas as pd
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto3
from botocore.errorfactory import ClientError
import os
from datetime import date





def all_terminal_liquidation_upload_aws():
    
    print("ALL TERMINAL LIQUIDATION UPLOADER COMMENCING")
    
    
    


    aws_connection = S3Connection('XXXXXXX','XXXXXXX')
    bucket = aws_connection.get_bucket('stoplossindicator')
    k = Key(bucket)
    k.key = 'company_wide_stop_loss_indicator.csv'
    k.set_contents_from_filename(r"C:\Users\jacks\Desktop\company_wide_stop_loss_indicator.csv")
    
    print("ALL TERMINAL LIQUIDATION UPLOADER COMPLETE")
    
    
all_terminal_liquidation_upload_aws()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








