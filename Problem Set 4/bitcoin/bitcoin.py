import requests
import sys


def main():

    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        bitcoin_number = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        usd_rate_float = response["bpi"]["USD"]["rate_float"]
        total = usd_rate_float * bitcoin_number
        print(f"${total:,.4f}")

    except ValueError:
        sys.exit(1)

    except requests.RequestException:
        sys.exit(1)


main()
