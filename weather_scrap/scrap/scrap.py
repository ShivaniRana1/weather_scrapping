import requests
# base URL

def country(name):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = name
    API_KEY = "Please enter your openweathermap API KEY"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        data = response.json()

        coordinate = data['coord']
        # print(f"{CITY:-^30}")
        # print(f"latitude: {coordinate['lat']}")
        # print(f"longitude: {coordinate['lon']}")
        dic = {'latitude':coordinate['lat'],'longitude':coordinate['lon']}
        return dic
    
    else:
    # showing the error message
        print("Error in the HTTP request")
        return 'Sorry City not Found'

