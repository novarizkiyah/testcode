#An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 
# (page 166) or Exercise 9-4 (page 171). Either version of the class will work; 
# just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays theese flavors. 
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors
    def describe_restaurant(self):
        info = f"{self.restaurant_name}, {self.cuisine_type}"
        return info.title()

restaurant = Restaurant('Selera Jawa', 'Java')
print(restaurant.describe_restaurant())

class IceCreamStand(Restaurant):
    def __init__(self, flavors):
        super.__init__(flavors)

