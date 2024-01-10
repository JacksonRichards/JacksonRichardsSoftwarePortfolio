
import csv


def error_records_database_setup():

    print("ERROR RECORDS DATABASE SETUP COMMENCING")    

    with open('error_records.csv', 'a', newline='') as csvfile:
        my_writer = csv.writer(csvfile)
        my_writer.writerow(("Error Time", "Error Type"))
        
        
    print("ERROR RECORDS DATABASE SETUP COMPLETE")  
        
error_records_database_setup()
    