def check_numbers():
        count_of_numbers = 0
        summa = 0
        
        while True:
            p_number = input("Enter a number: ")
            
            try:
                number = float(p_number)
                count_of_numbers += 1
                summa += number
            except ValueError:
                if p_number == "done":
                    print(summa, count_of_numbers, summa / count_of_numbers)
                    break 
                print('Error, please enter numeric input' )
                continue
               
                
            

check_numbers()

#version 2

def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False
        
empty_list = list()

while True:
    input_number = input("Enter a number: ")
    if input_number == "done":
        break
    
    number = check_for_float(input_number)
    
    
    if not number:
        continue
    
    empty_list.append(number)
    max_value = max(empty_list)
    min_value = min(empty_list)
    
print(f"Maximum number: {max_value}, Minimum number: {min_value}")
