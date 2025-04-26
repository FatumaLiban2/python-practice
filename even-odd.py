def even_or_odd(n):
    
    if n%2 ==0:
        return "Even"
    else:
        return "odd"
number=int(input("Enter a number: "))
#call the function with the user's number
result = even_or_odd(number) 
print("The number is: ", result)