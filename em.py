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
    speak("Mail has been sent.")
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
    speak("Alright, to whom do you want to send an email?")
    rec=listen().lower()
    for i in range(1):
        if "don't send" in rec or "stop" in rec or "no don't send" in rec:
            speak("Alright.")
            break
        
    else:
        try:
            em=contacts(str(rec))
            print(em)
        except KeyError:
            speak("Sorry, I could not find the contact. Please try again.")
            emailer()
        else:
            speak("And, what is the message?")
            m=listen().lower()
            speak("Alright. I am sending the email")
            mailer(str(em),m)