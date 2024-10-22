#Use the code in favorite_languages.py (page 104).

'''
1. Make a list of people who should take the favorite languages poll. 
Include some names that are already in the dictionary and some that are not.

2. Loop through the list of people who should take the poll. 
If they have already taken the poll, print a message thanking them for responding. 
If they have not yet taken the poll, print a message inviting them to take the poll.
'''    

favorite_language = {
    'sarah' : 'c',
    'nova' : 'python',
    'aya' : 'go',
    'mahdi' : 'pascal',
    'ramanujan' : 'java'
}

friends = ['sarah', 'ramanujan']

for name, language in favorite_language.items():
    if name in friends:
        print(f"Hi, {name.title()}, thank you for taking the poll")
    else:
        print(f"{name.title()}, please taking the poll")