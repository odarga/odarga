input = input("Input: ")

for i in input:
    if i.lower() in ["a", "e", "i", "o", "u"]:
        continue
    else:
        print(i, end = "")

print()
