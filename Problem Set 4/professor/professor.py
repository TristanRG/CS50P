import random


def main():
    current_level = get_level()
    count = 0
    score = 0

    while count < 10:
        x, y, z = generate_integer(current_level)
        tries = 0

        while tries < 3:
            try:
                user_response = int(input(f"{x} + {y} = "))
                if user_response != z:
                    print("EEE")
                    tries += 1

                else:
                    score += 1
                    break
            except ValueError():
                print("EEE")
                tries += 1

            if tries == 3:
                print(f"{x} + {y} = {z}")

        count += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2 ,3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    else:
        raise ValueError()

    z = x + y
    return x, y, z

if __name__ == "__main__":
    main()
