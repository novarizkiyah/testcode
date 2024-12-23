# Wrap your code from Exercise 10-6 in a while loop 
# so the user can continue entering numbers 
# even if they make a mistake and enter text instead of a number.

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