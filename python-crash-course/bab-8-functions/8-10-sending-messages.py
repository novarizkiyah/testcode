#Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints eaxh text messafes 
# and moves each message to a new list called sent_messages as its printed.
# After calling the functon,
# print both of your list to make sure the messages were moved correctly

# The last code
'''
messages = ['Hi Epriibodiihh',
              'Hi Prabowoooooo',
               'Hi Pusaosadakdnuvo']
sent_messages = []

# move from messages to sent messages
while messages:
    current_message = messages.pop()
    print(f"Current messages is {current_message}")
    sent_messages.append(current_message)

#Displat all sent messages
print("This is the complete sent messages")
for message in sent_messages:
    print(message)
'''

def print_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Current messages is {current_message}")
        sent_messages.append(current_message)
def show_messages(sent_messages):
    print("This is the complete sent messages :")
    for message in sent_messages:
        print(message)
messages = ['Hi Epriibodiihh',
              'Hi Prabowoooooo',
               'Hi Pusaosadakdnuvo']
sent_messages = []

print_messages(messages, sent_messages)
show_messages(sent_messages)