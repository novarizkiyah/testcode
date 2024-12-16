# Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list 
# and print a message saying that any ticket matching these 4 numbers 
# or letters wins a prize

from random import choice

num_let = [1,2,3,4,5,6,7,8,9,10, 'z', 'y', 'x', 'v', 'w']
winning_ticket = []
print("Who's the winners?")

while len(winning_ticket) < 4:
    pulled_item = choice(num_let)

    if pulled_item not in winning_ticket:
        print(f"We pulled : {pulled_item}")
        winning_ticket.append(pulled_item)

print(f"The winner is {winning_ticket}")