from tts import speak
from greet import *
from news import *
from listen import *
from mainListen import *
import os

# prerequisite section gathering data beforehand so that it can produce results faster when required
geodata=getLocation()
city=geodata[0]
state=geodata[1]

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    greet()
    mainListen()