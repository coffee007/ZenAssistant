import requests
def dadjoke():
    url = 'https://icanhazdadjoke.com'
    response = requests.get(url, headers={"Accept": "application/json"})
    return dict(response.json()).get("joke")