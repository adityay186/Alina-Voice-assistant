from listen import *
from news import *
def mainListen():
    while True:
        x=listen()
        if "news" in x:
            playNewsIndia()
        else:
            speak("Sorry, I could not do that at this point of time")
        speak("Can I dop something else Sir?")
        y=listen()
        if "exit" in y:
            speak("Alright Sir, Thank You for using this Voice Assistant, have a nice day. Good-Bye")
            break