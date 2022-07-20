from bs4 import BeautifulSoup
from pandas.core.indexes.range import RangeIndex
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Joe_Biden'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)

politician = {"Politician":"Joe Biden"}

tb = soup.find(class_ = "infobox vcard")
rows = tb.find_all('tr')
for r in rows:
    th = r.find('th')
    if th is not None:
        ths = th.get_text().strip()
        td = r.find('td')
        if td is not None:
            tds = td.get_text().strip()
            politician[ths] = tds
print(politician)

td = pd.DataFrame(data=politician, index=range(0, 1))
print(td)
#td.to_csv("dbiden.csv")