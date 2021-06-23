import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')


response = requests.get("https://api.hypixel.net/skyblock/bazaar/products?key=" + API_KEY)
if response.status_code != 200:
    print("There was an error connecting to the server. Check that your API KEY is correct. If it is, its probably a hypixel problem")
    print("Try again later.")
    exit()
else:
    print("Connection succesful!")


