import random
lower_bound = int(input("Enter Lower bound: "))
upper_bound = int(input("Enter Upper bound: "))
tries = 0
number = random.randint(lower_bound,upper_bound)
print()
print(f"{chr(0x20)*5}You've only  3  chances to guess the integer!")
print()
while True:
  guess = int(input("Guess a number: "))
  tries += 1
  if guess < number:
    print("You guessed too small!")
  elif guess > number:
    print("You Guessed too high!")
  else:
    print(f"Congratulations you did it in  {tries}  try")
    break
  if tries == 3:
     print()
     print(f"The number is {number}")
     print(f"{chr(0x20)*5}Better Luck Next time!")
     break   
