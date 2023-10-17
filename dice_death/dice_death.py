import random

def dice_game():
    score = 0
    roll = 0
    while 1:
        roll += 1
        print(f"Roll {roll}:")
        roll_result = random.choice(["death", 2, 3, 4, 5, 6])
        if roll_result == "death":
            score = 0
            print("You rolled death! Game over.")
            break
        else:
            score += roll_result * 10
            print(f"You rolled {roll_result}. Your score is now {score}.")
            choice = input("Do you want to roll again? (y/n) ")
            if choice.lower() == "n":
                break
    return score
