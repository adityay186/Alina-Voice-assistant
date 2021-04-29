from datetime import datetime
import time
import os
now = datetime.now()
dt_string = now.strftime("The date is :"+"%d/%m/%Y"+" and the time is: "+"%H:%M")
print(dt_string)
from tts import speak


def getDate_Time():
    val=None
    # h=date_time1 = time.strftime("%-I")
    # m=date_time2 = time.strftime("%M")
    # ampm=date_time3= time.strftime("%p")
    h=12
    m=0
    ampm="PM"
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
    if val=="Noon":
        speak(dt_string+" in the noon")
    elif val=="Afternoon":
        speak(dt_string+" in the afternoon")
    elif val=="Evening":
        speak(dt_string+" in the evening")
    elif val=="Night":
        speak(dt_string+" at night")
    elif val=="Mid-Night":
        speak(dt_string+" at mid-night")
    elif val=="Morning":
        speak(dt_string+" in the morning")