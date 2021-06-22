import requests
import json
from time import sleep




response = requests.get("https://api.hypixel.net/skyblock/bazaar")
if response.status_code != 200:
    print("There was an error connecting to the server! Try again later")
    sleep(5)
    exit()
else:
    print("Connection succesful!")


