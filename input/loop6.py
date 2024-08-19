#"while" loop keeps looping while its condition its True
# break statement will stop if the consition its True
# continue statement will continue if the condition its True
while True:
    print("Who are you? ")
    name=input()
    if name != "Nova":
        continue
    print("Hello, Nova. What is password? (clue: your hobby)")
    password = input()
    if password == "book":
        break
print("Access granted")