import random

def two_player():
    word = input("Player 1, enter the word to guess: ").lower()
    return hangman(word)
    

def single_player():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    word = random.choice(words)
    return hangman(word)

def hangman(word):
    guessed_letters = set()
    tries = 6
    score = 100

    while tries > 0:
        guessed_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(guessed_word)
        if guessed_word == word:
            print("Congratulations! You guessed the word!")
            return score / tries
        guess = input("Player 2, guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"Incorrect! You have {tries} tries left.")
    print(f"Game over! The word was {word}.")
    return 0
