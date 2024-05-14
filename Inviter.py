import requests

url = "https://discord.com/api/oauth2/token"
data = {
    'client_id': '1197490282460098560',
    'client_secret': 'rlMK3OxuvjIoz8Z4VrEaP5NO2_R3NFX8',
    'grant_type': 'authorization_code',
    'code': 'NT780fs0R667tA06IEurDbP7R2NnKx',
    'redirect_uri': 'https://xfast0.github.io/'
}

response = requests.post(url, data=data)
print(response.json())
