import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"([1-9]|1[0-2])(:[0-5][0-9])?\s(AM|PM)\sto\s([1-9]|1[0-2])(:[0-5][0-9])?\s(AM|PM)", s):
        list = s.split(" ")
        if ":" in list[0]:
            start_hour, start_minute = list[0].split(":")
            start_hour = int(start_hour)
            start_minute = int(start_minute)
        else:
            start_hour = int(list[0])
            start_minute = 0
        start_meridiem = list[1]
        if ":" in list[3]:
            end_hour, end_minute = list[3].split(":")
            end_hour = int(end_hour)
            end_minute = int(end_minute)
        else:
            end_hour = int(list[3])
            end_minute = 0
        end_meridiem = list[4]
    else:
        raise ValueError

    if start_meridiem == "AM" and start_hour == 12:
        start_hour = 0
    elif start_meridiem == "PM" and start_hour != 12:
        start_hour = start_hour + 12
    if end_meridiem == "AM" and end_hour == 12:
        end_hour = 0
    elif end_meridiem == "PM" and end_hour != 12:
        end_hour = end_hour + 12

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()
