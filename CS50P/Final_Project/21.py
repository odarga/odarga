import re
import csv
import random
import time
from update import update_db
from printcard import print_one_closed, print_all_open


# Class for a player
class User:

    def __init__(self, username, balance = 0):
        self.username = username
        self.balance = float(balance)

    # Depositing money
    def deposit(self, amount):
        self.balance += amount

    # Withdrawing money
    def withdraw(self, amount):
        self.balance -= amount

    # Updating balance after bet
    def bet(self, amount):
        self.balance -= amount

    # Updating balance after win
    def win(self, amount):
        self.balance += amount


def main():
    print("\nWelcome to the Basic 21 Game!")
    # Signup or Login
    while True:
        first_action = input("\nPress 's' for signup, press 'l' for login: ")
        if first_action.lower() in ("s", "l"):
            break
        else:
            print("\nInvalid input!")
    # If s is selected first sign up and log in, elif l is selected log in
    try:
        if first_action.lower() == "s":
            signup()
            login()
        else:
            login()
    except EOFError:
        print()
        main()


# Signup
def signup():
    usernames = []
    print("\nSIGN UP - Press control-d to go main menu.")
    # Reading usernames from db
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            usernames.append(row["username"])
    # Getting username and checking availabiliy
    while True:
        username = input("\nUsername: ")
        if username in usernames:
            print("\nUsername already taken!")
        elif not username:
            print("\nPlease enter username!")
        else:
            break
    # Getting password
    while True:
        password = input("\nPassword (6 - 12 characters, only letters and numbers are allowed): ")
        # Checking password format
        if re.search(r"([a-z]|[A-Z]|[0-9]){6,12}", password):
            break
    # Writing user to db
    with open("users.csv", "a") as file:
        fieldnames = ["username", "password", "balance"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writerow({"username": username, "password": password, "balance": 0})
    print("\nSuccessfull signed up!")


# Login
def login():
    usernames = []
    passwords = []
    balances = []
    print("\nLOG IN - Press control-d to go main menu.")
    # Reading usernames and passwords from db
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            usernames.append(row["username"])
            passwords.append(row["password"])
            balances.append(row["balance"])
    # Getting username and password and checking correctness of information
    while True:
        username = input("\nUsername: ")
        password = input("\nPassword: ")
        if not username:
            print("\nPlease enter username!")
        elif username not in usernames:
            print("\nUsername does not esixt!")
        else:
            index = usernames.index(username)
            if password == passwords[index]:
                print("\nSuccessfull logged in!")
                # Logged in and activating user class
                user = User(username, balances[index])
                game(user)
                break
            else:
                print("\nWrong password!")


def game(user):
    try:
        print("\nPress control-d to log out.")
        print(f"\nYour balance: ${user.balance:,.2f}")
        # Deposit or Withdraw or Play
        while True:
            second_action = input("\nPress 'd' to deposit money, press 'w' to withdraw money, press 'p' to play: ")
            if second_action.lower() in ("d", "w", "p"):
                break
            else:
                print("\nInvalid input!")
        # Deposit money
        if second_action.lower() == "d":
            while True:
                try:
                    deposit_amount = float(input("\nDeposit amount: "))
                except ValueError:
                    print("\nInvalid amount!")
                else:
                    # Depositing money
                    user.deposit(deposit_amount)
                    # Updating db after deposit
                    update_db(user)
                    game(user)
                    break
        # Withdraw money
        elif second_action.lower() == "w":
            while True:
                try:
                    withdraw_amount = float(input("\nWithdraw amount: "))
                except ValueError:
                    print("\nInvalid amount!")
                else:
                    # Checking if there are enough balance
                    if withdraw_amount > user.balance:
                        print("\nNot enough balance!")
                        continue
                    else:
                        # Withdrawing money
                        user.withdraw(withdraw_amount)
                        # Updating db after withdraw
                        update_db(user)
                        game(user)
                        break
        # Play
        else:
            play(user)
    except EOFError:
        user = None
        print()
        main()


# Playing game
def play(user):
    # 2 gaming decks
    deck = ["1-♥", "2-♥", "3-♥", "4-♥", "5-♥", "6-♥", "7-♥", "8-♥", "9-♥", "10-♥", "J-♥", "Q-♥", "K-♥", "A-♥",
            "1-♥", "2-♥", "3-♥", "4-♥", "5-♥", "6-♥", "7-♥", "8-♥", "9-♥", "10-♥", "J-♥", "Q-♥", "K-♥", "A-♥",
            "1-♣", "2-♣", "3-♣", "4-♣", "5-♣", "6-♣", "7-♣", "8-♣", "9-♣", "10-♣", "J-♣", "Q-♣", "K-♣", "A-♣",
            "1-♣", "2-♣", "3-♣", "4-♣", "5-♣", "6-♣", "7-♣", "8-♣", "9-♣", "10-♣", "J-♣", "Q-♣", "K-♣", "A-♣",
            "1-♠", "2-♠", "3-♠", "4-♠", "5-♠", "6-♠", "7-♠", "8-♠", "9-♠", "10-♠", "J-♠", "Q-♠", "K-♠", "A-♠",
            "1-♠", "2-♠", "3-♠", "4-♠", "5-♠", "6-♠", "7-♠", "8-♠", "9-♠", "10-♠", "J-♠", "Q-♠", "K-♠", "A-♠",
            "1-♦", "2-♦", "3-♦", "4-♦", "5-♦", "6-♦", "7-♦", "8-♦", "9-♦", "10-♦", "J-♦", "Q-♦", "K-♦", "A-♦",
            "1-♦", "2-♦", "3-♦", "4-♦", "5-♦", "6-♦", "7-♦", "8-♦", "9-♦", "10-♦", "J-♦", "Q-♦", "K-♦", "A-♦",
            ]
    # Points of each card
    points = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    # Shuffling deck
    random.shuffle(deck)
    # Betting
    print("\nMin bet: $1")
    print("\nMax bet: $5")
    print("\nPress control-d to exit game.")
    print(f"\nYour Balance: ${user.balance:,.2f}")
    try:
        while True:
            try:
                bet = int(input("\nBet: "))
            except ValueError:
                print("\nInvalid bet!")
            else:
                if 1 <= bet <= 5 and bet <= user.balance:
                    user.bet(bet)
                    # Updating db after bet
                    update_db(user)
                    break
                # Checking bet ammount
                elif bet < 1:
                    print("\nMin bet: $1")
                elif bet > 5:
                    print("\nMax bet: $5")
                # Checking balance
                else:
                    print("\nNot enough balance!")
    except EOFError:
        print()
        game(user)
    else:
        computer = []
        computer_symbol = []
        player = []
        player_symbol = []
        computer_score = 0
        player_score = 0
        # Two cards for computer
        a, b = deck[0].split("-")
        c, d = deck[1].split("-")
        computer.append(a)
        computer_score += points[a]
        computer.append(c)
        computer_symbol.append(b)
        computer_symbol.append(d)
        print(f"\nComputer: {computer_score} + ?")
        # Printing cards for computer, one closed
        print_one_closed(computer, computer_symbol)
        del deck[0:1]
        # Two cards for player
        e, f = deck[0].split("-")
        g, h = deck[1].split("-")
        player.append(e)
        player.append(g)
        player_score += points[e]
        player_score += points[g]
        player_symbol.append(f)
        player_symbol.append(h)
        print(f"\nPlayer: {player_score}")
        # Printing cards for player
        print_all_open(player, player_symbol)
        del deck[0:1]
        # Hit or stay
        while True:
            third_action = input("\nPress 'h' to hit, press 's' to stand: ")
            if third_action not in ("h", "s"):
                print("\nInvalid input!")
            # Standing
            elif third_action == "s":
                # Computer getting new card until exceeds player score or 21
                while True:
                    computer_score += points[c]
                    time.sleep(1)
                    print(f"\nPlayer: {computer_score}")
                    # Printing cards for computer
                    print_all_open(computer, computer_symbol)
                    print(f"\nPlayer: {player_score}")
                    # Printing cards for player
                    print_all_open(player, player_symbol)
                    # New card for computer
                    if computer_score < player_score:
                        x, y = deck[0].split("-")
                        computer.append(x)
                        computer_score += points[x]
                        computer_symbol.append(y)
                        del deck[0]
                    # Draw
                    elif player_score == computer_score:
                        print(f"\nDraw!")
                        break
                    # Computer wins
                    elif player_score < computer_score <= 21:
                        print(f"\nComputer wins!")
                        break
                    # Player wins
                    else:
                        print(f"\nPlayer wins!")
                        # Getting win
                        user.win(bet * 2)
                        # Updating db after win
                        update_db(user)
                        break
                break
            # Hitting
            else:
                # New card for player
                x, y = deck[0].split("-")
                player.append(x)
                player_score += points[x]
                player_symbol.append(y)
                del deck[0]
                print(f"\nComputer: {computer_score} + ?")
                # Printing cards for computer, one closed
                print_one_closed(computer, computer_symbol)
                print(f"\nPlayer: {player_score}")
                # Printing cards for player
                print_all_open(player, player_symbol)
                # Player busted
                if player_score > 21:
                    computer_score += points[c]
                    time.sleep(0.5)
                    print(f"\nComputer: {computer_score}")
                    # Printing cards for computer
                    print_all_open(computer, computer_symbol)
                    print(f"\nPlayer: {player_score}")
                    # Printing cards for player
                    print_all_open(player, player_symbol)
                    print(f"\nComputer wins!")
                    break
    # New game
    play(user)


if __name__ == "__main__":
    main()
