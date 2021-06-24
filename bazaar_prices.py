import os

# Install packages if not already
try:
    import requests
except Exception:
    print("=" * 32)
    print("Installing required packages...")
    print("=" * 32)
    os.system("pip3 install requests")
finally:
    import requests
import difflib
from time import sleep

response = requests.get("https://api.hypixel.net/skyblock/bazaar")
names = []


# define stuff
def connection_info(response):
    if response.status_code != 200:
        print("There was an error connecting to the server.")
        sleep(2)
        print("Try again later.")
        exit()
    else:
        print("Connecting to the server... ")
        sleep(2)
        print("Connection successful!")
        sleep(1)
        print("Getting data...")
        sleep(2)
        print("Data successfully recived!")
        sleep(1)


# Get a list of all items' names
def get_names(data):
    data = data.json()
    for i in data["products"]:
        names.append(i)


# still defining stuff
def print_price(response, requestedProduct):
    data = response.json()
    trueRequestedProduct = requestedProduct.upper()
    try:
        trueRequestedProduct = difflib.get_close_matches(trueRequestedProduct, names)[0]
        requestedProduct = trueRequestedProduct.replace("_", " ").lower().title()
        print("\n" + requestedProduct)
    except IndexError:
        pass

    try:
        product_sellPrice = data["products"][trueRequestedProduct]["sell_summary"][0]["pricePerUnit"]
        product_buyPrice = data["products"][trueRequestedProduct]["buy_summary"][0]["pricePerUnit"]
        print("One " + str(requestedProduct) + " sells for " + str(product_sellPrice) + " coins ")
        print("One " + str(requestedProduct) + " costs " + str(product_buyPrice) + " coins ")
    except KeyError:
        pass
        print("Hey! '" + requestedProduct + "' is not tradable on the bazaar.")


# ok actual code starts here
connection_info(response)
get_names(response)

keepGoing = "y"

while keepGoing == "y":
    requestedProduct = input("\nWhat product would you like to search for? | e.g; enchanted lava bucket: ")
    requestedProduct = requestedProduct.replace("_", " ")

    print_price(response, requestedProduct.lower())

    keepGoing = input("Would you like to search for another product? (y/n) ")
    if keepGoing == "n":
        break
print("Thank you for using Hypixel-Skyblock-Utilities by Lennster1")

# :)
