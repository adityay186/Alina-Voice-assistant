import requests
import json
from datetime import datetime
import os
now=datetime.now()
cw=now.strftime("%d-%m-%Y")
r=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=512&date="+cw)
k=json.loads(r.text)

def vaccine_check():
    val=[]
    for i in range(len(k["sessions"])):
        x=k["sessions"][i]["min_age_limit"]
        val.append(x)

    if 18 in val:
        started="Sounds/YesVaccinations-for-18-have-1620390278.mp3"
        os.system("play "+started+" tempo 1.1")
        print("Vaccination Started for 18+ of age")
    else:
        not_started="Sounds/NoVaccinations-for-18-have-n1620390403.mp3"
        os.system("play "+not_started+" tempo 1.1")
        print("Not yet started for 18+ of age")