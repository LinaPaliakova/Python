import random

while True:
    choice = input("Enter a choice (rock, paper, scissors): ")
    
    game_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(game_list)
    print(f"You chose {choice}, computer chose {computer_choice}.")
    if choice == computer_choice:
        print(f"Both players selected {choice}. It's a tie!")
    elif choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
   
    play_again = input("Play again (Y/N)? ")
    if play_again == "N":
      break  
