#Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, 
# and then change this value and print it again.

#Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.

#Add a method called increment_number_served() 
# that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, 
# say, a day of business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, number):
        """Method to increment the number of customers served."""
        self.number_served += number

restaurant = Restaurant("Praboemoelih", "Traditional Indonesia")

# Print the number of customers the restaurant has served
print(f"Customers served initially: {restaurant.number_served}")

# Change the number of customers served and print again
restaurant.number_served = 50
print(f"Customers served after change: {restaurant.number_served}")

# Set the number of customers served using the method
restaurant.set_number_served(100)
print(f"Customers served after setting new number: {restaurant.number_served}")

# Increment the number of customers served using the method
restaurant.increment_number_served(30)
print(f"Customers served after increment: {restaurant.number_served}")
