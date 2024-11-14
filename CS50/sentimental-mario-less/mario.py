from cs50 import get_int

while True:
    h = get_int("Height: ")
    if h > 0 and h <= 8:
        break

for i in range(h):
    for _ in range(h - i - 1):
        print(" ", end = "")
    for _ in range(i + 1):
        print("#", end = "")
    print()


