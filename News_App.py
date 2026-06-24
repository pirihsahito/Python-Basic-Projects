import requests
import json

query = input("What type of news are you interested in?: ")
url = f"https://Add link of your NEWS-API"

r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------")