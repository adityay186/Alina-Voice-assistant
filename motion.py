import requests
import json
import time
from loading import loading
import os
link="https://api.thingspeak.com/channels/1376677/fields/1.json?api_key=JSFE41V8RBGGFW64&results=2"
r = requests.get('https://api.thingspeak.com/channels/1376677/fields/1.json?api_key=JSFE41V8RBGGFW64&results=2')
val = json.loads(r.text)["channel"]["last_entry_id"]
i=1

def motion():
    print("Home Monitor : ")
    global val
    global i
    while True:
        loading()
        r2 = requests.get('https://api.thingspeak.com/channels/1376677/fields/1.json?api_key=JSFE41V8RBGGFW64&results=2')
        val2=json.loads(r2.text)["channel"]["last_entry_id"]
        if val2==val:
            print(i,"No Detection :",val2)
            print()
            i=i+1
        else:
            print(i,"Motion Detected :",val2)
            motion="Sounds/Some-motion-has-been-detected-1620374756.mp3"
            os.system("play "+motion+" tempo 1.1")
            print()
            val=val+1
            i=i+1
            print("Take Action Immediately")
            break