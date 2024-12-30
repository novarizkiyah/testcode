# Modify your except block in Exercise 10-8 
# to fail silently if either file is missing.

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    print(f"Reading file : {filename}")
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(content)