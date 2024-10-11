# Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, then

# 1. If the person is less than 2 years old, print a message that the person is a baby

# 2. If the person is more than 2 years old but less than 4, print a message that the person is a toddler

# 3. If the person is more than 4 years old but less than 13, print a message that the person is a kid

# 4. If the person is more than 13 years old but less than 20, print a message that the person is a teenager

# 4. If the person is more than 20 years old but less than 65, print a message that the person is an adult

# 5. If the person is more than 65, print a message that the person is an elder

print("How old your age?")
age = int(input())

if age<=2:
    print("this is a baby")
elif age>2 and age<=4:
    print("this is a toddler") 
elif 4<age<=13:
    print("this is a kid")
elif 13<age<=20:
    print("this is a teenager")
elif 20<age<=65:
    print("this is an adult")
else:
    print("this is an elder")


