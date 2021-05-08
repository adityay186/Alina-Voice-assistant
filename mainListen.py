from listen import *
from news import *
from getTime import *
from getDate import getDate
from dateandtime import getDate_Time
from age import age
from getLocation import getLocation
import gtts
from motion import motion
from em import emailer

def mainListen():
    while True:  
        x=listen().lower()
        if "news" in x:
            if "india" in x:
                playNewsIndia()
                doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
                os.system("play "+doyou+" tempo 1.1")
                # speak("Do you want me to do anything else?")
            else:
                playNews()
                doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
                os.system("play "+doyou+" tempo 1.1")
                # speak("Do you want me to do anything else?")

        elif "exit" in x or "no" in x or "no exit" in x:
            exit="Sounds/Alright-Thank-You-for-using-t1619638216.mp3"
            os.system("play "+exit+" tempo 1.1")
            # speak("Alright, Thank You for using this Voice Assistant, have a nice day.")
            break
        
        elif "email" in x or "send email" in x or "send" in x or "send an email" in x:
            emailer()
            doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
            os.system("play "+doyou+" tempo 1.1")

        elif "time" in x:
            if "date" in x:
                getDate_Time()
                doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
                os.system("play "+doyou+" tempo 1.1")
            else:
                getTime()
                doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
                os.system("play "+doyou+" tempo 1.1")
        
        elif "date" in x:
                getDate()
                doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
                os.system("play "+doyou+" tempo 1.1")

        elif "age" in x or "old" in x:
            age()
            doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
            os.system("play "+doyou+" tempo 1.1")

        elif "describe yourself" in x:
            alina="Sounds/Myself-Eleena-Alexas-little-1619638384.mp3"
            os.system("play "+alina+" tempo 1.1")
            # speak("Myself Alina, Alexa's little sister.")
            hm="greetings/How-can-I-help-you1619639087.mp3"
            os.system("play "+hm+" tempo 1.1")
            # speak("How may I help you?")

        elif "where" in x or "where am i" in x or "location" in x or "locate me" in x:
            # speak("You are currently in "+getLocation()[0]+getLocation()[1])
            # located="Sounds/You-are-currently-in1619697928.mp3"
            # os.system("play "+located+" tempo 1.1")
            # speak(getLocation()[0]+getLocation()[1])
            located="Sounds/You-are-currently-in-Valsad-Gu1619698254.mp3"
            os.system("play "+located+" tempo 1.1")
            doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
            os.system("play "+doyou+" tempo 1.1")

        elif "monitor" in x or "home" in x or "monitor my home" in x or "house" in x:
            mt="Sounds/AlrightI-am-now-monitoring-you1620383303.mp3"
            os.system("play "+mt+" tempo 1.1")
            motion()
            break
        
        elif "vaccinations" in x or "vaccines" in x or "vaccinations have started" in x or "have vaccinations" in x or "vaccination" in x:
            ok_let_me_check="Sounds/OKLet-me-check1620390574.mp3"
            os.system("play "+ok_let_me_check+" tempo 1.1")
            time.sleep(0.5)
            vaccine_check()
            doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
            os.system("play "+doyou+" tempo 1.1")

        else:
            icouldnot="Sounds/Sorry-I-could-not-do-that-at-1619638005.mp3"
            os.system("play "+icouldnot+" tempo 1.1")
            # speak("Sorry, I could not do that at this point of time, but I may get future updates")
            doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
            os.system("play "+doyou+" tempo 1.1")
            # speak("Do you want me to do anything else?")