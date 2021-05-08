import os
import requests

link="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=396001&date=09-05-2021"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

r=requests.get(link,headers=headers)
l=len(r.json()["sessions"])

def vaccination():
    val=[]
    for i in range(1):
        if l==0:
            no_gov_data="Sounds/SorryNo-Government-Data-is-av1620501969.mp3"
            os.system("play "+no_gov_data+" tempo 1.1")
            break
        else:
            for i in range(l):
                x=r.json()["sessions"][i]["min_age_limit"]
                val.append(x)
        if 18 in val:
            yes_available="Sounds/YesVaccinations-for-18-have-1620390278.mp3"
            os.system("play "+yes_available+" tempo 1.1")
        else:
            no_not_available="Sounds/NoVaccinations-for-18-have-n1620390403.mp3"
            os.system("play "+no_not_available+" tempo 1.1")