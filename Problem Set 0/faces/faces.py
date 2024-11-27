def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    inputText = input(str('Please provide a text that contains ":(" or ":)": '))
    convertText = convert(inputText)
    print(convertText)

main()



