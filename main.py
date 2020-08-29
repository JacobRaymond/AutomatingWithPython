import requests
from bs4 import BeautifulSoup
url="https://scrapingclub.com/exercise/list_basic/?page=1"
response=requests.get(url)
soup=BeautifulSoup(response.text, "lxml")

#Extract the links
pages=soup.find("ul", class_="pagination")
links=pages.find_all("a", class_="page-link")
print(links)