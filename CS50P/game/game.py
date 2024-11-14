from random import randint

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            break
        else:
            continue

number = randint(1, n)

while True:
    try:
        g = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if g <= 0:
            continue
        elif g < number:
            print("Too small!")
            continue
        elif g > number:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
