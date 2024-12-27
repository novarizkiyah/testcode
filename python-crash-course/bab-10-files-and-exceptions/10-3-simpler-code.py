# The program file_reader.py in this section uses a temporary variable, lines, 
# to show how splitlines() works. You can skip the temporary variable 
# and loop directly over the list that splitlines() returns:
'''
for line in contents.splitlines():
'''
# Remove the temporary variable from each of the programs in this section, 
# to make them more concise.

from pathlib import Path

'''First code pi digits'''

path = Path("pi_digits.txt")
contents = path.read_text()
'''
lines = contents.splitlines()
for line in lines:
    print(line)
'''
for line in contents.splitlines():
    print(line)


''' Second code pi million digit'''
path = Path("pi_million_digits.txt")
contents = path.read_text()

pi_string = ''
'''
lines = contents.splitlines()
for line in lines:
    pi_string += line.lstrip()
'''
for line in contents.splitlines():
    pi_string += line.lstrip()
print(f"{pi_string[:52]}")
print(len(pi_string))

'''Last code about is your birthday in pi million digit?'''
path = Path("pi_million_digits.txt")
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday in the first million digit of pi!")
else:
    print("Your birthday does not in the first million digit of pi")