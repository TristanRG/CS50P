from pyfiglet import Figlet
import random
import sys

def main():

    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        user_answer = input("Input: ")
        random_font = random.choice(fonts)
        figlet.setFont(font = random_font)
        print("Output:" + figlet.renderText(user_answer))


    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.args[2] in figlet.getFont()):
        user_answer = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print("Output:" + figlet.renderText(user_answer))

    else:
        sys.exit("Invalid usage")


main()
