# Choose ant three programs you wrote for this chapter
# and make sure they follow the styling guidelines describes in this section


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



# Create a copy of the messages list
messages_copy = messages[:]

# Send messages using the copy
print_messages(messages_copy, sent_messages)

# Print both lists to show original messages are retained
print("\nOriginal messages:")
print(messages)
print("\nDone messages:")
show_messages(sent_messages)