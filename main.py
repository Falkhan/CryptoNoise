import requests

def main():
    r = requests.get("https://blockchain.info/ticker")
    print(r.status_code)
    data = r.json()
    print(data["USD"])
    last_price = data["USD"]["last"]
    print(last_price)


if __name__ == '__main__':
    main()
