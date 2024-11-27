import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
        parts = ip.split(".")
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    return False



if __name__ == "__main__":
    main()