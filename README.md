# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates

## Overview
The Real-Time Data Processing System for Weather Monitoring is designed to continuously monitor weather conditions and provide summarized insights. By leveraging the OpenWeatherMap API, this system retrieves data on major metros in India, calculates aggregates, and triggers alerts based on user-defined thresholds.

## Objective
The primary goal is to develop a system that:
- Monitors real-time weather conditions.
- Provides summarized insights through daily rollups and aggregates.
- Notifies users of significant weather changes based on customizable thresholds.

## Data Source
The system utilizes data from the [OpenWeatherMap API](https://openweathermap.org/). The key weather parameters are:
- **main**: Main weather condition (e.g., Rain, Snow, Clear).
- **temp**: Current temperature in Celsius.
- **feels_like**: Perceived temperature in Celsius.
- **dt**: Time of the data update (Unix timestamp).

## Processing and Analysis
### Continuous Data Retrieval
The system retrieves weather data every 5 minutes for the following major metros in India:
- Delhi
- Mumbai
- Chennai
- Bangalore
- Kolkata
- Hyderabad

### Temperature Conversion
All temperature values are converted from Kelvin to Celsius or Fahrenheit based on user preference.

## Rollups and Aggregates
### 1. Daily Weather Summary
- Roll up weather data daily.
- Calculate the following aggregates:
  - **Average temperature**
  - **Maximum temperature**
  - **Minimum temperature**
  - **Dominant weather condition**: This is determined by identifying the most frequently occurring weather condition within the day.
- Store daily summaries in a database for further analysis.

### 2. Alerting Thresholds
- Define user-configurable thresholds for temperature or specific weather conditions (e.g., alert if the temperature exceeds 35 degrees Celsius for two consecutive updates).
- Continuously monitor the latest weather data and compare it with the defined thresholds.
- Trigger alerts if thresholds are breached.

### 3. Visualizations
- Use visualization libraries (e.g., Matplotlib, Plotly) to display:
  - Daily weather summaries
  - Historical trends
  - Triggered alerts

## Implementation Steps

### 1. System Setup
- **Environment**: The system is implemented in Python, using libraries such as:
  - `requests`: For making API calls.
  - `sqlite3`: For database storage.
  - `matplotlib` or `plotly`: For visualizations.
- **API Key**: Sign up for a free API key on OpenWeatherMap and replace `'your_api_key'` in the code.

### 2. Data Retrieval
Retrieve weather data from the OpenWeatherMap API:
python
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


### 3. Temperature Conversion
Convert temperature from Kelvin to Celsius or Fahrenheit:
python
def convert_temperature(kelvin_temp, to_celsius=True):
    if to_celsius:
        return kelvin_temp - 273.15  # Convert to Celsius
    return (kelvin_temp - 273.15) * 9/5 + 32  # Convert to Fahrenheit


### 4. Daily Weather Summary Calculation
Calculate daily weather aggregates:
python
from collections import defaultdict

daily_summaries = defaultdict(lambda: {'temps': [], 'conditions': []})

def update_daily_summary(weather_data):
    date = datetime.fromtimestamp(weather_data['dt']).date()
    daily_summaries[date]['temps'].append(weather_data['temp'])
    daily_summaries[date]['conditions'].append(weather_data['main'])

def calculate_daily_summary(date):
    if date in daily_summaries:
        temps = daily_summaries[date]['temps']
        conditions = daily_summaries[date]['conditions']
        
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        dominant_condition = max(set(conditions), key=conditions.count)
        
        return {
            'date': date,
            'average_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }
    return None


### 5. Alerting Mechanism
Check for alert conditions based on user-defined thresholds:
python
alert_threshold = 35  # Celsius
alert_count = 0

def check_alert_conditions(weather_data):
    global alert_count
    if weather_data['temp'] > alert_threshold:
        alert_count += 1
        if alert_count >= 2:
            print(f"Alert: High temperature detected! {weather_data['temp']}°C")
    else:
        alert_count = 0  # Reset if condition not met


### 6. Continuous Data Retrieval Loop
Implement a loop to continuously fetch weather data:
python
def start_monitoring():
    while True:
        for city in CITIES:
            data = fetch_weather_data(city)
            if data:
                temp = convert_temperature(data['main']['temp'])
                weather_data = {
                    'temp': temp,
                    'main': data['weather'][0]['main'],
                    'dt': data['dt']
                }
                update_daily_summary(weather_data)
                check_alert_conditions(weather_data)
        time.sleep(300)  # Wait for 5 minutes before next fetch


### 7. Data Storage
Store daily summaries and alerts in an SQLite database:
python
import sqlite3

def initialize_database():
    conn = sqlite3.connect('weather_monitoring.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                        date TEXT PRIMARY KEY,
                        average_temp REAL,
                        max_temp REAL,
                        min_temp REAL,
                        dominant_condition TEXT)''')
    
    conn.commit()
    conn.close()

def store_daily_summary(summary):
    conn = sqlite3.connect('weather_monitoring.db')
    cursor = conn.cursor()
    
    cursor.execute('''INSERT OR REPLACE INTO daily_summary 
                      (date, average_temp, max_temp, min_temp, dominant_condition) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (summary['date'], summary['average_temp'], summary['max_temp'], 
                    summary['min_temp'], summary['dominant_condition']))
    
    conn.commit()
    conn.close()


## Test Cases
To ensure the system works correctly, the following test cases should be implemented:
1. **System Setup**: Verify the connection to the OpenWeatherMap API and successful retrieval of data.
2. **Data Retrieval**: Simulate API calls to check if data is parsed correctly.
3. **Temperature Conversion**: Test conversion functions with various Kelvin values to ensure accuracy.
4. **Daily Weather Summary**: Validate calculations for daily aggregates.
5. **Alerting Thresholds**: Ensure alerts trigger correctly based on defined temperature thresholds.

## Bonus Features
- Extend the system to include additional weather parameters, such as humidity and wind speed, in the rollups and aggregates.
- Implement functionality to retrieve weather forecasts and generate summaries based on predicted conditions.

## Conclusion
This project serves as a comprehensive framework for real-time weather monitoring, providing valuable insights through analytics and timely alerts based on user-defined conditions. Future enhancements could focus on optimizing performance and integrating additional features to improve user experience.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

