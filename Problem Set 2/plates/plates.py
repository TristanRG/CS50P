def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    found_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and (i == 2 or not found_digit):
                return False
            found_digit = True

        elif found_digit:
            return False

    if not s.isalnum():
        return False
    return True

main()
