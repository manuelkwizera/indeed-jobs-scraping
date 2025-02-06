import requests

API_KEY = "c3d1bd8fa8846d4270bb348ecbd8f6876d16aa0e5e3eb04fb4fa432ae0653de6"
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
            print("Success:", response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print("An error occurred:", e)


trigger_brightdata_dataset()
