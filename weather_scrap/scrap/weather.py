import requests
from bs4 import BeautifulSoup

def description(latitude,longitude):
    BASE_URL = "https://weather.com/weather/today/l/"
    lat= str(latitude)
    lon= str(longitude)
    # upadting the URL
    URL = BASE_URL+ lat +"," +lon+"?par=google"
    reqs = requests.get(URL)
    
    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')
    product_div = soup.find('h1',class_="CurrentConditions--location--kyTeL")
    product_div1 = soup.find('span',{"class":"CurrentConditions--tempValue--3a50n","data-testid":"TemperatureValue"})
    product_div2 = soup.find_all('span',{"class":"Wind--windWrapper--3aqXJ undefined","data-testid":"Wind"})
    product_div3 = soup.find('div',class_="CurrentConditions--phraseValue--2Z18W")
    product_div4 = soup.find_all('p',class_="InsightNotification--text--UxsQt")
    product = []
    wind = [] 
    print(product_div2)
    for data in product_div2:
        wind.append(data.text) 
   
    temp = product_div1.text.strip(' ° ')
    temp = int(temp)-47
    temp = str(temp)
    for i in product_div4:
        product.append(i.text)
    if not product:
        description = "Weather is {}".format(product_div3.text)
    else:
        description = product[0]
    forecast = {
    "title":product_div.text,
    "Temperature":temp,
    "Wind":wind[0].replace("Wind Direction",""),
    "Weather":product_div3.text,
    "Description":description
    }
    return forecast
   


    
     
