#Try more comparisons, write more test
#have at least one True and one False result for each of the following:

#Test for equaliy and inequality with strings
car = 'BMW'
print("Is your car 'BMW'?")
print(car == 'BMW')
print("Is your car 'bmw'?")
print(car=='bmw')

print("Is not your car 'bmw'?")
print(car !='bmw')
print("Is not your car 'BMW'")
print(car != 'BMW')

#Test using lower() method

print("is the car is lower?")
print(car.lower()=='bmw')
print("is the car is lower?")
print(car.lower()=='BMW')

#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to and less than or equal to
number = 18
print("the number is 18, is the number is less than 20?")
print(number<20)
print("the number is 18, is the number is greater than 20?")
print(number>20)
print("Is the number 18?")
print(number==18)
print("Is not the number 18?")
print(number!=18)
print("Is 18 greater than or equal to 17?")
print(number>=17)
print("Is 18 is less than equal to 17?")
print(number<=17)

#Test using the 'and' keyword and the 'or keyword
age_1 = 30
age_2 = 40
print("so the age_1 is 30 and age_2 is 40")
print(age_1>=age_2 or age_1<=age_2)
print(age_1>=age_2 and age_1<=age_2)

#Test whether an item is in a list
dier = ["domba", "babi", "sapi"]
print('lele' in dier)
print('babi' in dier)

#Test whether an item is not in a list
if 'lele' not in dier:
    print("Sorry, Ik heb geen lele")