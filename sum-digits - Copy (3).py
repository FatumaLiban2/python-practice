def sum_of_digits(n):
    #convering n into a string
    n= str(abs(n))
    total=0

    for digit in n:
        #converting it back to int
        total=total+int(digit)
    

    return total

user_number= int(input("Enter a number: "))
print("sum of the digits is: ", sum_of_digits(user_number))