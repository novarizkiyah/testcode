from pathlib import Path

path = Path('numbers.json')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)
print(f"I know your favorite number is {contents}")