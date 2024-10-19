import requests
import time
from datetime import datetime

API_KEY = 'your_api_key'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data for {city}: {response.status_code}")
        return None
