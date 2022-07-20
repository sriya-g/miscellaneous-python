from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Joe_Biden'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)

#print(soup.find('title'))

#print(soup.prettify())

#print(soup.tbody.get_text())