#Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandiwch that is being ordered. 
# Call the function three tiems, using a different number of arguments each time.

def sandwiches(*items):
    print("List of items")
    for item in items:
        print(f"- {item}")

sandwiches('item 1', 'item 3', 'item 2')
sandwiches('item 4', 'item 2')
sandwiches('item 1', 'item 4')