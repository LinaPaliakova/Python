try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except ValueError:
  print("Error, please enter numeric input for Rate")
  quit()
else:  
    pay = round(hours * rate, 2)
    overpay = round(40 * rate + (hours - 40)  * rate * 1.5, 2)


    if hours <= 40:
       print(f"Pay: {pay}")
    else:
       print(f"Pay: {overpay}")
