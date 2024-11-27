import csv
import sys
from tabulate import tabulate

def main():
    name = sys.argv[1]

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not name.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(name) as csvfile:
            csvreader = csv.DictReader(csvfile)
            print(tabulate(csvreader, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
