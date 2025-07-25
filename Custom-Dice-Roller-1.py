import random

dice = int(input("How many sides are on your dice that you are rolling? "))

if 1 <= dice <= 100000000:
    roll = random.randint(1, dice)
    print(f"You rolled a {roll}.")
else:
    print("Sorry, that number of sides is not supported. Try a number between 1 and 100,000,000.")


