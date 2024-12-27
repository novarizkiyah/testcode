# The final listing for remember_me.py assumes 
# either that the user has already entered their username 
# or that the program is running for the first time. 
# We should modify it in case the current user is not the person 
# who last used the program.

# Before printing a welcome back message in greet_user(), 
# ask the user if this is the correct username. 
# If it's not, call get_new_username() to get the correct username.

from pathlib import Path
import json

def get_stored_user_info(path):
    '''Get stored username if available'''
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def get_new_user_info(path):
    '''Prompt for a new username'''
    username = input("What is your name? ")
    email = input("What is your email name? ")
    password = input("What is your password? ")

    user_dict = {
        'username' : username,
        'email' : email,
        'password' : password
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict
def greet_user():
    '''Greet user'''
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}")
        print(f"This is your email : {user_dict['email']}")
        print(f"Your password : {user_dict['password']}")
    else:
        user_dict = get_new_user_info(path)
        print(f"We'll remember you dear {user_dict['username']}")
greet_user()

