import requests
import csv

SNAPSHOT_ID = "s_m5qkzgtg1cufapv8l5"
API_KEY = "011dbeba182b9daa6c7999b5b82e8ae611335a0d50c48b0ff9b3143557cfa3ee"


def fetch_and_save_data():
    url = f"https://api.brightdata.com/datasets/v3/snapshot/{SNAPSHOT_ID}"
    querystring = {"format": "json", "batch_size": "1000"}
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(url, headers=headers, params=querystring)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            with open("response_data.csv", "w", newline="", encoding="utf-8") as csvfile:
                csv_writer = csv.writer(csvfile)
                if isinstance(data, list) and len(data) > 0:
                    csv_writer.writerow(data[0].keys())  
                    for item in data:
                        csv_writer.writerow(item.values())

            print("Data successfully saved to response_data.csv")
        else:
            print("Error:", response.text)
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)


fetch_and_save_data()
