import requests
from geopy.geocoders import Nominatim
# base URL
geolocator = Nominatim(user_agent="Locating address")

def country(name):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = name
    location = geolocator.geocode(CITY)
    if location:
        lat = location.latitude
        lon= location.longitude
    else:
        print("Count not found location of {}".format(CITY))
    print(type(str(lat)))
        
    API_KEY = "e928ad2b77507af6138b2320556e0f83"
    # upadting the URL
    URL = BASE_URL + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + API_KEY

    print(f'URL: {URL}')

    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        data = response.json()

        coordinate = data['coord']
        # print(f"{CITY:-^30}")
        # print(f"latitude: {coordinate['lat']}")
        # print(f"longitude: {coordinate['lon']}")
        # dic = {'latitude':coordinate['lat'],'longitude':coordinate['lon']}
        # print(data)
        return data
    
    else:
    # showing the error message
        print("Error in the HTTP request")
        return 'Sorry City not Found'

