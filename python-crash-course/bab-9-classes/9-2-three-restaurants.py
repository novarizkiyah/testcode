#Start with your class from Exercise 9-1. 
# Create three different instances from the class, 
# and call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Name Restaurant : {self.restaurant_name}")
        print(f"Type cuisine : {self.cuisine_type}")
    def open_restaurant(self):
        print(f"My {self.restaurant_name} is open")

restaurant = Restaurant("Praboemoelih", "Traditional Indonesia")
restaurant2 = Restaurant("Indian culinary", "Indian")
restaurant3 = Restaurant("Malaysian food", "Malaysian")

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()