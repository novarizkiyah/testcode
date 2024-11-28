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

class Battery:
    '''A simple attempt to model a battery for an electic car'''
    def __init__(self, battery_size = 40):
        '''Initialize the battery's attributes'''
        self.battery_size = battery_size
    def describe_battery(self):
        '''Print statement describing the battery size'''
        print(f"This car has a {self.battery_size}-kWh battery")
    def get_range(self):
        '''Print information about range battery'''
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge. ")
    def upgrade_battery(self):
        '''Check battery size capacity'''
        if self.battery_size == 40:
            self.battery_size = 65
            print("Upgrade battery 65 kWh")
        elif self.battery_size == 65:
            print("The battery already upgrade")


class ElecticCar(Car):
    '''Represent aspect of a car, specific to electric vehicles'''
    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class'''
        super().__init__(make, model, year)
        '''Then initialize attributes to an electric car'''
        self.battery = Battery()

    def fill_gas_tack(self):
        '''Electric cars don't have gas tanks'''
        print("This car doesn't have a gas tank")


my_leaf = ElecticCar('Nissan', 'leaf', 2024)
print(my_leaf.get_describe_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tack()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()