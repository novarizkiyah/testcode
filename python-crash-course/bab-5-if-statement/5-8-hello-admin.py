# Make a list of five or more usernames, including the name 'admin'
# Imagine you are writing the code that will print a greeting to each user after they log in to a web.
# Loop through the list, and print a greeting to each user

# 1. If the username is 'admin', print a special greeting, such as : Hello admin, would you like to see a status report.
# 2. Print a generic greeting, such as Hello Jardem thank you for logging in again 

usernames = ["admin", "nova", "aryya", "aya", "yusyril"]

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report")
    else:
        print(f"Hello {username.title()} thank you for logging in again")

