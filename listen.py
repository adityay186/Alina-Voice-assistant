#Python 2.x program for Speech Recognition

import speech_recognition as sr
from datetime import *
from tts import *
from playsound import playsound
import os

def listen():
    x=None
    while True:
        if x==None:
            rec = sr.Recognizer()
            with sr.Microphone() as source:
                file_start= "Google_Start.mp3"
                os.system("play "+file_start+" tempo 1.1")
                print('I\'M LISTENING...')
                audio = rec.listen(source, phrase_time_limit=3)
            try:
                text = rec.recognize_google(audio, language='en-US')
                file_end= "Google_End.mp3"
                os.system("play "+file_end+" tempo 1.1")
                x=text
                print("================================================================> USER SAID :    "+text)
                return text
            except:
                sorry="Sounds/Sorry-I-could-not-understand-1619637636.mp3"
                os.system("play "+sorry+" tempo 1.1")
                doyou="Sounds/Do-you-want-me-to-do-anything-1619637731.mp3"
                os.system("play "+doyou+" tempo 1.1")
        else:
            break