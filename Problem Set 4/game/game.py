import random

def main():
        while True:
             try:
                 level = int(input("Level: "))
                 if level < 1:
                      continue
                 break

             except ValueError:
                  pass


        correct_guess = random.randint(1, level)

        while True:
            try:
                guess = int(input("Guess: "))

                if guess < correct_guess:
                    print("Too small!")

                elif guess > correct_guess:
                    print("Too large!")

                else:
                    exit("Just right!")

            except ValueError:
                pass

main()
