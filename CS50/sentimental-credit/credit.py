from cs50 import get_string


def main():

    number = get_string("Number: ")
    digit = len(number)

    if digit == 13 or digit == 15 or digit == 16:
        validity(number)
    else:
        print("INVALID")


def validity(number):

    i = len(number) - 2
    total = 0

    while i >= 0:
        if int(number[i]) * 2 < 10:
            total += int(number[i]) * 2
        else:
            total += 1 + (int(number[i]) * 2) % 10
        i -= 2

    i = len(number) - 1

    while i >= 0:
        total += int(number[i])
        i -= 2

    digit = len(number)

    if total % 10 != 0:
        print("INVALID")
    else:
        if digit == 13 and number[0] == "4":
            print("VISA")
        elif digit == 16 and number[0] == "4":
            print("VISA")
        elif digit == 16 and number[0] == "5" and (int(number[1]) % 10 > 0 or int(number[1]) % 10 <= 5):
            print("MASTERCARD")
        elif digit == 15 and number[0] == "3" and (number[1] == "4" or number[1] == "7"):
            print("AMEX")
        else:
            print("INVALID")


main()
