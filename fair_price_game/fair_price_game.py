import random

def guess_number():
    # generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    
    score = 100

    retry = 0
    # ask the user to guess the number
    while 1:
        user_guess = int(input("Guess a number between 1 and 10: "))
        retry +=1
        # check if the user's guess is correct
        if user_guess == random_number:
            score = score / retry
            print("Congratulations, you guessed the number in {} try! Your score is {}".format(retry, score))
            break
        elif user_guess < random_number:
            print("Sorry, the number is greater. Try again!")
        else:
            print("Sorry, the number is lower. Try again!")
    return score

