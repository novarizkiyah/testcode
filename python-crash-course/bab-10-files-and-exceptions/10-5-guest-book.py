# Write a while loop that prompts users for their name. 
# Collect all the names that are entered, and then write these names 
# to a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

from pathlib import Path


guest_name = []

while True:
    content = input("What is your name? 'quit' to exit")
    
    if content == 'quit':
        break
    guest_name.append(content)


file_string = ''
for content in guest_name:
    file_string += f"{content}\n"


path = Path('guest_book.txt')
path.write_text(file_string)