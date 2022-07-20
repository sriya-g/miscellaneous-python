from bs4 import BeautifulSoup
from bs4 import NavigableString
from pandas.core.indexes.range import RangeIndex
import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

url = 'https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)

politico = []
thing = {}

main = soup.find('main')
for m in main.descendants:
    if not isinstance(m, NavigableString):
        if m.has_attr('class'):
            if m.attrs['class'][0] == 'story-text__heading-medium':
                if len(thing) != 0:
                    politico.append(thing) #4 is broken
                thing = {}
                thing['Things'] = m.get_text()
            if m.attrs['class'][0] == 'story-text__paragraph':
                text = m.get_text()
                if text.startswith('The move:'):
                    thing['Move'] = text
                elif text.startswith('The impact:'):
                    thing['Impact'] = text
                elif text.startswith('The upshot'):
                    thing['Upshot'] = text
if len(thing) != 0: #appends last entry
    politico.append(thing)

sid_obj = SentimentIntensityAnalyzer()

for i in range (0, len(politico)):
    if 'Impact' in politico[i]: #skips #3
        sentiment_dict = sid_obj.polarity_scores(politico[i]['Impact'])
        politico[i]['neg%'] = sentiment_dict['neg']*100
        politico[i]['pos%'] = sentiment_dict['pos']*100


td = pd.DataFrame(data=politico, index=range(0,len(politico))) 
print(td)
td.to_csv("politico.csv")