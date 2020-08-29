import requests
from bs4 import BeautifulSoup
url="http://quotes.toscrape.com/"
response=requests.get(url)

#Parse text using lxml
soup=BeautifulSoup(response.text, "lxml")
#print(soup)

#All quotes have the tag "span" and the class "text"
quotes=soup.find_all("span", class_="text")

#All authors have the tag "small" and the class "author"
authors=soup.find_all("small", class_="author")

#All authors have the tag "a" and the class "tag"
#But there can be more than one tag per quote, so we use the entire quote box
tags=soup.find_all("div", class_="tags")

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags=tags[i].find_all("a", class_="tag")
    for quoteTag in quoteTags:
        print(quoteTag.text)

