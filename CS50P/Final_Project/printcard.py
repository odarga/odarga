# Pritning one card open one card closed
def print_one_closed(computer, computer_symbol):
    print(" ___________     ___________ ")
    print("|           |   |           |")
    print(f"| {computer[0]:2s}     {computer[0]:2s} |   |           |")
    print("|           |   |           |")
    print(f"|     {computer_symbol[0]:2s}    |   |           |")
    print("|           |   |           |")
    print(f"| {computer[0]:2s}     {computer[0]:2s} |   |           |")
    print("|___________|   |___________|")


# Printing cards
def print_all_open(player, player_symbol):
    if len(player) == 2:
        print(" ___________     ___________ ")
        print("|           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |")
        print("|           |   |           |")
        print(f"|     {player_symbol[0]:2s}    |   |     {player_symbol[1]:2s}    |")
        print("|           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |")
        print("|___________|   |___________|")
    elif len(player) == 3:
        print(" ___________     ___________     ___________ ")
        print("|           |   |           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |   | {player[2]:2s}     {player[2]:2s} |")
        print("|           |   |           |   |           |")
        print(f"|     {player_symbol[0]:2s}    |   |     {player_symbol[1]:2s}    |   |     {player_symbol[2]:2s}    |")
        print("|           |   |           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |   | {player[2]:2s}     {player[2]:2s} |")
        print("|___________|   |___________|   |___________|")
    elif len(player) == 4:
        print(" ___________     ___________     ___________     ___________ ")
        print("|           |   |           |   |           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |   | {player[2]:2s}     {player[2]:2s} |   | {player[3]:2s}     {player[3]:2s} |")
        print("|           |   |           |   |           |   |           |")
        print(f"|     {player_symbol[0]:2s}    |   |     {player_symbol[1]:2s}    |   |     {player_symbol[2]:2s}    |   |     {player_symbol[3]:2s}    |")
        print("|           |   |           |   |           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |   | {player[2]:2s}     {player[2]:2s} |   | {player[3]:2s}     {player[3]:2s} |")
        print("|___________|   |___________|   |___________|   |___________|")
    elif len(player) == 5:
        print(" ___________     ___________     ___________     ___________     ___________ ")
        print("|           |   |           |   |           |   |           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |   | {player[2]:2s}     {player[2]:2s} |   | {player[3]:2s}     {player[3]:2s} |   | {player[4]:2s}     {player[4]:2s} |")
        print("|           |   |           |   |           |   |           |   |           |")
        print(f"|     {player_symbol[0]:2s}    |   |     {player_symbol[1]:2s}    |   |     {player_symbol[2]:2s}    |   |     {player_symbol[3]:2s}    |   |     {player_symbol[4]:2s}    |")
        print("|           |   |           |   |           |   |           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |   | {player[2]:2s}     {player[2]:2s} |   | {player[3]:2s}     {player[3]:2s} |   | {player[4]:2s}     {player[4]:2s} |")
        print("|___________|   |___________|   |___________|   |___________|   |___________|")
    else:
        print(" ___________     ___________     ___________     ___________     ___________     ___________ ")
        print("|           |   |           |   |           |   |           |   |           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |   | {player[2]:2s}     {player[2]:2s} |   | {player[3]:2s}     {player[3]:2s} |   | {player[4]:2s}     {player[4]:2s} |   | {player[5]:2s}     {player[5]:2s} |")
        print("|           |   |           |   |           |   |           |   |           |   |           |")
        print(f"|     {player_symbol[0]:2s}    |   |     {player_symbol[1]:2s}    |   |     {player_symbol[2]:2s}    |   |     {player_symbol[3]:2s}    |   |     {player_symbol[4]:2s}    |   |     {player_symbol[5]:2s}    |")
        print("|           |   |           |   |           |   |           |   |           |   |           |")
        print(f"| {player[0]:2s}     {player[0]:2s} |   | {player[1]:2s}     {player[1]:2s} |   | {player[2]:2s}     {player[2]:2s} |   | {player[3]:2s}     {player[3]:2s} |   | {player[4]:2s}     {player[4]:2s} |   | {player[5]:2s}     {player[5]:2s} |")
        print("|___________|   |___________|   |___________|   |___________|   |___________|   |___________|")
