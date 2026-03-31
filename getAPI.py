import requests
import json
import datetime
import os
# Get API Data
def extract_brewery_data(per_page= 10) :
    url =f"https://api.openbrewerydb.org/v1/breweries?per_page={per_page}"

#  Go to exception if there is error in the request
    try : 
        print( f"Getting API: {per_page} items per page" )
        response = requests.get(url)
        
        response.raise_for_status()            # Check if the request was successful (status code 200)
        
        data = response.json()           #  JSON to Python dict
        print("successfully got data from API")
        return data

    except Exception as e:
        print(f"Error Getting data: {e}")
        return None
    
def save_raw_data(data_to_save, filename):
    folder_name = "raw_data"              # folder name to save raw data

    if data_to_save is not None:           # check if there is data to save

        if not os.path.exists(folder_name):        # check if folder Not exists

            os.makedirs(folder_name)            # create folder if not exists
            print(f"Folder '{folder_name}' created successfully!")

        file_path = os.path.join(folder_name, filename)      # create path of the file

        with open(file_path, "w", encoding="utf-8") as file:        # open file to write

            json.dump(data_to_save, file, indent=4, ensure_ascii=False)  # save as JSON

        print(f"Data saved to file '{file_path}' successfully!")

    else:
        print("No data to save")


# Main function to execute the code
if __name__ == "__main__":
    raw_data = extract_brewery_data(per_page=200)  # Get data from API with 200 items per page

   # Generate file name with today's date
    today_date = datetime.datetime.now().strftime("%y%m%d") 
    file_name = f"raw_brewery_data_{today_date}.json"  
    
    # save file
    save_raw_data(raw_data,filename=file_name)