import requests

website = requests.get(url="http://api.open-notify.org/iss-now.json")
website.raise_for_status()

location = website.json()

longitude = location["iss_position"]["longitude"]
latitude = location["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)