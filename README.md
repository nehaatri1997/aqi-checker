# AQI Checker

# Overview
This Python script retrieves and displays the Air Quality Index (AQI) for a specific location. It uses an API to access real-time AQI data and provides insights on air quality, helping users make informed decisions based on air pollution levels.

# Features
1. Fetches AQI data for a given location.
2. Displays the current AQI level and offers an interpretation of air quality.
3. Allows users to specify different locations to check AQI levels in real-time.

# Prerequisites
1. Python 3.6+
2. Install the required library using:
     pip install requests


# Getting Started
1. API Key: Obtain an API key from an AQI data provider (like AQICN or OpenWeatherMap).
2. Configure API Key: Insert your API key into the script where specified.
3. Run the Script: Execute the script to check the AQI for your specified location.

# Usage
1. Run the script using:
python aqi_checker.py
2. Follow the prompts to input the location or update the script with predefined locations.
3. View the AQI level and associated message for the air quality.

# Example

Enter the location for AQI check: New York
AQI for New York: 85 (Moderate)

# Note
This script is intended for educational or personal use; for commercial use, check with the data provider for licensing and API rate limits.

# Troubleshooting
If the script returns an error, check if the API key is correctly set.
Verify that your internet connection is active, as this script requires API access.
