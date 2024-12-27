# Write a while loop that prompts users for their name. 
# Collect all the names that are entered, and then write these names 
# to a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

from pathlib import Path

guest_list = []
path = Path("guest_book.txt")
while True:
    content = input("What is your name? type 'quit' to exit ")
    if content == 'quit':
        break
    else:
        print(f"We will add {content} to our guest list")
        guest_list.append(content)

string = ""
for content in guest_list:
    string += f"{content.title()}\n"
path.write_text(string)
