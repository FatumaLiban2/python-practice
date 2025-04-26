def reverse_string(s):
    reversed_str= "" #starting with an empty string
    for char in s:
        reversed_str= char + reversed_str
    return reversed_str
#getting input from the user
user_input= input("Enter a string to reverse: ")
result = reverse_string(user_input)
print("Reversed String:", result)
   