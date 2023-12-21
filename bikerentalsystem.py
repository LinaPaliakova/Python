#OOP Python practice
import datetime

class BikeRental:
  def __init__(self, stock=0):
    self.stock = stock

  def display_stock(self):
    """Display bikes currently available on the system"""
    print(f"{self.stock}") 
    return self.stock

  def rent_bike_on_hourly_basis(self, number_of_bikes):
    """Display  rent of bikes prices for hour basis """
    
    self.number_of_bikes = number_of_bikes
    if self.number_of_bikes < 0:
        print("Number of bikes should be positive number")
        return None
    elif self.number_of_bikes > self.stock:
        print(f"We have only {self.stock}")
        return None
    else:  
        now = datetime.datetime.now()
        print(f"you have rented your bike at {now.hour}, {now.minute}")
        self.stock = self.stock - self.number_of_bikes
        print(f"{self.stock}")
        return now


  def rent_bike_on_daily_basis(self, number_of_bikes):
    """Display  rent of bikes prices for daily basis """
    
    self.number_of_bikes = number_of_bikes
    if self.number_of_bikes < 0:
        print("Number of bikes should be positive number")
        return None
    elif self.number_of_bikes > self.stock:
        print(f"We have only {self.stock}")
        return None
    else:  
        now = datetime.date.today()
        print(f"you have rented your bike at {now}")
        self.stock = self.stock - self.number_of_bikes
        return now

  def rent_bike_on_weekly_basis(self, number_of_bikes):
    """Display  rent of bikes prices for weekly basis """
    
    self.number_of_bikes = number_of_bikes
    if self.number_of_bikes < 0:
        print("Number of bikes should be positive number")
        return None
    elif self.number_of_bikes > self.stock:
        print(f"We have only {self.stock}")
        return None
    else:  
        now = datetime.date.today()
        till = datetime.date.today() + datetime.timedelta(days=7)
        print(f"you have rented your bike at {now} till {till}")
        self.stock = self.stock - self.number_of_bikes
        return now, till
  
  def return_bikes(self, request):
    """Method to return bikes """
    rental_time, rental_basis, number_of_bikes = request
    bill = 0
    if rental_time and rental_basis and number_of_bikes:
        self.stock += number_of_bikes
        now = datetime.datetime.now()
        rental_period = now - rental_time
        if rental_basis == 1:
           bill = round(rental_period.seconds / 3600) * 5 * number_of_bikes  #5$ - is price for hourly basis
        elif rental_basis == 2:
           bill = round(rental_period.days) * 20 * number_of_bikes #20$ - is price for daily basis
        elif rental_basis == 3:
           bill = round(rental_period.days / 7) * 60 * number_of_bikes #60 - is weekly rent
        if 3 <= number_of_bikes  <= 6: #discount for families
           bill = bill * 0.7
        print("Hope you enjoyed our time")           
        print(f"Your bill is {bill}")   
        return bill
    else:
       print("Are you sure that you have rented bile with us") 
       return None

class Customer:
  def __init__(self):
    self.bikes = 0
    self.rental_basis = 0
    self.rental_time = 0
    self.bill = 0
  def request_bike(self):
      bikes = int(input("Enter a number of bikes you would like to rent"))
      self.bikes = bikes
      return self.bikes
  def return_bike(self):
    if self.rental_time and self.rental_basis and self.bikes > 0:
        return self.rental_time, self.rental_basis, self.bikes
    else:
        return 0, 0, 0
    
bikesystem = BikeRental(100)
customer1 = Customer()
while True:
   print("=====    Bike rental APP     =====")
   print()
   options = ["1. Display available bikes",
            "2. Request a bike on hourle basis",
            "3. Request a bike on a daily basis",
            "4. Request on weekly basis",
            "5. Return a bike",
            "6. Exit"]
   print(*options, sep='\n')

   user_input = input("Please enter your choice")
   try:
       user_input = int(user_input)
   except ValueError:
       print(" You must enter a number")   
       continue
   if user_input == 1:
      bikesystem.display_stock()
   elif user_input == 2:
      requested_bikes = customer1.request_bike()
      rental_time = bikesystem.rent_bike_on_hourly_basis(requested_bikes)
      customer1.rental_time = rental_time
      customer1.rental_basis = 2
   elif  user_input == 3:
      rental_time = bikesystem.rent_bike_on_daily_basis(customer1.request_bike())
      customer1.rental_time = rental_time 
      customer1.rental_basis = 3
   elif user_input == 4:
      rental_time = bikesystem.rent_bike_on_weekly_basis(customer1.request_bike())
      customer1.rental_time = rental_time
      customer1.rental_basis = 4
   elif user_input == 5:
      request = customer1.return_bike()
      bill =  bikesystem.return_bikes(request)
      customer_bill = bill
      customer1.rental_basis, customer1.rental_time, customer1.bikes = 0, 0, 0
   elif user_input == 6:
       break  
   print("Thank you")        
