#Write a program that polls users about their dream vacation. 
# Write a prompt similar to "If you could visit one place in the world, where would you go?" 
# Include a block of code that prints the results of the poll.
 
responses = []

polling = True

while polling:
    response = input("If you could visit one place, where would you go? ")
    if response.lower() == 'quit':
        break
    else:
        responses.append(response)

for response in responses:
    print(f"I will visit {response.title()}")