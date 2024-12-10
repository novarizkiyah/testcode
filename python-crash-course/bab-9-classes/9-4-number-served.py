# Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, 
# and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.

# Add a method called increment_number_served() 
# that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in a day of business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Name : {self.restaurant_name}")
        print(f"Type : {self.cuisine_type}")
    def open_restaurant(self):
        print(f"This {self.restaurant_name} is open")
    def set_method_served(self, number):
        self.number_served = number
    def increment_number_served(self, increment_number):
        self.number_served += increment_number

restaurant = Restaurant("Praboemoelih", "Indonesian cuisine")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

#Print the number of customers the restaurant has served,
print(f"Restaurant has served : {restaurant.number_served}")

#change this value and print it again.
restaurant.number_served = 15
print(f"Restaurant has served : {restaurant.number_served} at this moment")

# Calling the method set_number_served()
restaurant.set_method_served(30)
print(f"Restaurant has served : {restaurant.number_served} at this moment")

# Calling increment_number_served()
restaurant.increment_number_served(1000)
print(f"Restaurant has served : {restaurant.number_served} at this moment")

restaurant.describe_restaurant()
restaurant.open_restaurant()
