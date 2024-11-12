#Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of the messages
# After calling the function,
# print both of your lists to show that the original list has retained its messages

messages = [
    "This is first message",
    "The second message",
    "Third mesages"
]
done_messages = []

def send_messages(messages, done_messages):
    while messages:
        current_messages = messages.pop()
        print(f"My messages now : {current_messages}")
        done_messages.append(current_messages)
        
def show_messages(done_messages):
    for done_message in done_messages: 
        print(done_message)

'''
send_messages(messages, done_messages)
show_messages(done_messages)

for message in messages:
    print(message)
'''


copy_messages = messages[:]
send_messages(copy_messages, done_messages)

print(messages)
print(copy_messages)
show_messages(done_messages)