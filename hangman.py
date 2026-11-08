import random

with open("words.txt","r")as file:
    words=file.read().splitlines()

secret_word=random.choice(words).lower()

gessed_letters=set()

attempts=6

stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

print("===WELCOME TO HANGMAN GAME===")

while attempts>0:
    print(stages[6-attempts])

    display_word=""

    for letter in secret_word:
        if letter in gessed_letters:
            display_word += letter +" "
        else:
            display_word+="_"

    print("\nWord:", display_word)
    print("Attempts left:", attempts)
    print("Guessed letters:", sorted(gessed_letters))     

    if all(letter in gessed_letters for letter in secret_word):
        print("\nCongratulations!you WON!") 
        print("The word was:",secret_word)
        break

    guess=input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    
    if guess in gessed_letters:
        print("You already guessed that letter!")
        continue   

    gessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")

    else:
        print("Wrong guess!")
        attempts-=1

    if attempts == 0:
        print(stages[6])
        print("\nGame over!You Lost")
        print("Correct word was:",secret_word)
