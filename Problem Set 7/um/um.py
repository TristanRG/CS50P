import re


def main():
    print(count(input("Text: ")))


def count(s):
    counter = int(0)
    pattern = r"\bum\b"
    match = re.findall(pattern, s, re.IGNORECASE)

    for _ in match:
        counter += 1

    return counter



if __name__ == "__main__":
    main()
