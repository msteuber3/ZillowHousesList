import requests

url = "https://zillow-working-api.p.rapidapi.com/client/byaddress"

querystring = {"propertyaddress": "10945 MCVINE AVE LOS ANGELES CA 91040"}

headers = {
    "X-RapidAPI-Key": "a21e225447mshf488525040b1036p1a40ffjsnb99943c1a50a",
    "X-RapidAPI-Host": "zillow-working-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
