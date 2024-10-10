import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-09-10&sortBy=publishedAt&language=en&apiKey=5f0e4ebdff65433abf307f351df3df2d"  #Please use your API key for this
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")