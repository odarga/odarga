import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    n = re.findall(r"um", s.lower())
    m = re.findall(r"[a-z]um|um[a-z]", s.lower())
    return len(n) - len(m)



if __name__ == "__main__":
    main()
