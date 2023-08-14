from ascii_art import logo
import os

def clear():
  os.system("clear")

print(logo)

all_bids = {}

while True:
  name = input("Please enter a name: ")
  bid = int(input("Please enter your bid $"))
  answer = input("Are there any other bidder? ")
  all_bids[name] = bid
  if answer == "Y":
      clear()
  else:
      max_bidder = max(all_bids, key=all_bids.get)
      print(f"The winner is {max_bidder} with a bid of $", max(all_bids.values()))
      break
  
