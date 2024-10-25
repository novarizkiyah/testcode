#A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; 
# if they are between 3 and 12, the ticket is $10; 
# and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tel them the cost of their movie ticket.

number = int(input("How old are you? "))

while True:
    if 0<number<=3:
        print("the ticket is free")
    elif 3 < number < 12:
        print("the ticket is $10")
    else:
        print("the ticket is $15")
    break