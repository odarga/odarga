def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    new_word = word
    for i in word:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            print(i)
            new_word = new_word.replace(i,"")

    return f"{new_word}"


if __name__ == "__main__":
    main()




