import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if re.search(r"[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}", ip):
        n1, n2, n3, n4 = ip.split(".")
        if int(n1) > 255 or int(n2) > 255 or int(n3) > 255 or int(n4) > 255:
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
