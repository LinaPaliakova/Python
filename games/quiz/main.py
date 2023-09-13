from art import logo
from questions import questions
import os


def clear():
  os.system("clear")

def greet_user():
    print(logo)
    print("There are a total of 6 questions, you can skip a question anytime by typing 'skip'")
    input("Press any key to get started...")
    return True 

def check_answer(question, answer, attempt, current_player):
    clear()
    if answer.lower() == questions[key]["answer"].lower():
       print(f"Correct Answer! \n{current_player}'s score is {player_score[current_player]}!"
      )
       return True 
    else:
       print(f"Wrong Answer :( \nYou have {attempt} left! \nTry again...")
       return False
  
def print_dictionary():
    for question_id, ques_answer in questions.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])

def print_winner(player1, player2): 
    if player_score[player1] > player_score[player2]:
        print(f"{player1} WON! The score is {player_score[player1]}")
    elif player_score[player1] < player_score[player2]:
        print(f"{player2} WON! The score is {player_score[player2]}")
    else:
        print("It's DRAW!")

greetings = greet_user()
players_list = input("Enter 2 Players with Space: ").split(" ")
current_player = players_list[0]
print(current_player)
player_score = dict.fromkeys(players_list, 0)

for key in questions.keys():
  print("------------------------------")
  print(f"It is {current_player}'s turn.")
  attempt = 2
  while attempt > 0:
    print(questions[key]["question"])
    answer = input("Enter Answer (To move to the next question, type 'skip') : ")
    if answer == "skip":
            break
    check = check_answer(questions, answer, attempt, current_player)
    if check:
            player_score[current_player] += 1
            break
    attempt -= 1
    
    

  if players_list.index(current_player) == 0:
    current_player = players_list[1]
  else:
    current_player = players_list[0]


print_winner(players_list[0], players_list[1])

question_answers = input("Want to know the correct answers? (Y/N): ")
if question_answers == 'Y':
   print_dictionary()
print("Thanks for playing!")
