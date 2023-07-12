temp = int(input("Enter a temperature: "))

def measure_tem(temp):
  if temp > 28:
    return "Hot"
  elif 18 <= temp <= 28:
    return "Warm"
  else:
     return "Cold"

print(measure_tem(temp))
