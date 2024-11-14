def main():
    # Asking for input
    text = input()

    # Calling function converting emoticons to emojis
    text = convert(text)

    # Printing result
    print(text)


def convert(text):
    # Converting emoticons to emojis
    return text.replace(":)","🙂").replace(":(","🙁")


main()
