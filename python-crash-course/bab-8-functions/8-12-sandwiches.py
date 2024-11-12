#Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandiwch that is being ordered. 
# Call the function three times, using a different number of arguments each time.


def sandwiches(*items):
    for item in items:
        print(item)

sandwiches("sandwiches A", "sandwiches B")
sandwiches("sandwiches C")
sandwiches("sandwiches D", "sandwiches C", "sandwiches E")