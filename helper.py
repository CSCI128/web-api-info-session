import requests
import base64

def get_token_with_scope(scope: str) -> str:
    CLIENT_ID = ""
    CLIENT_SECRET = ""

    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_header = f"Basic {base64.b64encode(credentials.encode()).decode()}"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": auth_header
    }

    data = {
        "grant_type": "client_credentials",
        "scope": scope
    }

    resp = requests.post('https://api.kroger.com/v1/connect/oauth2/token', headers=headers, data=data)
    resp = resp.json()

    # print("DEBUG:", resp)

    return resp['access_token']
