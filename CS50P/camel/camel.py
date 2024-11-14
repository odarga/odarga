input = input("camelCase: ")

for i in input:
    if i.isupper():
        print("_", end = "")
    print(i.lower(), end = "")

print()
