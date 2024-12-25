# Write a program that prompts for the user's favorite number. 
# Use json.dumps() to store this number in a file. 
# Write a separate program that reads in this value and prints the message, 
# "I know your favorite number! It's _____."

from pathlib import Path
import json

numbers = [7, 17, 9, 6, 11, 4]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)