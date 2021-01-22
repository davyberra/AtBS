#! python 3
# get_open_weather.py - Prints the weather for a location from the command line.

APPID = '812c6fb8e8c133a983d95b7fee239608'

import json, requests, sys

# Compute location from command line arguments.

if len(sys.argv) < 2:
    print('Usage: get_open_weather.py city_name, 2-letter_country_code')
    sys.exit()

location = ''.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()

# print(response.text)

# TODO: Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print(f'Current weather in {location}:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])