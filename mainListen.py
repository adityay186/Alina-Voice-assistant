from listen import *
from news import *
def mainListen():
    while True:
        x=listen()
        if "top news" in x:
            playNews()
            speak("Do you want me to do anything else?")
        elif "news from India" in x:
            playNewsIndia()
            speak("Do you want me to do anything else?")
        elif "exit" in x:
            speak("Alright Sir, Thank You for using this Voice Assistant, have a nice day. Good-Bye")
            break
        else:
            speak("Sorry, I could not do that at this point of time")
            speak("Do you want me to do anything else?")