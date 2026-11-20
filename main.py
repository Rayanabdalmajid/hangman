import random
from hangman_art import logo,stages
from hangman_words import word_list

print(logo)

chosen_words = random.choice(word_list)


lives = 6

placeholder = ""
for position in chosen_words:
    placeholder += "_"
print(placeholder)

Game_over = False
correct_letters = []

while not Game_over:
    guess = input("guess a letter: ").lower()
    print(f"number of lives left {lives}/6")

    if guess in correct_letters:
        print(f"You already guessed {guess}")

    display = ""
    for letter in chosen_words:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else :
            display += "_"

    print(display)


    if guess not in chosen_words :
        lives -= 1
        print(f"you guessed {guess}, is not in the word. You lose a life")
        

        if lives == 0:
            Game_over = True
            print(f"The word was {chosen_words}, You lose!")

    elif "_" not in display:
        Game_over = True
        print("Congrats, you win!")

    print(stages[lives])
