import csv


# Updating db
def update_db(user):
    usernames = []
    passwords = []
    balances = []
    # Reading old db
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            usernames.append(row["username"])
            passwords.append(row["password"])
            balances.append(row["balance"])
    # Updating values
    balances[usernames.index(user.username)] = user.balance
    # Writing new db
    with open("users.csv", "w") as file:
        fieldnames = ["username", "password", "balance"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        for i in usernames:
            index = usernames.index(i)
            writer.writerow({"username": i, "password": passwords[index], "balance": balances[index]})
