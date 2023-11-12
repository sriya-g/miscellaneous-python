from bs4 import BeautifulSoup
import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

heatmap = []
cnn = {"News Source":"CNN"}
fox = {"News Source":"Fox News"}
msnbc = {"News Source":"MSNBC"}
huffpost = {"News Source":"Huffpost"}
nbc = {"News Source":"NBC"}
usatoday = {"News Source":"USA Today"}

def senscore(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    posScore = sentiment_dict["pos"]*100
    posScore = round(posScore, 2)
    return posScore

url = "https://www.cnn.com/2022/01/13/opinions/bidens-approval-rating-history-zelizer/index.html"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "article__content").getText()
cnn["Joe Biden"] = senscore(text)

url = "https://www.cnn.com/2022/01/15/us/january-6-martin-luther-king-jr-birthday-blake-cec/index.html"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "article__content").getText()
cnn["Donald Trump"] = senscore(text)

url = "https://www.foxnews.com/politics/bidens-legislative-agenda-going-nowhere-one-year-into-presidency"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "article-body").getText()
fox["Joe Biden"] = senscore(text)

url = "https://www.foxnews.com/media/graham-trump-is-indispensable-gop-leader-like-it-or-not"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "article-body").getText()
fox["Donald Trump"] = senscore(text)

url = "https://www.msnbc.com/opinion/biden-cheney-2024-would-be-terrible-idea-just-ask-abe-n1287532"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "article-body__content").getText()
msnbc["Joe Biden"] = senscore(text)

url = "https://www.msnbc.com/opinion/why-donald-trump-hammering-ron-desantis-vaccines-n1287414"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "article-body__content").getText()
msnbc["Donald Trump"] = senscore(text)

url = "https://www.huffpost.com/entry/biden-approval-ratings-covid-infrastructure_n_61e1b476e4b0a864b07241d9"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "entry__content-list js-main-content-list").getText()
huffpost["Joe Biden"] = senscore(text)

url = "https://www.huffpost.com/entry/kevin-mccarthy-donald-trump-jan-6-confession_n_61e28c3ee4b01f707da37e60"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "entry__content-list js-main-content-list").getText()
huffpost["Donald Trump"] = senscore(text)

url = "https://www.nbcnews.com/politics/white-house/biden-plans-executive-action-police-reform-revive-stalled-issue-n1287454"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "article-body__content").getText()
nbc["Joe Biden"] = senscore(text)

url = "https://www.nbcnews.com/politics/donald-trump/inside-trump-s-secretive-endorsement-operation-n1287383"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "article-body__content").getText()
nbc["Donald Trump"] = senscore(text)

url = "https://www.usatoday.com/story/opinion/2022/01/13/supreme-court-mandates-and-voter-rights-biden-takes-more-losses/6516516001/"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "gnt_ar_b").getText()
usatoday["Joe Biden"] = senscore(text)

url = "https://www.usatoday.com/story/news/politics/2022/01/11/trump-rally-speechwriter-new-subpoenas-jan-6-committee/9177252002/"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)
text = soup.find(class_ = "gnt_ar_b").getText()
usatoday["Donald Trump"] = senscore(text)

heatmap.append(cnn)
heatmap.append(fox)
heatmap.append(msnbc)
heatmap.append(huffpost)
heatmap.append(nbc)
heatmap.append(usatoday)

td = pd.DataFrame(data=heatmap, index=range(0,len(heatmap)))
td = td.set_index("News Source") 
print(td)
#uncomment code below if you want a csv file with the data
#td.to_csv("posmap.csv")

sns.heatmap(td, cmap = "Blues", xticklabels = True, yticklabels = True)
plt.title("Politician Favorability by News Media")
plt.show()
