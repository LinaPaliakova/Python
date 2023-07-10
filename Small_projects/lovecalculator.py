print("Welcome to Love calculator!")
name1 = input("Enter a name: ")
name2 = input("Enter a name: ")
word1 = "true"
word = "love"
common_name = name1 + name2
total1 = 0
total2 = 0
for i in word1:
  total1 += common_name.count(i)

for i in word:
  total2 += common_name.count(i)
 
  
love_score = int(str(total1) +  str(total2))
print(love_score)
if love_score < 10 or love_score > 85:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score > 70:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
