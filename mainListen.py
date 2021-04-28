from listen import *
from news import *
def mainListen():
    while True:
        x=listen().lower()
        if "news" in x:
            if "india" in x:
                playNewsIndia()
                speak("Do you want me to do anything else?")
            else:
                playNews()
                speak("Do you want me to do anything else?")

        elif "exit" in x:
            speak("Alright, Thank You for using this Voice Assistant, have a nice day.")
            break

        elif "describe yourself" in x:
            speak("Myself Alina, Alexa's little sister.")
            speak("How may i help you?")

        else:
            speak("Sorry, I could not do that at this point of time")
            speak("Do you want me to do anything else?")