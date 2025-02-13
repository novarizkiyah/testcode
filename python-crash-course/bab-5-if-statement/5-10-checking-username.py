# Do the following to create a program that simulates how websites ensure that everyone has a unique username

# 1. Make a list of five or more usernames called current_users

# 2. Make another list of five username called new_users. Make sure one or two of the new usernames are also in the current_users list

# 3. Loop through the new_users list to see if each new username has already been used. 
# If it has, print a message that the person will need to enter a new username.
# If a username has not been used, print a message saying that the username is available.

# 4. Make sure your comparison is case insensitive. 
# If 'John' has been used, 'JOHN' should not be accepted.
# (To do this, you'll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ["John", "Sandy", "melk", "Mikael", "Abraham"]
convert_users = [user.lower() for user in current_users]

new_users = ["JOHN", "Merata", "Maharini", "SANDY", "Suci"]


for new_user in new_users:
    if new_user.lower() in convert_users:
        print(f"Hello {new_user}, pleased used another name")
    else:
        print(f"Username {new_user} still available")