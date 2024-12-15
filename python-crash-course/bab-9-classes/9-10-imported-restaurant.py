# Using your latest Restaurant class, store it in a module. 
# Make a separate file that imports Restaurant. 
# Make a Restaurant instance, and call one of Restaurant’s methods 
# to show that the import statement is working properly.

# restaurant.py:

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
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    def show_flavors(self):
        print("Our Ice Cream : ")
        for flavor in self.flavors:
            print(f"- {flavor}")

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

icecream = IceCreamStand("Es Krim")
icecream.flavors = ['Strawberry', 'Chocolate', 'Vanilla']
icecream.show_flavors()