import requests

url = "https://wttr.in/Dhaka?format=3"

response = requests.get(url)

print("Weather Report:")
print(response.text)