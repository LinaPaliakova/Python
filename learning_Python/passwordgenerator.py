import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"
letters_num = int(input("How many letters do you want in your password? "))
numbers_num = int(input("How many numbers do you want in your password? "))
symbols_num = int(input("How many symbols do you want in your password? "))

password = random.sample(letters, letters_num) + random.sample(nums, numbers_num) + random.sample(symbols, symbols_num)
random.shuffle(password)
print("Your password is: ",''.join(password))
