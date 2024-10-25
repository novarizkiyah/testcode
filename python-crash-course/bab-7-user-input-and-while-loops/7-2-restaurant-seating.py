#Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

message = input("How many people in dinner group? ")
number = int(message)

if number > 8:
    print("You have to wait")
else:
    print("the table is ready")