#Use the final version of electric_car.py from this section. 
# Add a method to the Battery class called upgrade_battery(). 
# This method should check the battery size and set the capacity to 85 if it isn’t already. 
# Make an electric car with a default battery size, call get_range() once, 
# and then call get_range() a second time after upgrading the battery. 
# You should see an increase in the car’s range.

class Car:
    '''Simple attempt to represent a car'''
    def __init__(self, make, model, year) :
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_describe_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    def read_odometer(self):
        '''Print a statement showing the car's mileage'''
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading'''
        self.odometer_reading += miles

class ElecticCar(Car):
    '''Represent aspect of a car, specific to electric vehicles'''
    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class'''
        super().__init__(make, model, year)
        '''Then initialize attributes to an electric car'''
        self.battery_size = 40

    def describe_battery(self):
        '''Print statement describing the battery size'''
        print(f"This car has a {self.battery_size}-kWh battery")


my_leaf = ElecticCar('Nissan', 'leaf', 2024)
print(my_leaf.get_describe_name())
my_leaf.describe_battery()