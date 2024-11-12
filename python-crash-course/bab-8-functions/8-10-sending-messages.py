#Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text messages 
# and moves each message to a new list called sent_messages as its printed.
# After calling the functon,
# print both of your list to make sure the messages were moved correctly

messages = [
    "This is first message",
    "The second message",
    "Third mesages"
]
done_messages = []
'''
# Move the messages to done messages
while messages:
    current_messages = messages.pop()
    print(f"My messages is : {current_messages}")
    done_messages.append(current_messages)

# Display all of the sent messages:
print("This is the sent messages:")
for done_message in done_messages:
    print(done_message)

'''

# This is using functions

# Move the messages to done messages
def sent_messages(messages, done_messages):
    while messages:
        current_messages = messages.pop()
        print(f"My messages is : {current_messages}")
        done_messages.append(current_messages)

# Display all of the done messages:
def show_messages(done_messages):
    print("This is the sent messages:")
    for done_message in done_messages:
        print(done_message)

sent_messages(messages,done_messages)
show_messages(done_messages)

for message in messages:
    print(f"any message {message}")




