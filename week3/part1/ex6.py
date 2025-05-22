import random

bet = input("Place your bet (just for fun): ")

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

print(f"You rolled: {die1} + {die2} = {total}")


# Hardways = same dice, total must be 4, 6, 8, or 10
if die1 == die2:
    if total in [4, 10]:
        print("Hard 4 or 10 → You win 7:1!")
    elif total in [6, 8]:
        print("Hard 6 or 8 → You win 9:1!")
    else:
        print("Hardway total not 4, 6, 8, or 10 → Bet stands.")
else:
    # Easy ways (unequal dice), check if it's 4, 6, 8, or 10
    if total in [4, 6, 8, 10]:
        print("Easy way → You lose!")
    elif total == 7:
        print("You rolled a 7 → You lose!")
    else:
        print("Bet stands.")
