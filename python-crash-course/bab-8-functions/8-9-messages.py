#Make a list containing a series of short text messages
# Pass the list to a function called show_messages(), 
# wich prints each text messages.

messages = [
    "This is first message",
    "The second message",
    "Third mesages"
]

def show_messages():
    for message in messages:
        print(message)

show_messages()