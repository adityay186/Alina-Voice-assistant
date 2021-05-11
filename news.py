import requests
from tts import *


def playNewsIndia():
    r = requests.get("https://newsapi.org/v2/everything?q=india&from=2021-04-27&sortBy=publishedAt&apiKey=f8c963cf1fcf46c8bac952f272bc0da0")

    news_data=r.json()
    # print(news_data)
    l=len(news_data["articles"])

    for i in range(1):
        k=news_data["articles"][i]["description"]
        source=news_data["articles"][i]["source"]["name"]
        if k!=None:
            speak(source+"से अगली खबर")
            speak(k)

def playNews():
    r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f8c963cf1fcf46c8bac952f272bc0da0")

    news_data=r.json()
    # print(news_data)
    l=len(news_data["articles"])

    for i in range(1):
        k=news_data["articles"][i]["description"]
        source=news_data["articles"][i]["source"]["name"]
        if k!=None:
            speak("News From :"+source)
            speak(k)