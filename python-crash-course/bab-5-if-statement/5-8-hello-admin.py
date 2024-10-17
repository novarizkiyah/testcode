# Make a list of five or more usernames, including the name 'admin'
# Imagine you are writing the code that will print a greeting to each user after they log in to a web.
# Loop through the list, and print a greeting to each user

# 1. If the username is 'admin', print a special greeting, such as : Hello admin, would you like to see a status report.
# 2. Print a generic greeting, such as Hello Jardem thank you for logging in again 


lists = ["nova", "rizkiyah", "admin", "mulyono", "fufufafa"]



for list in lists:
    if list == "admin":
        print("Hello Admin, would you like to see a status?")
    else:
        print(f"Hello, {list.title()} thank you for logging again")