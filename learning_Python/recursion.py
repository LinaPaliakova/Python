6. Write a Python program to get the sum of a non-negative integer.
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9

def sum_of_numbers(n):
  assert n >=0, 'Must be positive numbers'
  if len(str(n)) == 1 or len(str(n) == 0:
    return n
  else:
    return n%10 + sum_of_numbers(n // 10)

7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30


def sum_of_numbers(n):
  assert n >= 0, 'Must be positive numbers'
  if n == 0:
    return n
  else:
    return n + sum_of_numbers(n - 2)


1. Write a Python program to calculate the sum of a list of numbers.

def sum_of_list(list):
    if len(list) == 0:
      return 0
    elif len(list) == 1:
      return list[0]
    else:
      return list[0] + sum_of_list(list[1:])
      
      
3. Write a Python program to sum recursion lists.

def sum_of_lists(my_list):
    total = 0
    for i in my_list:
        if isinstance(i,list):
            total = total + sum_of_lists(i)
        else:
            total += i
    return total  

4. Write a Python program to get the factorial of a non-negative integer.

def get_factorial(n):
       assert n >= 0, 'Must be non-negative'  
       if n == 0 or n == 1:
           return 1
       else:
           return n * get_factorial((n-1))
            
print(get_factorial(5))  


            
print(sum_of_lists([1, 2, [3,4],[5,6]])) 

5. Write a Python program to solve the Fibonacci sequence using recursion.
def fibonacchi(n):
       assert n >= 0, 'Must be non-negative'  
       if n == 1 or n == 2:
           return 1
       else:
           return fibonacchi(n-1) + fibonacchi(n - 2)
            
print(fibonacchi(7))       

10. Write a Python program to calculate the value of 'a' to the power of 'b'.

def power(a, b):
       
       if b == 0 :
           return 1
       elif a == 0:
           return 0
       elif b == 1:
           return a
       else:
           return a *(power(a,b - 1))

2. Write a Python program to convert an integer to a string in any base.

def convert_to_string(n, base):
       
      string="0123456789ABCDEF"
      if n < base:
          return string[n]
      else:
          return convert_to_string(n // base, base) + string[n % base]

def harmonic_sum(n):
  
  if n < 2:
    return 1
  else:
    return 1 /n + harmonic_sum(n - 1)

print(harmonic_sum(7))            
            
def common_divisioner(a, b) :
    if  b == 0:
        return a
    else:
        return common_divisioner(b, a % b)

def geometric_sum(n):
  
  if n < 0:
    return 0
  else:
    return 1 / pow(2,n) + geometric_sum(n - 1)

Write a recursive function that accepts a decimal integer and display its binary equivalent.
def find( decimal_number ):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 *
                find(int(decimal_number // 2)))
 
# Driver Code
decimal_number = 10
print(find(decimal_number))

sum of natural numbers       
def sum_of_natural(n):
    
    if n == 0:
        return 0
    else:
       return n + sum_of_natural(n-1)

print(sum_of_natural(10))   

      







    




