🍺 Automated Brewery Data Pipeline

This project is a comprehensive, automated Data Pipeline designed to fetch brewery data from an Open API, perform data cleaning and transformation, convert datasets into optimized storage formats (CSV/Parquet), and securely upload the results to AWS S3 with integrated Telegram notifications.

🚀 Key Features

Data Extraction: Automated ingestion from the Open Brewery API.

Data Transformation: Data cleaning and schema enforcement using Pandas, including JSON to CSV/Parquet conversion for optimized performance.

Cloud Integration: Secure and scalable storage on AWS S3 for data lake readiness.

Monitoring & Alerting: Real-time success/failure status updates via Telegram Bot API.

📁 Project Structure

Project Data Validate/
├── main.py                # Main entry point to trigger the entire pipeline
├── getAPI.py              # Script for API extraction and raw JSON storage
├── jsontocsv.py           # Data cleaning, transformation, and format conversion
├── load_to_cloud.py       # AWS S3 upload logic and Telegram notification handler
├── .env                   # (Excluded) Environment variables for credentials
├── .gitignore             # Git exclusion rules for security and system junk
├── requirements.txt       # List of Python dependencies (Pandas, Boto3, etc.)
│
├── raw_data/              # Directory for ingested raw JSON files
├── cleaned_data/          # Directory for processed CSV files
└── data_parquet_to_upload/ # Directory for optimized Parquet files. 
                            # Implement data quality checks before loading to AWS S3.


🛠️ Tech Stack

Language: Python 3.x

Data Processing: Pandas, Pyarrow

Cloud Services: AWS S3 (via Boto3 SDK)

Communications: Telegram Bot API

Utilities: Requests, Python-dotenv

⚙️ Setup & Installation

Clone the repository:

git clone [https://github.com/chotiratwithgit/automated-brewery-data-cleaner.git](https://github.com/chotiratwithgit/automated-brewery-data-cleaner.git)


Install dependencies:

pip install -r requirements.txt


Configuration: Create a .env file in the root directory and provide the following credentials:

AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key
S3_BUCKET_NAME=your_bucket_name
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id


🏃 How to Run

Execute the main.py script to trigger the end-to-end pipeline:

python main.py


📊 Data Pipeline Workflow

Extract: Executes getAPI.py to fetch and store raw brewery data in JSON format.

Transform: Executes jsontocsv.py to handle missing values, enforce data types, and generate Parquet files.

Load: Executes load_to_cloud.py to sync the Parquet files to AWS S3 and dispatch a status notification to Telegram.

Note: Ensure that .env is listed in .gitignore to prevent leaking sensitive AWS and Telegram credentials.