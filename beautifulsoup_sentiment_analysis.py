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

def scrape(url, classname):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, features="lxml")
    text = soup.find(class_=classname).getText()
    return senscore(text)

url = "https://www.cnn.com/2022/01/13/opinions/bidens-approval-rating-history-zelizer/index.html"
cnn["Joe Biden"] = scrape(url, "article__content")

url = "https://www.cnn.com/2022/01/15/us/january-6-martin-luther-king-jr-birthday-blake-cec/index.html"
cnn["Donald Trump"] = scrape(url, "article__content")

url = "https://www.foxnews.com/politics/bidens-legislative-agenda-going-nowhere-one-year-into-presidency"
fox["Joe Biden"] = scrape(url, "article-body")

url = "https://www.foxnews.com/media/graham-trump-is-indispensable-gop-leader-like-it-or-not"
fox["Donald Trump"] = scrape(url, "article-body")

url = "https://www.msnbc.com/opinion/biden-cheney-2024-would-be-terrible-idea-just-ask-abe-n1287532"
msnbc["Joe Biden"] = scrape(url, "article-body__content")

url = "https://www.msnbc.com/opinion/why-donald-trump-hammering-ron-desantis-vaccines-n1287414"
msnbc["Donald Trump"] = scrape(url, "article-body__content")

url = "https://www.huffpost.com/entry/biden-approval-ratings-covid-infrastructure_n_61e1b476e4b0a864b07241d9"
huffpost["Joe Biden"] = scrape(url, "entry__content-list js-main-content-list")

url = "https://www.huffpost.com/entry/kevin-mccarthy-donald-trump-jan-6-confession_n_61e28c3ee4b01f707da37e60"
huffpost["Donald Trump"] = scrape(url, "entry__content-list js-main-content-list")

url = "https://www.nbcnews.com/politics/white-house/biden-plans-executive-action-police-reform-revive-stalled-issue-n1287454"
nbc["Joe Biden"] = scrape(url, "article-body__content")

url = "https://www.nbcnews.com/politics/donald-trump/inside-trump-s-secretive-endorsement-operation-n1287383"
nbc["Donald Trump"] = scrape(url, "article-body__content")

url = "https://www.usatoday.com/story/opinion/2022/01/13/supreme-court-mandates-and-voter-rights-biden-takes-more-losses/6516516001/"
usatoday["Joe Biden"] = scrape(url, "gnt_ar_b")

url = "https://www.usatoday.com/story/news/politics/2022/01/11/trump-rally-speechwriter-new-subpoenas-jan-6-committee/9177252002/"
usatoday["Donald Trump"] = scrape(url, "gnt_ar_b")

heatmap.append(cnn)
heatmap.append(fox)
heatmap.append(msnbc)
heatmap.append(huffpost)
heatmap.append(nbc)
heatmap.append(usatoday)

td = pd.DataFrame(data=heatmap, index=range(0,len(heatmap)))
td = td.set_index("News Source") 
print(td)

td.to_csv("posmap.csv")

sns.heatmap(td, cmap = "Blues", xticklabels = True, yticklabels = True)
plt.title("Politician Favorability by News Media")
plt.show()
