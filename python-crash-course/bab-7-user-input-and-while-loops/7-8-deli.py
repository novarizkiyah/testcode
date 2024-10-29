#Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, 
# such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['sandwich A', 'sandwich B', 'sandwich C']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(sandwich_order)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made a {current_sandwich}")
    finished_sandwiches.append(current_sandwich)


print("List my sadwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


   