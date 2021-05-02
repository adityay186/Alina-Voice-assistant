import requests

url = "https://indianrailways.p.rapidapi.com/findstations.php"

querystring = {"station":"valsad"}

headers = {
    'x-rapidapi-key': "01efd7b9f7msh2d8313d59d1c3aep145b2fjsnba398a049126",
    'x-rapidapi-host': "indianrailways.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)