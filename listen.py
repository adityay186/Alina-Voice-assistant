#Python 2.x program for Speech Recognition

import speech_recognition as sr
from datetime import *
from tts import *
from playsound import playsound
import os

# def listen():
#     required=-1
#     for index, name in enumerate(sr.Microphone.list_microphone_names()):
#         if "pulse" in name:
#             required= index
#     r = sr.Recognizer()
#     with sr.Microphone(device_index=required) as source:
#         r.adjust_for_ambient_noise(source)
#         file_start= "Google_Start.mp3"
#         os.system("mpg123 " + file_start)
#         print("Say something!")
#         audio = r.listen(source, phrase_time_limit=2)
#     try:
#         input = r.recognize_google(audio)
#         file_end= "Google_End.mp3"
#         os.system("mpg123 " + file_end)
#         print("You said: " + input)
#         return str(input)
#     except sr.UnknownValueError:
#         speak("Sorry, could not understand what you said")
#         speak("Do you want me to do something else Sir?")
#         listen()
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))


# def capture():
#     rec = sr.Recognizer()
#     with sr.Microphone() as source:
#         file_start= "Google_Start.mp3"
#         os.system("mpg123 " + file_start)
#         print('I\'M LISTENING...')
#         audio = rec.listen(source, phrase_time_limit=2)
#     try:
#         text = rec.recognize_google(audio, language='en-US')
#         file_end= "Google_End.mp3"
#         os.system("mpg123 " + file_end)
#         return text
#     except:
#         speak('Sorry, I could not understand what you said.')
#         speak("Do you want me to do anything else, Sir?")
#         capture()

# # listen()
# # print(capture())

def listen():
    x=None
    while True:
        if x==None:
            rec = sr.Recognizer()
            with sr.Microphone() as source:
                file_start= "Google_Start.mp3"
                os.system("mpg123 " + file_start)
                print('I\'M LISTENING...')
                audio = rec.listen(source, phrase_time_limit=3)
            try:
                text = rec.recognize_google(audio, language='en-US')
                file_end= "Google_End.mp3"
                os.system("mpg123 " + file_end)
                x=text
                print(text)
                return text
            except:
                speak('Sorry, I could not understand what you said.')
                speak("Do you want me to do anything else Sir?")
        else:
            break