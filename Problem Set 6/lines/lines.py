import sys

def main():

    name = sys.argv[1]

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if not name.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(name, "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")

    code_lines = 0

    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            code_lines += 1

    print(code_lines)

if __name__ == "__main__":
    main()
