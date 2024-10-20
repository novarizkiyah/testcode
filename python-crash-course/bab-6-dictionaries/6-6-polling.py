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

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

friends = ['nova', 'ramanujan']

for name in favorite_language.keys():
    if name in friends:
        print(f"Hello {name.title()}, thank you to get the pool")
    else:
        print(f"Hello {name.title()}, please take our pool")