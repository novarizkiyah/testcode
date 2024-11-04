#Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of the messages
# After calling the function,
# print both of your lists to show that the original list has retained its messages

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

print_messages(messages[:], sent_messages)
show_messages(sent_messages)