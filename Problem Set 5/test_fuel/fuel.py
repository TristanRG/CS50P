def main():
    while True:
        try:
            fractions = input("Fraction: ")
            percentage = convert(fractions)
            result = gauge(percentage)
            print(result)
            break

        except ValueError:
                pass

        except ZeroDivisionError:
                pass


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    return (x / y) * 100


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
         return "E"
    else:
         return f"{round(percentage)}%"


if __name__ == "__main__":
    main()



