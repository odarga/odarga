import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r".+https?://(www\.)?youtube\.com/embed/.+", s):
        shorten = re.sub(r".+https?://(www\.)?youtube\.com/embed/", "", s)
        path = shorten.split('"')
        return f"https://youtu.be/{path[0]}"


if __name__ == "__main__":
    main()
