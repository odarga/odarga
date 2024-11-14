def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Checking if plate contains at least two, at most 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Checking if plate starts with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Finding first number in plate
    for i in range(2, len(s)):
        if s[i].isdigit():
            first_number = i
            break

    # Checking if first number in plate is not zero
    if s[first_number] == "0":
        return False

    # Checking if there is no letter after numbers
    for i in range(first_number + 1, len(s)):
        if s[i].isalpha():
            return False

    # Checking if there is no periods, spaces, or punctuation marks
    for i in range(2, len(s)):
        if s[i].isdigit() == False and s[i].isalpha() == False:
            return False

    return True


if __name__ == "__main__":
    main()
