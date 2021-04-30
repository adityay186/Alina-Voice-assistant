import requests

def getLocation():
    url = "https://freegeoip.app/json/"
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    try:
        response = requests.request("GET", url, headers=headers)
    except requests.exceptions.ConnectionError:
        print("No Internet Connection")
    else:
        c=response.json()["city"]
        s=response.json()["region_name"]
        return c,s