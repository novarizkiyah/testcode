# The remember_me.py example only stores one piece of information, 
# the username. 
# Expand this example by asking for two more pieces of information about 
# the user, 
# then store all the information you collect in a dictionary. 
# Write this dictionary to a file using json.dumps(), 
# and read it back in using json.loads(). 
# Print a summary showing exactly what your program remembers about 
# the user.

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

