import requests
import csv
import time

API_KEY = "011dbeba182b9daa6c7999b5b82e8ae611335a0d50c48b0ff9b3143557cfa3ee"
DATASET_ID = "gd_l4dx9j9sscpvs7no2"

def trigger_brightdata_dataset():
    url = "https://api.brightdata.com/datasets/v3/trigger"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = [
        {"url": "https://de.indeed.com/jobs?q=python+developer&l=Germany"},
    ]
    
    params = {
        "dataset_id": DATASET_ID,
        "include_errors": "true",
        "type": "discover_new",
        "discover_by": "url"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, params=params)
        if response.status_code == 200:
            print("Dataset Trigger Success:", response.json())
            return response.json().get("snapshot_id")  # Return the snapshot_id
        else:
            print(f"Dataset Trigger Error: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print("An error occurred during dataset trigger:", e)
    return None  # Return None if there's an error

def fetch_and_save_data(snapshot_id, retries=5, delay=10):
    if not snapshot_id:
        print("Invalid snapshot ID. Cannot fetch data.")
        return
    
    url = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}"
    querystring = {"format": "json", "batch_size": "1000"}
    headers = {"Authorization": f"Bearer {API_KEY}"}

    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, params=querystring)
            print("Snapshot Fetch Status Code:", response.status_code)

            if response.status_code == 200:
                data = response.json()
                with open("response_data.csv", "w", newline="", encoding="utf-8") as csvfile:
                    csv_writer = csv.writer(csvfile)
                    if isinstance(data, list) and len(data) > 0:
                        csv_writer.writerow(data[0].keys())  
                        for item in data:
                            csv_writer.writerow(item.values())

                print("Data successfully saved to response_data.csv")
                return  # Exit after successfully saving the data
            else:
                error_data = response.json()
                if error_data.get("status") == "running" and "Snapshot is not ready yet" in error_data.get("message", ""):
                    print(f"Snapshot not ready yet. Attempt {attempt + 1}/{retries}. Retrying in {delay} seconds...")
                    print("API Error:", response.text)
                    time.sleep(delay)
                else:
                    print("Error fetching snapshot:", response.text)
                    break
        except requests.exceptions.RequestException as e:
            print("Request Error during data fetch:", e)
            break

    print("Failed to fetch data after retries.")

# Trigger the dataset and fetch the data
snapshot_id = trigger_brightdata_dataset()
fetch_and_save_data(snapshot_id)
