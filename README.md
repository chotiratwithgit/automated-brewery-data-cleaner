##🍺 Automated Brewery Data Pipeline

## 📌 Project Overview
This project is a comprehensive, automated Data Pipeline designed to fetch brewery data from an Open API, perform data cleaning and transformation, convert datasets into optimized storage formats (CSV/Parquet), and securely upload the results to AWS S3 with integrated Telegram notifications.

This repository demonstrates skills in **API integration**, **Data Cleaning/Transformation**, **Cloud Storage Operations (AWS)**,And securely upload the results to AWS S3 with integrated Telegram notifications

## 🛠️ Architecture
1. **Extract**: Fetch raw JSON data from Open Brewery DB API (`getAPI.py`).
2. **Transform**: Clean data, handle missing values, and convert JSON to CSV format (`jsontocsv.py`).
3. **Load**: Read the cleaned CSV, convert it to a highly compressed Parquet format, and upload it to an AWS S3 bucket (`load_to_cloud.py`).
4. **Monitoring & Alerting**: Real-time success/failure status updates via Telegram Bot API

## 🚀 Tech Stack
- **Python**: Core programming language
- **Pandas**: Data manipulation and cleaning
- **Boto3**: AWS SDK for Python (uploading to S3)
- **PyArrow**: Parquet file conversion
- **python-dotenv**: Environment variable management
- **Telegram Bot API**: Monitoring & Alerting status updates



## ⚙️ Setup & Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/chotiratwithgit/automated-brewery-data-cleaner.git
   cd automated-brewery-data-cleaner
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory and provide the following credentials:
   ```ini
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   S3_BUCKET_NAME=your_bucket_name
   TELEGRAM_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```

## 📂 File Structure
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
                            
## 🏃 How to Run                            
Execute the main.py script to trigger the end-to-end pipeline:
python main.py

## 📊Data Pipeline Workflow

Extract: Executes getAPI.py to fetch and store raw brewery data in JSON format.
Transform: Executes jsontocsv.py to handle missing values, enforce data types, and generate Parquet files.
Load: Executes load_to_cloud.py to sync the Parquet files to AWS S3 and dispatch a status notification to Telegram.

Note: Ensure that .env is listed in .gitignore to prevent leaking sensitive AWS and Telegram credentials.

## 📝 Future Improvements
- Automate pipeline execution using Airflow or cron jobs.
- Add logging and error alerting capabilities.
- Implement data quality checks before loading to AWS S3.
