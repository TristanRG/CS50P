import inflect

def main():
    p = inflect.engine()
    name_list = []

    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            formatted_names = p.join(name_list)
            print(f"Adieu, adieu, to {formatted_names}")
            break


main()