print("What's your name ")
my_name = input()
print("What's your password")
password = input()
if my_name == "Nova":
    print("Hello Nova")
    if password == "123":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Hello " + my_name)
