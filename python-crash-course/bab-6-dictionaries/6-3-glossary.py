# Think of five programming words you learn so far. Use these words as the keys in your glossary.
# Print each word ans its meaning. Use the newline character to insert blank line

glossary = {
    "Variable": "A named location used to store data in memory.",
    "Function": "A block of code that performs a specific task when called.",
    "Loop": "A sequence of instructions that repeats until a certain condition is met.",
    "List": "A collection of ordered and changeable elements.",
    "Dictionary": "A collection of key-value pairs used to store data in Python."
}

# Print each word with its meaning and a blank line in between

word = 'Variable'
print(f"{word} : " + glossary[word])

word = 'Function'
print(f"{word} : " + glossary[word])

word = 'Loop'
print(f"{word} : " + glossary[word])

word = 'List'
print(f"{word} : " + glossary[word])

word = 'Dictionary'
print(f"{word} : " + glossary[word])




#for word, meaning in glossary.items():
#    print(f"{word}: {meaning}\n")