# Wrap your code from Exercise 10-6 in a while loop 
# so the user can continue entering numbers 
# even if they make a mistake and enter text instead of a number.


while True:
    print("\n Please type 'quit' to exit")
    print("\n Please input 2 numbers")
    number_one = input("\n What is your number one? ")
    if number_one == 'quit':
        break
    number_two = input("\n What is your second number? ")
    if number_two == 'quit':
        break

    try: 
        sum = int(number_one)+ int(number_two)
    except ValueError:
        print("\n Please input numbers!")
    else:
        print(f"\n The addition is : {sum}")
