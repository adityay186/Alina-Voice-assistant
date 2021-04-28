from tts import speak

def greet():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir!")  
  
    else:
        speak("Good Evening Sir!") 
  
    speak("I am your Voice Assistant")
    speak("How may I help you?")