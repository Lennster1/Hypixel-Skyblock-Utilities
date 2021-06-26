import os

# Install packages if not already present
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

# define connection_info, checks if api is working
def connection_info(response):
    if response.status_code != 200:
        print("There was an error connecting to the server.")
        sleep(2)
        print("Try again later.")
        exit()
    else:
        print("Connecting to the server... ")
        sleep(1)
        print("Connection successful!")
        sleep(1)
        print("Getting data...")
        sleep(1)
        print("Data successfully recived!")
        sleep(1)


# Get a list of all items' names
def get_names(data):
    data = data.json()
    for i in data["products"]:
        names.append(i)


# define showing the output
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
        #difference between sell and buy
        diff = product_buyPrice - product_sellPrice
        #amount of items insta sold/bought this week
        salesweek = data['products'][trueRequestedProduct]['quick_status']['sellMovingWeek']
        buysweek = data['products'][trueRequestedProduct]['quick_status']['buyMovingWeek']
        print("-----------------------------------------------------------------------------")
        print(f"One {requestedProduct} sells for {str('{:,}'.format(product_sellPrice))} coins ")
        print(f"One {requestedProduct} costs {str('{:,}'.format(product_buyPrice))} coins ")
        print("")
        print(f"The difference between buy and sell price is {str('{:,}'.format(round(diff)))} coins")
        print(f"The difference between buy and sell price after tax is {str('{:,}'.format(round(diff - 1/100 * product_buyPrice)))} coins")
        print(f"")
        print(f"Amount of items insta-bought this week: {buysweek}")
        print(f"Amount of items insta-sold this week: {salesweek}")
        print("-----------------------------------------------------------------------------")

    except KeyError:
        pass
        print(f"Hey! '{requestedProduct}' is not tradable on the bazaar.")


# COde calling functions
connection_info(response)
get_names(response)

keepGoing = "y"
# Forever if keepGoing is y, do this stuff. If not, thank and stop
while keepGoing == "y":
    requestedProduct = input("\nWhat product would you like to search for? | e.g; enchanted lava bucket: ")
    requestedProduct = requestedProduct.replace("_", " ")

    print_price(response, requestedProduct.lower())

    keepGoing = input("Would you like to search for another product? (y/n) ")
    if keepGoing == "n":
        break
print("Thank you for using Hypixel-Skyblock-Utilities by Lennster1")

# :)