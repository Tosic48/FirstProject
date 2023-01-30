import requests
BASE_URL = 'https://www.nbrb.by/api/exrates/currencies'
query_params = {
    "limit": 3
}
response = requests.get(f"{BASE_URL}/products", params=query_params)
print(response.json())