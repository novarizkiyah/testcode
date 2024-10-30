# Write different version excercise 7-5 that do following at least once:

# use a conditional test in while statement to stop the loop

# use an active variable to control flow how long the loop runs

# use break statement to exit the loop when the user enter a 'quit' value

active = True

while active:
    user_input = input("How old are you?, write 'quit' to exit ")
    if user_input.lower() == 'quit':
        active = False
        print("Thank you for using this code")
        break
    try:
        number = int(user_input)
        if 0 < number <= 3:
            print("The ticket is free")
        elif 3 < number <= 12:
            print("the ticket is $10")
        else:
            print("the ticket is $15")
    except ValueError:
        print("Please enter a valid response, like number or 'quit'")



