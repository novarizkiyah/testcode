#Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = int(input("Guess your number! "))

if number % 10 == 0 and number != 0 :
    print("The number is multiple of 10")
else:
    print("the number is not multiple of 10")