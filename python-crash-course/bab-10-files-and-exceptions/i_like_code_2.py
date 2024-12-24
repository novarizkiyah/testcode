
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

'''
In Python you can make everything
From Data to Devops
From easy to hard
everything in Python
and I can see myself 
growing like Python community grow
'''
