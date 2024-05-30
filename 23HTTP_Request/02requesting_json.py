import requests

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers = {'Accept': "application/json"}, timeout=60)

data = response.json()

print(response.text)
print(response.json())
print(type(data))
print(data["joke"])
