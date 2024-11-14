import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Request error, try again")
else:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

rate = float(response["bpi"]["USD"]["rate_float"])
price = rate * n
print(f"${price:,.4f}")


