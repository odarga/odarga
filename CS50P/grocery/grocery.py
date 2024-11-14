grocery = {}

while True:
    try:
        item = input()
    except EOFError:
        print()
        break
    else:
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

for i in sorted(grocery):
    print(grocery[i], i.upper())
