from datetime import datetime
from tts import *
def getDate():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")
    speak("The date is :"+dt_string)