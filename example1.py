# WEATHER API EXAMPLE
# https://openweathermap.org/api
import requests

API_KEY='TODO'

# Get location data for Golden
resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=Golden,CO,USA&appid={API_KEY}')
resp = resp.json()

# Get the weather in Golden!
resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=39.7546349&lon=-105.22058&units=imperial&appid={API_KEY}')
resp = resp.json()
print(resp)
