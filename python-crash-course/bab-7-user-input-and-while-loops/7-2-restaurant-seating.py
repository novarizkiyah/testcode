#Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

number = int(input("How many people in your dinner group?"))

if number > 8:
    print("You have to wait")
else:
    print("the table is ready")