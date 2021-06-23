import requests
import json
from time import sleep
keepGoing = "y"
response = requests.get("https://api.hypixel.net/skyblock/bazaar")
if response.status_code != 200:   
    print("There was an error connecting to the server.")
    sleep(2)
    print("Try again later.")
    exit()
else:
    print("Connecting to the server... ")
    sleep(2)
    print("Connection succesful!")
    sleep(1)
    print("Getting data...")
    sleep(2)
    print("Data successfully recived!")
    sleep(1)
while keepGoing == "y": 
    requestedProduct = input ("What product would you like to search for? Please note that multi-worded items require an underscore between spaces. | e.g; enchanted_lava_bucket | ")
    trueRequestedProduct = requestedProduct.upper()
    print (trueRequestedProduct)
    data = requests.get("https://api.hypixel.net/skyblock/bazaar").json()
    try: 
        product_sellPrice = data["products"][trueRequestedProduct]["sell_summary"][0]["pricePerUnit"]
        product_buyPrice = data["products"][trueRequestedProduct]["buy_summary"][0]["pricePerUnit"]
        print ("One " + str(requestedProduct) + " sells for " + str(product_sellPrice) + " coins ")
        print ("One " + str(requestedProduct) + " costs " + str(product_buyPrice) + " coins ")
    except KeyError:
        pass
        print("Hey! That item doesnt exist!")
    keepGoing = input ("Would you like to search for another product? (y/n) ")
    if keepGoing == "n":
        break
print("Thank you for using Hypixel-Skyblock-Utilities by Lennster1")



