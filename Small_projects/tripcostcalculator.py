print("Welcome to the Trip Cost Calculator!")
days = int(input("How many days will you stay? "))
hotel_cost = float(input("How much does hotel cost per night? $"))
flight_cost = float(input("How much does flight cost? $"))
car_price = float(input("If you need rental car please enter the price otherwise enter zero. $"))
other_expen = float(input("Enter other possible expenses $"))
total = hotel_cost * days + flight_cost + car_price * days + other_expen
print(f"Total Cost: ${total}")
