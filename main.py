from fair_price import fair_price
from hangman import hangman
from rock_paper_cissor import rock_paper_cissor

game_mode = {
    0 : "Single player",
    1 : "Two player",
}
solo_games = {
    0 : "The fair price game",
    1 : "The Hangman's game",
    2 : "Rock paper cissors game"
}

# TODO : Implement two player mode with two scores
def main():
    score = 0
    input("Welcome to the mini games competition. Will you outdo yourself and get a huge score?, press Enter to start")
    while 1:
        user_input = input()
        if user_input == "":
            break
    print("Let's start the solo scoring mode games with", solo_games.get(0))
    # fair score game 
    score = score + fair_price.guess_number()

    print("Let's continue with", solo_games.get(1))
    # hangman's game
    mode_choose = int(input("Choose a mode for hangman's game: \n 0. Single player  \n 1. Two player \n"))
    if(mode_choose not in game_mode.keys()):
        print("Invalid mode choose, please try again!")
        return main()
    if(mode_choose == game_mode.get("Single player")):
        score = score + hangman.single_player()
    else:
        score = score + hangman.two_player()

    # Rock paper cissors game
    print("Let's continue with", solo_games.get(2))
    score = score + rock_paper_cissor.play_one_player()

    # Final score
    print("Your final score is {}, you have an average of {}".format(score, score / len(games)))
    print("Thanks for playing!")

if __name__ == '__main__':
    main()
