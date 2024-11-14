def main():
    greeting = input("Greeting: ")
    x = value(greeting)
    print(f"${x}")


def value(greeting):
    if greeting.lower().startswith("hello"): # Checking if text starts with hello
        return 0
    elif greeting.lower().startswith("h"): # Checking if text starts with h
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


