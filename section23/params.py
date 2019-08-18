import requests

url = "https://icanhazdadjoke.com/search"

# response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(
    url, 
    headers={"Accept": "Application/json"},
    params = {
        "term": "cat",
        "limit": 1
    }
)

data = response.json()

#print(data["joke"])
print(data["results"][0]["joke"])