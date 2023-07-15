import random

while True:
  number1 = random.randint(1,6)
  number2 = random.randint(1,6)
  print(f"Dice1: {number1}")
  print(f"Dice2: {number2}")
  answer = input("Roll the dice again? (Y/N) ")
  if answer == "N":
    break
