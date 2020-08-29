import requests
from bs4 import BeautifulSoup
url="http://quotes.toscrape.com/"
response=requests.get(url)

#Parse text using lxml
soup=BeautifulSoup(response.text, "lxml")
print(soup)