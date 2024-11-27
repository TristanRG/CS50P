from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birthday = input("Date of birth: ")
    minutes = date_of_birth(birthday)
    print(convert_text(minutes))


def date_of_birth(birth):
    try:
        b = date.fromisoformat(birth)
    except ValueError:
        sys.exit(1)
    else:
        today = date.today()
        sub = today - b
        total = sub.total_seconds() / 60
    return round(total)

def convert_text(num):
    return f"{p.number_to_words(num,andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
