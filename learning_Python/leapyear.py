def leap_year(p_year):
    
    if p_year % 4 == 0:
        if p_year % 100 == 0:
             if p_year % 400 == 0:
                 return "Leap year."
             else:  
                 return "Not Leap year."
        else:    
           return "Leap year."
    else:
       return "Not a leap year."

year = int(input("Enter a year: "))
print(leap_year(year))
