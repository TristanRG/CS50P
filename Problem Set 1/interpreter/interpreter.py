def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        result = x + z
        print(float(result))

    elif y == "-":
        result = x - z
        print(float(result))

    elif y == "/":
        result = x / z
        print(float(result))

    elif y == "*":
        result = x * z
        print(float(result))


main()
