def main():
    text = input("Input: ")
    final_result = shorten(text)


    print("Output:", final_result)


def shorten(word):
    result = ""
    for char in word:
        if char != "U" and char != "u" and char != "A" and char != "a" and char != "E" and char != "e" and char != "I" and char != "i" and char != "O" and char != "o":
            result += char
    return result


if __name__ == "__main__":
    main()
