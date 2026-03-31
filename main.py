import jsontocsv
import getAPI
import load_to_cloud

import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")     # Get the Telegram bot token from environment variables
chat_id = os.getenv("TELEGRAM_CHAT_ID")         # Get the Telegram chat ID from environment variables


# Setup logging

logging.basicConfig(   
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s" # Log format to include timestamp, log level, and message
)

def send_telegram_message(bot_token, chat_id, message):
 # Function to send a message to Telegram using the bot token and chat ID
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage" # Telegram API to send a message
    payload = {
        "chat_id": chat_id,
        "text": message    
    }
    
    response = requests.post(url, data=payload) # Send a POST request to the Telegram API with the message payload
    response.raise_for_status()

# logging for reporting errors and debugging
def run_pepline():
    logging.info("Starting the data pipeline...") # Log the start of the pipeline

    try : 
        logging.info("Extracting data from API...") # Log the start of data extraction
        getAPI.extract_brewery_data()    # Extracting data from API 
        logging.info("Data extraction completed successfully.") # Log the successful completion of data extraction
    except Exception as e:
        logging.exception(f"Error Extracting Data: {e}") # Log any errors that occur during data extraction
        send_telegram_message(bot_token, chat_id,"Error occurred while extracting data.")
        return
    
    try :
        logging.info("Converting JSON data to CSV format...") # Log the start of data conversion
        jsontocsv.convert_json_to_csv()  # Converting JSON data to CSV format
        logging.info("Data conversion completed successfully.") # Log the successful completion of data conversion
    except Exception as e:
        logging.exception(f"Error Converting Data: {e}") # Log any errors that occur during data conversion
        send_telegram_message(bot_token, chat_id,"Error occurred while converting data.")
        return

    try :
        logging.info("uploading data to cloud storage...") # Log the start of data uploading
        load_to_cloud.upload_to_s3()            # upload data to Google Cloud Storage
        logging.info("Data upload completed successfully.") # Log the successful completion of data uploading
    except Exception as e:
        logging.exception(f"Error uploading Data: {e}") # Log any errors that occur during data uploading
        send_telegram_message(bot_token, chat_id,"Error occurred while uploading data.")
        return
    
    logging.info("Data pipeline completed successfully!") # Log the successful completion of the pipeline
    send_telegram_message(bot_token, chat_id,"Data pipeline completed successfully!")
if __name__ == "__main__":
    run_pepline()

    