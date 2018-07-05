import random

def roll_2dice():
    dice = []
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    dice.append(die1)
    dice.append(die2)
    return dice

print("What is your name?")
name = raw_input("> ")
print("Hello, " + name + "!")


dice = roll_2dice()
total = dice[0] + dice[1]

print("Rolling the dice...")
print("Die 1: " + str(dice[0]))
print("Die 2: " + str(dice[1]))
print("Total value: " + str(total))


if total > 7:
    print(str(name) + " won!")
else:
    print(str(name) + " lost.")


