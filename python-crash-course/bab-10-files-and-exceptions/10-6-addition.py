# One common problem when prompting for numerical input occurs 
# when people provide text instead of numbers. 
# When you try to convert the input to an int, you'll get a ValueError. 
# Write a program that prompts for two numbers. 
# Add them together and print the result. 
# Catch the ValueError if either input value is not a number, 
# and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text 
# instead of a number.


print("Please input 2 numbers")
number_one = input("What is your number one? ")
number_two = input("What is your second number? ")

try: 
    sum = int(number_one)+ int(number_two)
except ValueError:
    print("Please input numbers!")
else:
    print(f"The addition is : {sum}")

