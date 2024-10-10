#Write a series of conditional tests.
#Print a statement describing each test and your predictions for the result of each test.
#Your code should look something like this
#-------------------------------------------
'''
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi' ? I predict False")
print(car == 'audi')
'''

# Look closely at your result and make sure you understand why each line evaluate to True or False
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("Is car 'audi'? I predict False")
print(car=='audi')

#Create at least 10 test. Have at least 5 tests evaluate to True and another 5 tests evaluate to False

number = 15 
print(f"the number is {number}")
print("Is the number > 10? I predict True")
print(number>10)
print("Is the number < 10? I predict False ")
print(number<10)

color = 'red'
print(f"the color is {color}")
print("Is the color == blue? I predict False")
print(color=='blue')
print("Is the color == red? I predict True")
print(color=='red')

foods = ['martabak', 'sate ayam', 'lele goreng']
print("Is the 'martabak' in the foods? I predict True")
print("martabak" in foods)
print("Is 'gulai kambing' in foods? I predict False")
print("gulai kambing" in foods)

string = 'hello'
print("Is len(string) == 5? I predict True")
print(len(string)==5)
print("Is len(string) == 4? I predict False")
print(len(string)==4)