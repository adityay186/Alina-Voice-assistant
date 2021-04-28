from tts import speak
import os
def greet():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        morning= "greetings/Good-Morning-Sir1619636836.mp3"
        os.system("play "+morning+" tempo 1.2")
  
    elif hour>= 12 and hour<18:
        afternoon= "greetings/Good-Afternoon-Sir1619636891.mp3"
        os.system("play "+afternoon+" tempo 1.2")
  
    else:
        evening= "greetings/Good-Evening-Siremphasis-leve1619635928.mp3"
        os.system("play "+evening+" tempo 1.2")
  
    imyva= "greetings/I-am-your-Voice-Assistant1619636026.mp3"
    os.system("play "+imyva+" tempo 1.2")
    hmihy= "greetings/How-may-I-help-you1619636115.mp3"
    os.system("play "+hmihy+" tempo 1.2")

greet()