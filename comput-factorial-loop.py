# compute factorial using for loop
#non negative integer

def factorial(n):
    result=1
    while n>1:
      result= result*n
      n=n-1
    return result

number= int(input("Enter a positive integer: "))
#checking if the input is valid 

if number<0:
   print("Factorial not for negative numbers ")
else:
   print("Factorial of" , number,"is", factorial(number))