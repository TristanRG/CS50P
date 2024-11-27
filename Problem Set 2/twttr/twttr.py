def main():
    text = input("Input: ")
    result = ""
    for char in text:
        if char != "U" and char != "u" and char != "A" and char != "a" and char != "E" and char != "e" and char != "I" and char != "i" and char != "O" and char != "o":
            result += char

    print("Output:", result)


main()
