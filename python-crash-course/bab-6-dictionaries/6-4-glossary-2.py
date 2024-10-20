#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. 
#When you’re sure that your loop works, add five more Python terms to your glossary. 
#When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    "Variable": "A named location used to store data in memory.",
    "Function": "A block of code that performs a specific task when called.",
    "Loop": "A sequence of instructions that repeats until a certain condition is met.",
    "List": "A collection of ordered and changeable elements.",
    "Dictionary": "A collection of key-value pairs used to store data in Python."
}

for key, value in glossary.items():
    print(f" {key} : {value}")