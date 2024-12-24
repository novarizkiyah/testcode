# Open a blank file in your text editor and 
# write a few lines summarizing what you've learned about Python so far. 
# Start each line with the phrase In Python you can... 
# Save the file as learning_python.txt in the same directory as your exercises 
# from this chapter. 
# Write a program that reads the file and prints what you wrote two times: 
# print the contents once by reading in the entire file, 
# and once by storing the lines in a list and then looping over each line.

from pathlib import Path


path = Path("learning_python.txt")
contents = path.read_text()
print(contents)

print("Using loop")
lines = contents.splitlines()
for line in lines:
    print(line)

print("how many Python here")
count = 0
for line in lines:
    if 'Python' in line:
        count += 1
print(count)
