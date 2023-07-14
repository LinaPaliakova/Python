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
