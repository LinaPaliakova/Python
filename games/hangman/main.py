import random
from logo_stages import hangman_stages, logo
from hangman_words import word_list
import os

def clear():
  os.system("clear")
print(logo)

secret_word = random.choice(word_list)
blanks = []

for _ in range(len(secret_word)):
    blanks.append("_")

end_game = False
guessed_letters = []
lives = 6
while not end_game:
    guess = input("Guess a letter:").upper()
    clear()
    all_indexes = []
       
    if guess in guessed_letters:
         print("You have already guessed this letter!")
         continue
    else:   
         guessed_letters.append(guess)

    if guess not in secret_word:
       lives = lives - 1
         
    
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            all_indexes.append(i)
     

    for i in all_indexes:
        blanks[i] = guess

    print(' '.join(blanks))
    print(hangman_stages[lives])      
    if "_" not in blanks:
       end_game = True
       
    if lives == 0:
       end_game = True
       print("You lose")
       

    if end_game == True:
        ask = input("Do you want to play again? (Y/N)")
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            blanks = []
            for _ in range(len(secret_word)):
                blanks.append("_")
            end_game = False
            guessed_letters.clear()
            lives = 6
        else:
            print("See you next time!")
            break
