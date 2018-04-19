import requests
import json
import time


def get_price(r):
    return r.json()["USD"]["last"]

def main():
    # Get a request from an API
    r = requests.get("https://blockchain.info/ticker")
    if (r.status_code == 200):
        print("Success! Site is up.")
    elif (r.status_code == 400):
        print("Bad request")
    data = r.json()
    last_price = data["USD"]["last"]
    stream(last_price)

def stream(price):
    last_price = price
    time.sleep(1)
    r = requests.get("https://blockchain.info/ticker")

    ## If the request get an OK resposne, the program continues
    if (r.status_code == 200):

        if(get_price(r) > last_price):
            print("UP: "+ str(get_price(r)), "BY "+ str(get_price(r) - last_price))
        elif (get_price(r) < last_price):
            print("DOWN: "+ str(get_price(r)), "BY "+str(last_price-get_price(r)))
        else:
            print("SAME: " + str(last_price))

        last_price = get_price(r)
        stream(last_price)

if __name__ == '__main__':
    main()
