import sys

line_number = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

else:
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        for i in lines:
            if i.strip().startswith("#") or i.isspace():
                continue
            else:
                line_number += 1

print(line_number)
