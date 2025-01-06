from pathlib import Path

contents = ['persian cat', 'american shorthair', 'burmesse cat']
path = Path("cats.txt")
file_string = ''
for content in contents:
    file_string += f"{content}\n"
path.write_text(file_string)

content = path.read_text()
lines = content.splitlines()
print("Name of cats:")
for line in lines:
    print(f"-{line}")
contents2 = ['siberian husky', 'poodle', 'chihuahua']
path2 = Path("dogs.txt")
file_string2 = ''
for content2 in contents2:
    file_string2 += f"{content2}\n"
path2.write_text(file_string2)
content2 = path.read_text()
lines2 = content2.splitlines()
print("Name of dogs:")
for line2 in lines2:
    print(f"-{line2}")

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

#lines = contents.splitlines()
#for line in lines:
#    print(line)

for line in contents.splitlines():
    print(line)

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
#lines = contents.splitlines()
#for line in lines:
#    pi_string += line.lstrip()
for line in contents.splitlines():
    pi_string += line.lstrip()
print(f"{pi_string[:53]}...")
print(len(pi_string))


from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

from pathlib import Path

content = input("What is your name? ")
path = Path('guest.txt')
path.write_text(content)

from pathlib import Path

guest_name = []
while True:
    content = input("What is your name? 'quit' to exit ")
    if content == 'quit':
        break
    print(f"We will add {content} to the guest book")
    guest_name.append(content)

file_string = ''
for content in guest_name:
    file_string += f"{content}\n"

path = Path('guest_book.txt')
path.write_text(file_string)


from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(f"Reading file : {filename}")
    path = Path(filename)
    try:
        content = path.read_text()
    except FileNotFoundError:
        print(f"The {path} is missing")
    else:
        print(content)

from pathlib import Path
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(f"Reading file : {filename}")
    path = Path(filename)
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(content)

from pathlib import Path

path = Path("gutenberg.txt")

try:
    contents = path.read_text(encoding='utf-8')

except FileNotFoundError:
    print(f"Sorry, the {path} does not exist")

else:
    #Count -the- in the text
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has {num_words} words.")
    the_words = contents.lower().count('the ')
    print(f"How much 'the' in {path}? {the_words}")

from pathlib import Path
import json

number = input("What is your favorite number? ")

path = Path('numbers.json')
contents = json.dumps(number)
path.write_text(contents)

print(f"I know your favorite number is {number}")

from pathlib import Path
import json

def get_stored_username(path):
    '''Get stored username if available'''
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
def get_new_username(path):
    '''Prompt for a new username'''
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
def greet_user():
    '''Greet user'''
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}")
        else:
            username = get_new_username(path)
            print(f"We'll remember you dear {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you dear {username}")
greet_user()

'''
def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    #   Prompt for a new username.
    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")
'''
