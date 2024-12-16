# Make a class Die with one attribute called sides, 
# which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.

# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

'''
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
    
die6 = Die()
results = []
for x in range(10):
    result = die6.roll_die()
    results.append(result)
print(f"6 sides die results : {results}")
    
die10 = Die(sides=10)
results = []
for x in range(10):
    result = die10.roll_die()
    results.append(result)
print(f"10 sides die results : {results}")

die20 = Die(sides=20)
results = []
for x in range(10):
    result = die20.roll_die()
    results.append(result)
print(f"20 sides die results : {results}")

'''

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
    
def roll_and_prints(die, rolls, sides):
        results = [die.roll_die() for x in range(rolls)]
        print(f"10 times of {sides} sides die : ")
        print(results)
die6 = Die()
roll_and_prints(die6, 10, 6)

die10 = Die(sides=10)
roll_and_prints(die10, 10, 10)

die20 = Die(sides=20)
roll_and_prints(die20, 10, 20)