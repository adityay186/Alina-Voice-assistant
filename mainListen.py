from listen import *
from news import *
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

        elif "exit" in x:
            exit="Sounds/Alright-Thank-You-for-using-t1619638216.mp3"
            os.system("play "+exit+" tempo 1.1")
            # speak("Alright, Thank You for using this Voice Assistant, have a nice day.")
            break

        elif "describe yourself" in x:
            alina="Sounds/Myself-Eleena-Alexas-little-1619638384.mp3"
            os.system("play "+alina+" tempo 1.1")
            # speak("Myself Alina, Alexa's little sister.")
            hm="greetings/How-can-I-help-you1619639087.mp3"
            os.system("play "+hm+" tempo 1.1")
            # speak("How may I help you?")

        else:
            icouldnot="Sounds/Sorry-I-could-not-do-that-at-1619638005.mp3"
            os.system("play "+icouldnot+" tempo 1.1")
            # speak("Sorry, I could not do that at this point of time, but I may get future updates")
            doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
            os.system("play "+doyou+" tempo 1.1")
            # speak("Do you want me to do anything else?")