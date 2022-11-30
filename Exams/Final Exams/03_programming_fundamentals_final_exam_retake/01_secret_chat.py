def insert_space(message: str, input_index: int):
    message = message[0:input_index] + " " + message[input_index:len(message)]
    print(message)
    return message


def reverse(message: str, substring: str):
    if substring in message:
        message = message.replace(substring, "", 1) + substring[::-1]
        print(message)
    else:
        print('error')
    return message


def change_all(message: str, substring: str, replacement: str):
    message = message.replace(substring, replacement)
    print(message)
    return message


text_message = input()
command = input()

while command != 'Reveal':
    command = command.split(':|:')
    action = command[0]
    if action == 'InsertSpace':
        index = int(command[1])
        text_message = insert_space(text_message, index)
    elif action == 'Reverse':
        input_substring = command[1]
        text_message = reverse(text_message, input_substring)
    elif action == 'ChangeAll':
        input_substring = command[1]
        rep_string = command[2]
        text_message = change_all(text_message, input_substring, rep_string)
    command = input()

print(f'You have a new text message: {text_message}')