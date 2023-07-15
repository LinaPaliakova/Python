for i in range(1,101):
  if i % 5 == 0:
    print("Fizz")
  elif i % 7 == 0:
    print("Buzz")
  elif i % 7 == 0 and i % 5 == 0:
    print("FizzBuzz")
  else:
    print(i)
