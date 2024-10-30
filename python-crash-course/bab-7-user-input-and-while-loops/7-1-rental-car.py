#Write a program that asks the user what kind of rental car they would like. 
# Print a message about that car, such as “Let me see if I can find you a Subaru”.

message = input("What kind of car do you want to rent?")
print(f"Let me see if I can find you a {message.title()}")