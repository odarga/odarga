from cs50 import get_float

while True:
    change = get_float("Change: ")
    if change > 0:
        break

number = 0

while change >= 0.25:
    change = round(change - 0.25, 2)
    number += 1

while change >= 0.100:
    change = round(change - 0.10, 2)
    number += 1

while change >= 0.050:
    change = round(change - 0.05, 2)
    number += 1

while change >= 0.010:
    change = round(change - 0.01, 2)
    number += 1

print(number)
