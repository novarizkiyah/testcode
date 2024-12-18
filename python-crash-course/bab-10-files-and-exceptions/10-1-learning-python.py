# Open a blank file in your text editor and 
# write a few lines summarizing what you've learned about Python so far. 
# Start each line with the phrase In Python you can... 
# Save the file as learning_python.txt in the same directory as your exercises from this 
# chapter. 
# Write a program that reads the file and prints what you wrote two times: 
# print the contents once by reading in the entire file, 
# and once by storing the lines in a list and then looping over each line.

from pathlib import Path

print("\n ---- Reading entire lines")
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)


print("\n--- Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)

print("\n--- Print only Python keyword:")
for line in lines:
    if 'Python' in line:
        print(line)

print("\n --- Make lines upper")
for line in lines:
    print(line.upper())

print("\n --- Do not print Python lines")
for line in lines:
    if 'Python' not in line:
        print(line)

print("\n --- How much Python in lines")
count = 0
for line in lines:
    if 'Python' in line:
        count += 1
print(count)