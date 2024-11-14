due = 50

while True:
    print("Amount Due:", due)
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        due = due - coin
    if due <= 0:
        break

print("Change Owed:", 0 - due)
