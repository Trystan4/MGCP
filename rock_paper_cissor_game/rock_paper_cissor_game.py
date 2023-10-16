import random
import getpass

choices = ['rock', 'paper', 'scissors']

def play_one_player():
    score = 0
    parties = 10

    while parties > 0:
        print("Enter your choice (rock/paper/scissors): ")
        player_choice = input().lower()
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")
        if player_choice == computer_choice:
            print("Tie!")
            score += 5
        elif player_choice == 'rock' and computer_choice == 'scissors' or \
             player_choice == 'paper' and computer_choice == 'rock' or \
             player_choice == 'scissors' and computer_choice == 'paper':
            print("You win!")
            score += 10
        else:
            print("You lose!")
            score -= 5
        parties -= 1
    return score

def play_two_player():
    score1 = 0
    score2 = 0
    parties = 10

    while parties > 0:
        print("Player 1, enter your choice (rock/paper/scissors): ")
        player1_choice = getpass.getpass().lower()
        print("Player 2, enter your choice (rock/paper/scissors): ")
        player2_choice = input().lower()
        if player1_choice == player2_choice:
            print("Tie!")
            score1 += 5
            score2 += 5
        elif player1_choice == 'rock' and player2_choice == 'scissors' or \
             player1_choice == 'paper' and player2_choice == 'rock' or \
             player1_choice == 'scissors' and player2_choice == 'paper':
            print("Player 1 wins!")
            score1 += 10
            score2 -= 5
        else:
            print("Player 2 wins!")
            score1 -= 5
            score2 += 10
        parties -= 1
    return score1, score2
