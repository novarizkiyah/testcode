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
