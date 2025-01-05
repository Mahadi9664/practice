import requests
import json
import sys


if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command Line argument is not a number")
        sys.exit()

else:
    print("Missing command-line argument")
    sys.exit()


try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    rate = response['bpi']['USD']['rate_float']
    total = rate*value
    print(f"${total:,.4f}")



except requests.RequestException:
    print("RequestsException")
    sys.exit()