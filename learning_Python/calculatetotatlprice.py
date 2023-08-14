available_parts = {1: "computer", 2: "monitor", 3: "keyboard", 4: "mouse", 5: "hdmi cable", 6: "dvd drive", 0: "to finish"}

price_quantity = {
  "computer" : { "price" : 500,
                 "quantity": 10
              },
    "monitor" : { "price" : 200,
                "quantity" : 8
              },
  "keyboard" : {
                 "price": 500,
                 "quantity": 5
    },
  "mouse" : {
                 "price": 10,
                 "quantity": 0
    },
  "hdmi cable" : {
                 "price": 20,
                 "quantity": 7
    },
  "dvd drive" : {
                 "price": 50,
                 "quantity": 5
    }
     
}

print("Please add options from the list")
for key, value in available_parts.items():
    print(key, ':', value)

total_price = 0

while True:
    choice = int(input())
    for key, value in available_parts.items():
        if key == choice:
            choice_value = value  


    for key, value in price_quantity.items():
        if choice_value == key and price_quantity[key]["quantity"] > 0:
            total_price += price_quantity[key]["price"]
            price_quantity[key]["quantity"] -=1
            print("Adding", key)
        if choice_value == key and price_quantity[key]["quantity"] == 0: 
            print(key, "is out of stock")
    if choice == 0:
      print("Total price:", total_price)
      break
  
