import random

words = ["apple", "tiger", "chair", "house", "plant"]
word = random.choice(words)

guessed = []
wrong = 0

while wrong < 6:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("You Won!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        wrong += 1
        print("Wrong Guess! Attempts left:", 6 - wrong)

if wrong == 6:
    print("Game Over! Word was:", word)