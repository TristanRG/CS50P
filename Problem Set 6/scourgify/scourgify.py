import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1]) as inputfile:
            reader = csv.DictReader(inputfile)
            new_rows = []
            for row in reader:
                last, first = row["name"].split(", ")
                first = first.strip()
                last = last.strip()
                house = row["house"].strip()
                new_rows.append({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit("File does not exist")

    try:
        with open(sys.argv[2], "w", newline="") as outputfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_rows)
            for row in new_rows:
                print(row["first"], row["last"], row["house"])

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
