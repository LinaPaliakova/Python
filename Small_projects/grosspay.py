hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = round(hours * rate, 2)
overpay = round(40 * rate + (hours - 40)  * rate * 1.5, 2)


if hours <= 40:
   print(f"Pay: {pay}")
else:
   print(f"Pay: {overpay}")
  
