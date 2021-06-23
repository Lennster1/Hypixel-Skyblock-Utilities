import requests
import json

response = requests.get("https://api.hypixel.net/skyblock/bazaar")
if response.status_code != 200:   
    print("There was an error connecting to the server.")
    print("Try again later.")
    exit()
else:
    print("Connection succesful!")

requestedProduct = input ("What product would you like to search for? Please note that multi-worded items require an underscore between spaces. | e.g; enchanted_lava_bucket | ")
trueRequestedProduct = requestedProduct.upper()
print (trueRequestedProduct)
data = requests.get("https://api.hypixel.net/skyblock/bazaar").json()
product_sellPrice = round(data["products"][trueRequestedProduct]["quick_status"]["sellPrice"], 2)
product_buyPrice = round(data["products"][trueRequestedProduct]["quick_status"]["buyPrice"], 2)

print ("One " + str(requestedProduct) + " sells for " + str(product_sellPrice) + " coins ")
print ("One " + str(requestedProduct) + " costs " + str(product_buyPrice) + " coins ")


