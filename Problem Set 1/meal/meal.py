def main():
    time = input("What time is it? ")
    convertedTime = convert(time)
    if convertedTime >= 7 and convertedTime <= 10:
        print("breakfast time")
    elif convertedTime >= 12 and convertedTime <= 16:
        print("lunch time")
    elif convertedTime >= 18 and convertedTime <= 21:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60
    return hours + minutes




if __name__ == "__main__":
    main()
