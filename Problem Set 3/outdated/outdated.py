def main():

    list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        date = input("Date: ")

        try:
            month, day, year = date.split("/")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break

        except:

            try:
                new_month, new_day, year = date.split(" ")
                for _ in range(len(list)):
                    if new_month == list[_]:
                        month = _ + 1
                day = new_day.replace(",", "")

                if not new_day.endswith(","):
                    continue

                if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                    break

            except:
                print()
                pass


    print(f"{year}-{int(month):02}-{int(day):02}")




main()
