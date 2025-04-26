def factorial_recursive(n):
#0! and 1! is 1;
    if n == 0 or n == 1:
     return 1
    else:
       return n* factorial_recursive(n-1)
    
number = int(input("Enter a positive integer: "))

if number<0:
 print("Factorial is not defined for negative numbers:")
 
else:
 print("Factorial of", number, "is", factorial_recursive(number))
