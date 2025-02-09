# -*- coding: utf-8 -*-
"""AQI checker.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HWUUvUGxe0rw7V76mUr4ApacSOuOEfRV
"""

pip install requests

import requests

# Define your API key and base URL
API_KEY = 'fdbae4344e382c24cf2442f1456da6d6'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/air_pollution'

# Function to get air quality data
def get_air_quality(lat, lon):
    # Build the complete API URL
    url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        air_quality = data['list'][0]['main']['aqi']

        # Translate AQI level to description
        air_quality_description = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very Poor"
        }

        print(f"Air Quality Index (AQI) Level: {air_quality} ({air_quality_description.get(air_quality, 'Unknown')})")
    else:
        print("Error retrieving air quality data. Please check the coordinates and API key.")

# Function to get latitude and longitude for a city
def get_coordinates(city):
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    response = requests.get(geocode_url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            print("City not found. Please check the city name.")
            return None, None
    else:
        print("Error retrieving location coordinates.")
        return None, None

# Example usage
city_name = input("Enter the city name: ")
lat, lon = get_coordinates(city_name)

if lat and lon:
    get_air_quality(lat, lon)