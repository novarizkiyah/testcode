# Combine the two programs from Exercise 10-11 into one file. 
# If the number is already stored, report the favorite number to the user. 
# If not, prompt for the user's favorite number and store it in a file. 
# Run the program twice to see that it works.

from pathlib import Path
import json

path = Path('numbers2.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    favorite_number = int(input("What's your favorite number? "))
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print("I will remember that")
else:
    favorite_number = json.loads(contents)
    print(f"I know your favorite number is {favorite_number}")