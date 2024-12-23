# Make two files, cats.txt and dogs.txt. 
# Store at least three names of cats in the first file and three names of dogs 
# in the second file. 
# Write a program that tries to read these files and 
# print the contents of the file to the screen. 
# Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing. 
# Move one of the files to a different location on your system, 
# and make sure the code in the except block executes properly.

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

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(f"Reading file : {filename}")
    path = Path(filename)
    try:
        content = path.read_text()
    except FileNotFoundError:
        print("The file is missing")
    else:
        print(content)
