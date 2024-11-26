# api key access
from dotenv import load_dotenv
import os
load_dotenv("API_KEY.env") 
API_KEY = os.getenv('API_KEY')

#start
import json
import requests

# Base URL of the API
url = "https://mma-stats.p.rapidapi.com/search"

# Headers required by RapidAPI
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "mma-stats.p.rapidapi.com"
}

querystring = {"name": "Sean Strickland"}

response = requests.get(url, headers=headers, params=querystring)
if response.status_code == 200:
    print("Request was successful!")
    response_data = response.json()

    # Saving the JSON response to a file
    with open("mma_stats_response.json", "w") as json_file:
        json.dump(response_data, json_file, indent=4)

    print("Response saved to 'mma_stats_response.json'!")
else:
    print(f"Error: {response.status_code}")
    print("Details:", response.text)