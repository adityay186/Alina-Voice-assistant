import datetime

from tts import speak
def age():
    today = datetime.date.today()
    start = datetime.date(2021, 4, 26)
    diff = today - start
    age=diff.days
    speak("I am "+str(age)+" days old.")