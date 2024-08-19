print("What's your name?")
name = input()
print("How old are you?")
age = int(input())

if name == 'Alice':
    print("Hi, Alice")
#This code is right, if name input is True then if age will execute 
if age < 12:
    print("You're not Alice, kiddo")
elif age > 100:
    print("You are not Alice, grannie")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire")