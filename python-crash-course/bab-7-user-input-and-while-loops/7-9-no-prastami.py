#Using the list sandwich_orders from Exercise 7-8, 
# make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandiches.

sandwich_orders = ['lamb', 'prastami', 'prastami', 'beef', 'prastami', 'chicken', 'egg']

print("The Deli has run out of prastami")

while 'prastami' in sandwich_orders:
    sandwich_orders.remove('prastami')

print(sandwich_orders)
for sandwich_order in sandwich_orders:
    print(f"I just only have {sandwich_order}")