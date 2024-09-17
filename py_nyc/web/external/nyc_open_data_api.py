import requests
import os


def get_trip_data():
    APP_TOKEN = os.environ.get("NYC_OPEN_DATA_APP_TOKEN")
    url = "https://data.cityofnewyork.us/resource/u253-aew4.json?$limit=10"
    headers = {"X-App-Token": APP_TOKEN}
    resp = requests.get(url, headers=headers)

    return resp
