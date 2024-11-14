# Greeting
greeting = input("Greeting: ")

if greeting.strip().lower().startswith("hello"): # Checking if text starts with hello
    print("$0")
elif greeting.strip().lower().startswith("h"): # Checking if text starts with h
    print("$20")
else:
    print("$100")

