
import time
# get current time
date_time1 = time.strftime("%-I")
date_time2 = time.strftime("%M")
date_time3= time.strftime("%p")
from tts import *

# print(date_time1,date_time2,date_time3)

def getTime(x,y,z):
    h=x
    m=y
    ampm=z
    val=None
    # h=date_time1 = time.strftime("%-I")
    # m=date_time2 = time.strftime("%M")
    # ampm=date_time3= time.strftime("%p")
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
        speak("The time is "+" 12 "+" noon")