import requests
import os
import random
import time
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv('API_TOKEN')

url = "https://api.brightdata.com/request" # the endpoint for proxy based scripting

payload = {
    "zone": "mobile_proxy1",  # proxy zone
    "url": "https://www.indeed.com/jobs?q=python&l=Texas",  # query parameter we will update later to make it dynamic
    "format": "raw"  # raw htm content
}

headers = {
    "Authorization": f'Bearer {api_token}', # api token
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"  # Simulate a browser
}

def fetch_data():
    try:
        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 200:
            print("Request successful. Data retrieved:")
            print(response.text)  # html data
        else:
            print(f"Error: {response.status_code}, {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

fetch_data()
