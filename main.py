# KROGER API EXAMPLE - https://developer.kroger.com/api-products
import requests
from helper import get_token_with_scope

# PRODUCT API - https://developer.kroger.com/api-products/api/product-api-public
token = get_token_with_scope("product.compact")
headers = {"Authorization": f"Bearer {token}"}
params = {
    "filter.brand": "Oatly",
    "filter.term": "milk",
    "filter.limit": 5
}

resp = requests.get('https://api.kroger.com/v1/products', headers=headers, params=params)
resp = resp.json()
print(resp)
