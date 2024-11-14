import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        print(f"{x} + {y} = ", end = "")
        for j in range(3):
            try:
                answer = int(input())
            except ValueError:
                print("EEE")
                print(f"{x} + {y} = ", end = "")
                continue
            else:
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    print(f"{x} + {y} = ", end = "")
        if answer != x + y:
            print(x + y)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            l = int(input("Level: "))
        except ValueError:
            pass
        else:
            if l in (1, 2, 3):
                return l
            else:
                continue


def generate_integer(level):
    match level:
        case 1: return random.randint(0, 9)
        case 2: return random.randint(10, 99)
        case 3: return random.randint(100, 999)
        case _: raise ValueError


if __name__ == "__main__":
    main()
