# Add an if test to hello_admin.py to make sure the list of users is not empty

# 1. If the list is empty. print the message : We need to find some users!

# 2. Remove all of the usernames from your list and make sure the correct message is printed.

usernames = []

if usernames:
    for username in usernames:
            print(f"Adding {username}")
    print("Add admin")
else:
    print("We need find some users")
