#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, 
# and a shirt of any size with a different message.

def make_shirt(size, sentences):
    print(f"I love Python, my size is {size} so {sentences}")

make_shirt("S", "cute")
make_shirt("L", "large")
make_shirt("M", "medium")
