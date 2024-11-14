names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)

print()
print("Adieu, adieu, to ", end = "")

if len(names) == 1:
    for x in names:
        print(x, end = "")
elif len(names) == 2:
    print(f"{names[0]} and {names[1]}", end = "")
else:
    for x in names[0 : len(names) - 1]:
        print(f"{x}, ", end = "")
    print(f"and {names[len(names) - 1]}", end = "")

print()
