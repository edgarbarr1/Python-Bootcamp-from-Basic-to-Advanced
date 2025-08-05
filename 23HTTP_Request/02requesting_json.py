from security import safe_requests

url = "https://icanhazdadjoke.com/"

response = safe_requests.get(url, headers = {'Accept': "application/json"})

data = response.json()

print(response.text)
print(response.json())
print(type(data))
print(data["joke"])
