import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

search_term = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params = {
        "term": search_term,        
    }
)

data = response.json()
amount = len(data["results"])

if amount > 1:
    print(f"I've got {amount} jokes about {search_term}. Here's one: ")
    random_joke = choice(data["results"])
    print(random_joke["joke"])    
elif amount == 1:
    print(f"I've got one joke about {search_term}. Here it is: ")
    print(data["results"][0]["joke"])
else:
    print(f"Sorry, I've got no jokes about {search_term}. Please try again. ")
    



#print(data["results"][0]["joke"])
