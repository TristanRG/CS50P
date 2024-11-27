def main():

    d = {}

    while True:
        try:
            item = input()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1

        except EOFError:
            upper_case = [(key.upper(), count) for key, count in d.items()]
            upper_case.sort()

            for key, count in upper_case:
                print(f"{count} {key}")
            break


main()
