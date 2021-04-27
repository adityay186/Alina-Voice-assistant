# import requests

# import json

# r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f8c963cf1fcf46c8bac952f272bc0da0")

# # r = requests.get("https://newsapi.org/v2/everything?q=india&from=2021-03-26&sortBy=publishedAt&apiKey=f8c963cf1fcf46c8bac952f272bc0da0")

# news_data=r.json()
# # print(news_data)
# l=len(news_data["articles"])

# for i in range(l):
#     k=news_data["articles"][i]["description"]
#     if k!=None:
#         print(k)
#         print("\n")

from tts import speak
from greet import *
while True:
    greet()