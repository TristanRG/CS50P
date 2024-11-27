def main():
    while True:
        try:
            fractions = input("Fraction: ")
            x, y = fractions.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                  continue

            if x > y:
                  continue

            fraction = x / y
            percent = fraction * 100

            if percent >= 99:
                  print("F")
                  break

            elif percent <= 1:
                  print("E")
                  break

            else:
                print(f"{round(percent)}%")
                break

        except ValueError:
                pass


        except ZeroDivisionError:
                pass




main()
