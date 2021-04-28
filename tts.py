def speak(text_to_speak):
    from gtts import gTTS
    import os 
    language="hi"
    myobj = gTTS(text=text_to_speak, lang=language, slow=False)
    myobj.save("speak.mp3")
    os.system("play "+"speak.mp3"+" tempo 1.4")