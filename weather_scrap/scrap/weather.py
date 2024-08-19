import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Locating address")

def description(data):
    # Parse the JSON data
    weather_data = data

    # Extract relevant weather information
    coordinates = weather_data.get('coord', {})
    main_weather = weather_data.get('weather', [{}])[0]
    main_info = weather_data.get('main', {})
    wind_info = weather_data.get('wind', {})
    visibility = weather_data.get('visibility')
    city_name = weather_data.get('name')
    country_code = weather_data.get('sys', {}).get('country')
    
    #converting kelvin to fahrenheit
    temp = main_info.get('temp')
    temp = ((temp-273.15)*(9/5))+32
    
    temp_feel= main_info.get('feels_like')
    temp_feel = ((temp_feel-273.15)*(9/5))+32
    
    temp_min =main_info.get('temp_min')
    temp_min = ((temp_min-273.15)*(9/5))+32
    
    temp_max = main_info.get('temp_max')
    temp_max = ((temp_max-273.15)*(9/5))+32

    # Build the forecast dictionary
    forecast = {
        "title": f"{city_name}, {country_code}",
        "Temperature": '%.3f'%(temp),
        "Feels Like":'%.3f'%(temp_feel),
        "Minimum Temperature": '%.3f'%(temp_min),
        "Maximum Temperature": '%.3f'%(temp_max),
        "Pressure": main_info.get('pressure'),
        "Humidity": main_info.get('humidity'),
        "Wind": wind_info.get('speed'),
        "Wind Direction": wind_info.get('deg'),
        "Weather": main_weather.get('main'),
        "Description": main_weather.get('description'),
        "Visibility": visibility
    }

    return forecast

   


    
     
