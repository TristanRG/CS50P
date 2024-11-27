import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError(1)

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    if start_minute is None:
        start_minute = "00"
    if end_minute is None:
        end_minute = "00"

    start_hour, start_minute = int(start_hour), int(start_minute)
    end_hour, end_minute = int(end_hour), int(end_minute)

    if not(0 <= start_hour <= 12 and 0 <= start_minute < 60):
        raise ValueError(1)
    if not(0 <= end_hour <= 12 and 0 <= end_minute < 60):
        raise ValueError(1)

    start_hour = convert_to_24_hour(start_hour, start_period)
    end_hour = convert_to_24_hour(end_hour, end_period)

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

def convert_to_24_hour(hour, period):
    if period == "AM":
        return hour % 12
    elif period == "PM":
        return hour % 12 + 12

if __name__ == "__main__":
    main()
