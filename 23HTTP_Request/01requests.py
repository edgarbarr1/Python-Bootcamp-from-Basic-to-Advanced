import requests

url = "http://google.com"

response = requests.get(url, timeout=60)

print(response.status_code)
