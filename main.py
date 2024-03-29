from tts import speak
from greet import *
from news import *
from listen import *
from mainListen import *
import os
import threading

# prerequisite section gathering data beforehand so that it can produce results faster when required
def pr():
    geodata=getLocation()
    try:
        city=geodata[0]
        state=geodata[1]
    except TypeError:
        print("Empty")
    else:
        print("Location :"+city+", "+state)

done=False
t=threading.Thread(target=pr)
t.start()
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    greet()
    mainListen()