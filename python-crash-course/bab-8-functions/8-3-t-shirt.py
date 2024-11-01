#Write a function called make_shirt() that accepts a size and 
# the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of 
# the shirt and the message printed on it.

#Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

# Positional argument
def make_shirt(size, sentences):
    print(f"My size is {size} so {sentences}")

make_shirt("S", "this is cute")

#Keyword argument
def make_shirt(size, sentences):
    print(f"My size is {size} so {sentences}")

make_shirt(size="S", sentences="this is cute")