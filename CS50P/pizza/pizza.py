import sys
import csv
from tabulate import tabulate

pizzas = []
headers = []
table = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                pizzas.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        headers = pizzas[0]
        for i in pizzas[1:]:
            table.append(i)
        print(tabulate(table, headers, tablefmt="grid"))


