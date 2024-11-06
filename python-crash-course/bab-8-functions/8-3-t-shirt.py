#Write a function called make_shirt() that accepts a size and 
# the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of 
# the shirt and the message printed on it.

#Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

# Positional argument
def make_shirt(size, message):
    print(f"{size} : {message}")

make_shirt("S", "Small")
make_shirt("M", "Medium")
make_shirt("Small", "S")

#Keyword argument
def make_shirt(size, message):
    print(f"{size} : {message}")

make_shirt(size="S", message="Small")
make_shirt(message="Medium", size="M")