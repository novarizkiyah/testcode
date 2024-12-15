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

