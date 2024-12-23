# One common problem when prompting for numerical input occurs 
# when people provide text instead of numbers. 
# When you try to convert the input to an int, you'll get a ValueError. 
# Write a program that prompts for two numbers. 
# Add them together and print the result. 
# Catch the ValueError if either input value is not a number, 
# and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text 
# instead of a number.



while True:
    print("\n Give me 2 numbers")
    print("\n Enter q to quit")
    first_number = input("\n Your first number: ")
    if first_number == 'q':
        break
    second_number = input("\n Your second number: ")
    if second_number == 'q':
        break
    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print("\n You must input number!")
    else:
        print(f"\n sum : {sum}")
