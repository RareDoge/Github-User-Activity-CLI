import requests

api_key = "CG-bSntvKgniRj1MQz4b9qv85ge"
url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids" : "ethereum",
    "vs_currencies" : "usd"
}

headers = {
    "accept": "application/json",
    "x-cg-demo-api_key": api_key
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    price = data["ethereum"]["usd"]
    print(f"The current price of {params['ids']} is: ${price}")
else:
    print(f"Error: {response.status_code}")