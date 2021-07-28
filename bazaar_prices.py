import requests

import difflib
from time import sleep

#Colored output
from colorama import Fore, Back, Style

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

    product_sellPrice = data["products"][trueRequestedProduct]["sell_summary"][0]["pricePerUnit"]
    product_buyPrice = data["products"][trueRequestedProduct]["buy_summary"][0]["pricePerUnit"]
    # difference between sell and buy

    differenceBuySell = product_buyPrice - product_sellPrice

    # amount of items insta sold/bought this week

    salesWeek = data['products'][trueRequestedProduct]['quick_status']['sellMovingWeek']
    buysWeek = data['products'][trueRequestedProduct]['quick_status']['buyMovingWeek']
    print(
        Fore.YELLOW + Style.BRIGHT + "-----------------------------------------------------------------------------" + Style.RESET_ALL)
    print(
        f"One {Style.BRIGHT + Fore.YELLOW}{requestedProduct}{Style.RESET_ALL} sells for {Back.BLACK + Fore.YELLOW + Style.BRIGHT}{str('{:,}'.format(product_sellPrice))}{Style.RESET_ALL} coins ")
    print(
        f"One {Style.BRIGHT + Fore.YELLOW}{requestedProduct}{Style.RESET_ALL} costs {Back.BLACK + Fore.YELLOW + Style.BRIGHT}{str('{:,}'.format(product_buyPrice))}{Style.RESET_ALL} coins ")
    print(
        f"64x {Style.BRIGHT + Fore.YELLOW}{requestedProduct}{Style.RESET_ALL} costs {Back.BLACK + Fore.YELLOW + Style.BRIGHT}{str('{:,}'.format(product_buyPrice * 64))}{Style.RESET_ALL} coins ")
    print("")
    print(
        f"The difference between buy and sell price is {Back.BLACK + Fore.YELLOW + Style.BRIGHT}{str('{:,}'.format(round(differenceBuySell, 2)))}{Style.RESET_ALL} coins")
    print("")
    print("Amount of items insta-bought this week: " + Back.BLACK + Fore.YELLOW + Style.BRIGHT + str(
        "{:,}".format(buysWeek)) + Style.RESET_ALL + " items")
    print("Amount of items insta-sold this week: " + Back.BLACK + Fore.YELLOW + Style.BRIGHT + str(
        "{:,}".format(salesWeek)) + Style.RESET_ALL + " items")
    print(
         Fore.YELLOW + Style.BRIGHT + "-----------------------------------------------------------------------------" + Style.RESET_ALL)

# COde calling functions
connection_info(response)
get_names(response)

#Instead of asking if you want to search an other product, it asks until it gives a valid product
while True:
    while True:
        requestedProduct = input("\nWhat product would you like to search for? | e.g; enchanted lava bucket: ")
        requestedProduct = requestedProduct.replace("_", " ")
        try:
            print_price(response, requestedProduct.lower())
            break
        except KeyError:
            pass
            print(f"Hey! '{Fore.YELLOW + Style.BRIGHT}{requestedProduct}{Style.RESET_ALL}' is not tradable on the bazaar.")

    keepGoing = input("Would you like to search for another product? (y/n): ")
    if keepGoing == "y":
        continue
    else:
        break

print("")
print("Thank you for using Hypixel-Skyblock-Utilities by Lennster1")

# :)