import requests
import json
import time


def get_price(r):
    return r.json()["USD"]["last"]

def main():
    r = requests.get("https://blockchain.info/ticker")
    print(r.status_code)
    data = r.json()
    #print(data["USD"])
    last_price = data["USD"]["last"]
    while True:
        time.sleep(1)
        r = requests.get("https://blockchain.info/ticker")
        if(get_price(r) > last_price):
            print("UP: "+ str(get_price(r)), "BY "+ str(get_price(r) - last_price))
        elif (get_price(r) < last_price):
            print("DOWN: "+ str(get_price(r)), "BY "+str(last_price-get_price(r)))
        else:
            print("SAME: " + str(last_price))
        last_price = get_price(r)

if __name__ == '__main__':
    main()
