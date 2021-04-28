from tts import speak
from greet import *
from news import *
from listen import *
from mainListen import *
import os

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    greet()
    mainListen()