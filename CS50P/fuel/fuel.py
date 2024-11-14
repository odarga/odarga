while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        pass
    else:
        if x > y:
            continue
        else:
            try:
                result = round(float(x) / float(y) * 100)
            except ZeroDivisionError:
                pass
            else:
                break

if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result}%")
