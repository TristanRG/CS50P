def main():
    initialAmount = 50
    remainingAmount = initialAmount
    while remainingAmount > 0:
        print("Amount Due:", remainingAmount)
        coin = int(input("Insert Coin: "))
        while coin not in [25, 10, 5]:
            print("Amount Due:", remainingAmount)
            coin = int(input("Insert Coin: "))
        remainingAmount -= coin
    if remainingAmount < 0:
        print("Change Owed:", -remainingAmount)
    else:
        print("Change Owed: 0")

main()
