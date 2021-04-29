
import time
import datetime
# get current time
# date_time1 = time.strftime("%-I")
# date_time2 = time.strftime("%M")
# date_time3= time.strftime("%p")
from tts import *

# print(date_time1,date_time2,date_time3)

def getTime():
    val=None
    h=date_time1 = time.strftime("%-I")
    m=date_time2 = time.strftime("%M")
    ampm=date_time3= time.strftime("%p")
    if ampm=="PM":
        if int(h)==12 and int(m)==0:
            val="Noon"
        elif int(h)==12 and int(m)>0:
            val="Afternoon"
        elif int(h)<4:
            val="Afternoon"
        elif int(h)>=4 and int(h)<8:
            val="Evening"
        else:
            val="Night"
    else:
        if int(h)==12 and int(m)==0:
            val="Mid-Night"
        elif int(h)==12 and int(m)>0:
            val="Night"
        elif int(h)<4:
            val="Night"
        else:
            val="Morning"
    strTime = time.strftime("%-I:%M")
    print(strTime)
    if val=="Noon":
        speak("The time is "+strTime+" in the noon")
    elif val=="Afternoon":
        speak("The time is "+strTime+" in the afternoon")
    elif val=="Evening":
        speak("The time is "+strTime+" in the evening")
    elif val=="Night":
        speak("The time is "+strTime+" at night")
    elif val=="Mid-Night":
        speak("The time is "+strTime+" at mid-night")
    elif val=="Morning":
        speak("The time is "+strTime+" in the morning")
getTime()

   
# speak(f"Sir, the time is {strTime}")