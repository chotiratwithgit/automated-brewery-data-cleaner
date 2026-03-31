import pandas as pd
import boto3 
import os
from dotenv import load_dotenv
import datetime 
# Read the CSV 

input_filename = "cleaned_data/cleaned_breweries.csv" 
print(f"Reading data from {input_filename}...")
df = pd.read_csv(input_filename)

def upload_to_s3():           


    # Convert to parquet

    def clean_data_to_parquet(dataframe, filename):                 # Function to save the cleaned DataFrame to foolder as a parquet file
        folder_name = "data_parquet_to_upload"

        if not os.path.exists(folder_name):                         # Check if the folder exists, if not, create it
            os.makedirs(folder_name) 
            print(f"Folder '{folder_name}' created successfully!")


        file_path = os.path.join(folder_name, filename)                 # Create the file path
        dataframe.to_parquet(file_path, engine='pyarrow', index=False) 

        print(f"\nSave Cleaned Data to Folder '{file_path}' Successful!")
        return file_path                                                       # Return the path of the parquet file to upload

    today_date = datetime.datetime.now().strftime("%y%m%d") # Generate file name with today's date

    parquet_filename = f"cleaned_breweries_{today_date}.parquet"  # Define the parquet file name with today's date
    parquet_file_path = clean_data_to_parquet(df, parquet_filename) # Get the path of the parquet file to upload
                                                                    
    print(f"Data converted successfully to {parquet_filename}.")




    # Upload to cloud (AWS S3)

    load_dotenv()                                     # load environment variables from .env

    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    BUCKET_NAME = 'my-data-portfolio-chotirat-2026'


    def upload_to_s3(file_name, bucket_name):            # Function to upload the parquet file to S3 bucket
        print(f"Uploading {file_name} to S3 bucket '{bucket_name}' on AWS...")

        try:
        
            s3_client = boto3.client(               # Create an S3 client using the AWS credentials from environment variables
                's3', 
                aws_access_key_id=AWS_ACCESS_KEY,
                aws_secret_access_key=AWS_SECRET_KEY  
            )
        
            
            s3_client.upload_file(file_name, bucket_name, file_name)    # Upload the file to the specified S3 bucket 
            print(" Uploaded successfully to bucket!")
            
        except Exception as e:
            print(f" Error uploading file to S3: {e}")

    upload_to_s3(parquet_file_path, BUCKET_NAME)
                                
                                
                                
                                


