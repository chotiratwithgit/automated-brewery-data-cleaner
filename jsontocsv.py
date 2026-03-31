import json
import glob
import os
import pandas as pd


def convert_json_to_csv():        

    def save_cleaned_data_to_csv(dataframe, filename): # Function to save the cleaned DataFrame to foolder as a CSV file
        folder_name = "cleaned_data"

        if not os.path.exists(folder_name): # Check if the folder exists, if not, create it
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created successfully!")

        file_path = os.path.join(folder_name, filename) # Create the file path 

        dataframe.to_csv(file_path, index=False, encoding="utf-8") # Save the DataFrame to a CSV file without the index and with UTF-8 encoding

        print(f"\nSave Cleaned Data to Folder '{file_path}' Successful!")


    # Load Raw Data
    json_files = glob.glob("raw_data/raw_brewery_data_*.json")
    # Search for JSON files in the current directory that match the pattern "raw_brewery_data_*.json"

    if json_files:
        filename = max(json_files, key=os.path.getctime)  # Select the latest file found

        print(f"Latest JSON file found: {filename}")

        with open(filename, "r", encoding="utf-8") as file:
            raw_data = json.load(file)  # Load data from the JSON file

            print(f"Load Raw Data from File '{filename}' Successful!")
    else:
        print("No JSON files found in the current folder.")
        exit()

    # Create DataFrame
    df = pd.DataFrame(raw_data)

    # Choose columns to keep
    columns_to_keep = ['id', 'name', 'brewery_type', 'city', 'state', 'country']

    missing_columns = [col for col in columns_to_keep if col not in df.columns]
    if missing_columns:
        raise KeyError(f"Missing expected columns in JSON data: {missing_columns}")

    df_cleaned = df[columns_to_keep].copy()

    # Solve missing, null, and unknown values
    cols_to_clean = ['id', 'name', 'brewery_type', 'city', 'state', 'country']

    for col in cols_to_clean:
        df_cleaned.loc[:, col] = df_cleaned[col].fillna('Unknown')  # Fill missing values with 'Unknown'
        df_cleaned.loc[:, col] = df_cleaned[col].str.strip().str.upper()  # Remove extra spaces and convert to uppercase


    # Cleaned Data
    print("\nCleaned Data:")
    print(df_cleaned.head())

    # Save To Csv
    output_filename = "cleaned_breweries.csv"
    save_cleaned_data_to_csv(df_cleaned, output_filename)
