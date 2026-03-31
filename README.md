# Open Brewery ETL Pipeline (Data Engineering Portfolio)

## 📌 Project Overview
This project is an end-to-end Extract, Transform, Load (ETL) pipeline built with Python. It extracts brewery data from the [Open Brewery DB API](https://www.openbrewerydb.org/), cleans and transforms the data using Pandas, and loads it into an AWS S3 bucket in Parquet format.

This repository demonstrates skills in **API integration**, **Data Cleaning/Transformation**, and **Cloud Storage Operations (AWS)**.

## 🛠️ Architecture
1. **Extract**: Fetch raw JSON data from Open Brewery DB API (`getAPI.py`).
2. **Transform**: Clean data, handle missing values, and convert JSON to CSV format (`jsontocsv.py`).
3. **Load**: Read the cleaned CSV, convert it to a highly compressed Parquet format, and upload it to an AWS S3 bucket (`load_to_cloud.py`).

## 🚀 Technologies Used
- **Python**: Core programming language
- **Pandas**: Data manipulation and cleaning
- **Boto3**: AWS SDK for Python (uploading to S3)
- **PyArrow**: Parquet file conversion
- **python-dotenv**: Environment variable management

## ⚙️ Setup & Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/open-brewery-etl.git
   cd open-brewery-etl
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
   Create a `.env` file in the root directory and add your AWS credentials:
   ```ini
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   ```

## 📂 File Structure
- `getAPI.py`: Script to extract data from API and save as JSON.
- `jsontocsv.py`: Script to transform JSON data to a cleaned CSV.
- `load_to_cloud.py`: Script to convert CSV to Parquet and upload to AWS S3.
- `requirements.txt`: Python package dependencies.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## 📝 Future Improvements
- Automate pipeline execution using Airflow or cron jobs.
- Add logging and error alerting capabilities.
- Implement data quality checks before loading to AWS S3.
