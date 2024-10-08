# Think of five simple food and store them in a tuple
print("Using tuples: ")
foods = ("sate", "soto", "rawon", "nasi goreng", "bakwan")

# Use for loop to print each food
for food in foods:
    print(food)

#Try to modify one of the items, and make sure Python reject the change
#foods[1] = "mie goreng"

print("revised menu in tuples: ")
#The restaurant changes its menu, replacing two of the items with different foods.
foods = ("sate", "perkedel", "rujak", "nasi goreng", "bakwan")

#Add a line that rewrites the tuple and then use a for loop to print each food of the items on the revised menu
for food in foods:
    print(food)