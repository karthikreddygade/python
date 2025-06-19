import random
import hangmanwords
from stages import stages

#word_list = ['apple','bananna','cat','dog']
lives = 7
choosen_word = random.choice(hangmanwords.word_list)
print(choosen_word)
placeholder = ""
length = len(choosen_word)
for word in range(length):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letter = []

while not game_over:
    print(f"{lives}/8")
    guess = input("Enter the letter\n").lower()
    if guess in correct_letter:
        print(f"already guessed {guess}")
    display = ''
    for letter in choosen_word:
        if letter == guess:
            display += letter
           # correct_guess = True
            correct_letter.append(guess)
            # print(correct_letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"


    print(display)
    if guess not in choosen_word:
        lives -= 1
        print(f"your guess is not in the words {guess}")
        if lives == 0:
            game_over = True
            print(f"you lose and the correct word is{word}")

    if "_" not in display:
        game_over = True
        print("you win")
    print(stages[lives])