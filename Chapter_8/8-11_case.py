# def show_messages(messages):
#     for message in messages:
#         print(message)

list_messages = [
    "Chao buoi sang",
    "Good morning!",
    "Nihao",
    "Ohayou Gozaimasu",
    "Bonjour",
]
# show_messages(list_messages)


def send_messages(original_messages, sent_messages):
    while original_messages:
        current_message = original_messages.pop()
        sent_messages.append(current_message)


after_messages = []
send_messages(list_messages[:], after_messages)

print(f"This is a list_messages {list_messages}")
print(f"This is an after_messages {after_messages}")
