import requests

def getLocation():
    url = "https://freegeoip.app/json/"
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers)
    c=response.json()["city"]
    s=response.json()["region_name"]
    return c,s