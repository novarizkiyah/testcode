#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

message = ""
while message != 'quit':
    message = input("\nEnter pizza toping ? ")
    if message != 'quit':
        print(f"I'll add {message} to your pizza")


