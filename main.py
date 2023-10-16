from fair_price_game import fair_price_game
from hangman_game import hangman_game

game_mode = {
    0 : "Single player",
    1 : "Two player",
}

def main():
    score = 0

    # fair score game 
    score = score + fair_price_game.guess_number()

    # hangman's game
    mode_choose = int(input("Choose a mode for hangman's game: \n 0. Two player \n 1. Single player \n"))
    if(mode_choose not in game_mode.keys()):
        print("Invalid mode choose, please try again!")
        return main()
    if(mode_choose == game_mode.single_player):
        score = score + hangman_game.single_player()
    else:
        score = score + hangman_game.two_player()
        
    # Other games here

    # Final score
    print("Your final score is {}".format(score))

if __name__ == '__main__':
    main()
