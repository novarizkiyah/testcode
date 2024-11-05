# Start with a copy of user_profile.py from page 148
# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you

def build_profile(first, last, **user_info):
    ''' Build a dictionary containing everything about the user'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('nova', 'rizkiyah',
                             location = 'rotterdam',
                             field = 'physics',
                             favorite_food = 'martabak')
print(user_profile)