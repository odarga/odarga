months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    if "/" in date:
        m, d, y = date.split("/")
        try:
            month = int(m)
            day = int(d)
            year = int(y)
        except ValueError:
            pass
        else:
            if month > 12 or day > 31:
                continue
            else:
                print(f"{year:04}-{month:02}-{day:02}")
                break
    elif "," in date:
        m, d, y = date.split(" ")
        d = d.split(",")
        try:
            month = months.index(m) + 1
            day = int(d[0])
            year = int(y)
        except ValueError:
            pass
        else:
            if day > 31:
                continue
            else:
                print(f"{year:04}-{month:02}-{day:02}")
                break


