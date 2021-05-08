import os
import time
import subprocess
import smtplib
from tts import speak
from listen import listen

def mailer(receiver,message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("adityactms@gmail.com", "myselfaditya")
    s.sendmail("adityactms@gmail.com", receiver, message)
    s.quit()
    sendmessage()
    em="Sounds/The-email-has-been-sent1620499047.mp3"
    os.system("play "+em+" tempo 1.1")
    print("Mail Sent")

def sendmessage():
    subprocess.Popen(['notify-send', "Mail Sent"])
    return

def contacts(rc):
    cont={
        "aditya":"20190802060@dypiu.ac.in",
        "raj":"20190802013@dypiu.ac.in",
    }
    return cont[rc]

def emailer():
    al="Sounds/To-whom-do-you-want-to-send-an1620499811.mp3"
    os.system("play "+al+" tempo 1.1")
    rec=listen().lower()
    for i in range(1):
        if "don't send" in rec or "stop" in rec or "no don't send" in rec:
            ok="Sounds/Okay1620499210.mp3"
            os.system("play "+ok+" tempo 1.1")
            break
        
    else:
        try:
            em=contacts(str(rec))
            print(em)
        except KeyError:
            sorry="Sounds/SorryI-could-not-find-the-cont1620499348.mp3"
            os.system("play "+sorry+" tempo 1.1")
            emailer()
        else:
            sorry="Sounds/Andwhat-is-the-message1620499422.mp3"
            os.system("play "+sorry+" tempo 1.1")
            m=listen().lower()
            semail="Sounds/AlrightI-am-sending-the-email1620499479.mp3"
            os.system("play "+semail+" tempo 1.1")
            mailer(str(em),m)