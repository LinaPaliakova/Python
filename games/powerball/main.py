#Step 1
from ascii_art import logo
import random
print(logo)

while True: 
    try:
        numbers = [int(i) for i in input("Enter 5 different numbers from 1 to 69, with spaces between each number. (For example: 5 17 23 42 50) \n").split(" ")]
    except ValueError:
        print("Please enter numbers, like 1,10 or 35")
        continue
    
    if len(numbers) != 5:
        print("Please enter 5 numbers. Separated by spaces.")
        continue
    between1_69 = True  
    for i in numbers:
        if  not (1 <=  i  <= 69):
            print("The numbers must be between 1 and 69")
            between1_69 = False
            break
    if not between1_69:
        continue
    
    if len(set(numbers)) != 5:
       print("Please enter 5 different numbers")
    break  
   

# Step 2 
while True:
    try:
      powerball_number = int(input("Enter the powerball number from 1 to 26.\n"))
    except ValueError:
        print("Please enter numbers, like 1,10 or 35")
        continue  
  
    if not  (1 <= powerball_number <= 26):
        print("The numbers must be between 1 and 26")
        continue
    break  

#Step 3
while True:
    try: 
        user_input3 = int(input("How many times do you want to play? (Max: 1000000)\n"))
    except ValueError:
        print("Please enter numbers, like 1,10 or 35")
        continue
    if not(1 <= user_input3 <= 1000000):
         print("You can play between 1 and 1000000")
         continue
    break  

#Step 4
cost_of_game = 2 * user_input3
print(f"It costs {cost_of_game}$ to play {user_input3} times, but don't worry. I'm sure you'll win it all back.")
input("Press Enter to start...")


for i in range(user_input3):
    winning_numbers = list(random.sample(range(1, 70), 5))
    win_powerball_number = random.randint(1,26)
    winning_num_str = ""
    for i in winning_numbers:
        winning_num_str += str(i) + " " 
    if set(winning_numbers) == set(numbers) and powerball_number ==  win_powerball_number:
          print( "The winning number are: ", winning_num_str, "and", str(win_powerball_number), "You have won the powerball lotery. Congratulations.")
          break
    else:
           print( "The winning number are: ", winning_num_str, "and", str(win_powerball_number), "You lost")
print(f"You have wasted ${cost_of_game}")
print("Thanks for playing!")




           
    
    
  
  


