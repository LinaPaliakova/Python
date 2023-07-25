def compute_pay(hours,rate):
    pay = round(hours * rate, 2)
    overpay = round(40 * rate + (hours - 40)  * rate * 1.5, 2)
    if hours <= 40:
       return f"Pay: {pay}"
    else:
       return f"Pay: {overpay}"


def check_value(p_input):
    try:
        val = float(p_input)
        return val
    except ValueError:
        print("Error, please enter numeric input for Rate")
        quit()
    


hours = input("Enter Hours: ")
hours = check_value(hours)
rate = input("Enter Hours: ")
rate = check_value(rate)

print(compute_pay(hours,rate)) 
