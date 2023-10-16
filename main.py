from fair_price_game import fair_price_game

def main():
    score = 0

    # fair score game 
    score = score + fair_price_game.guess_number()

    # Other games here

    # Final score
    print("Your final score is {}".format(score))

if __name__ == '__main__':
    main()
