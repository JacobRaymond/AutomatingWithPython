import requests
import json

#Create a dictionnary with the desired key (upc here)
parameters={'upc': '079400027252'}

#Create the API request
url='https://api.upcitemdb.com/prod/trial/lookup?'
response=requests.get(url, params=parameters)
print(response.url)

#Obtain content
content=response.content #Import in JSON
info=json.loads(content) #Convert to Python dictionary

#Extract the name and brand
item=info['items']
itemInfo=item[0] #First element of the item dictionary
title=itemInfo['title']
print(title)
brand=itemInfo['brand']
print(brand)




