# start your program with exercise 4-1, copy list of pizza, called in friend_pizzas
my_favorite_pizzas = ['enak','enak_aja', 'enak_banget']

friend_pizzas = my_favorite_pizzas[:]

#add a new pizza to the original list 
my_favorite_pizzas.append('tidak enak')

#add different pizza to the list friend_pizzas
friend_pizzas.append('biasa aja')

# prove that you have separated lists. 
print(my_favorite_pizzas)
print(friend_pizzas)

# Print the message "My favorite pizzas are"
print("My favorite pizza are ")

#then use a for loop to print the first list
for my_pizza in my_favorite_pizzas:
    print(my_pizza)

#Print the message "My friends's favorite pizzas are"
print("My friend's favorite pizzas are ")

#Then use a for loop to print the second list
for my_friend_pizza in friend_pizzas:
    print(my_friend_pizza)