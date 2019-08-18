import requests

url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(url, headers={"Accept": "Application/json"})

data = response.json()

print(data["joke"])