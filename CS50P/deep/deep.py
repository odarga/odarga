# Asking for an anwer
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if answer.strip().isdigit() and int(answer.strip()) == 42: # Checking if the answer is 42
    print("Yes")
elif answer.replace("-"," ").lower().strip() == "forty two": # Cheking if the answer is forty-two or forty two
    print("Yes")
else:
    print("No")
