from bs4 import BeautifulSoup
from pandas.core.indexes.range import RangeIndex
import requests
import pandas as pd

def parsePol(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page)
    name = soup.find(class_ = "firstHeading").get_text()

    politician = {"Politician": name}

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
    return politician

def getPolLinks():
    links = []
    baseurl = ['https://en.wikipedia.org/wiki/Category:18th-century_presidents_of_the_United_States', 'https://en.wikipedia.org/wiki/Category:19th-century_presidents_of_the_United_States', 'https://en.wikipedia.org/wiki/Category:20th-century_presidents_of_the_United_States', 'https://en.wikipedia.org/wiki/Category:21st-century_presidents_of_the_United_States']
    for url in baseurl:
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page)
        para = soup.find(class_ = "mw-category-generated")
        for x in para.find_all('ul'):
            for y in x.find_all('li'):
                for z in y.find_all('a'):
                    links.append("https://en.wikipedia.org"+z.get('href'))
    print(links)

    pres = []
    for link in links:
        pol = parsePol(link)
        pres.append(pol)
    return pres
    
pres = getPolLinks()
td = pd.DataFrame(data=pres, index=range(0,len(pres))) 
print(td)
td.to_csv("pres21.csv")