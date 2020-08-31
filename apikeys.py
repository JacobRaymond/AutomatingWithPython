import requests
import json

#Create a dictionnary with the desired keys (included api key)
parameters={'q': 'Seattle, US', 'APPID': 'ea6e0a7fdee71f1f65f91038d004a334'}

#Create the API request
url='http://api.openweathermap.org/data/2.5/weather'
response=requests.get(url, params=parameters)
print(response.content)

