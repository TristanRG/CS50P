import emoji

def main():
    value = input("Input: ")
    result = emoji.emojize(value, language="alias")
    print(f"{result}")


main()



