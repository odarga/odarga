from cs50 import get_string


def main():

    text = get_string("Text: ")

    letters = letter(text)
    words = word(text)
    sentences = sentence(text)

    L = letters / words * 100
    S = sentences / words * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def letter(text):
    count = 0

    for i in text:
        if i.isalpha():
            count += 1

    return count


def word(text):
    count = 1

    for i in text:
        if i == " ":
            count += 1

    return count


def sentence(text):
    count = 0

    for i in text:
        if i == "." or i == "!" or i == "?":
            count += 1

    return count


main()
