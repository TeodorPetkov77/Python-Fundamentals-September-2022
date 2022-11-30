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

# https://judge.softuni.org/Contests/Practice/Index/2307#0

# Problem 1 - Secret Chat
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#0.
#
# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go ahead and type it in!
# On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given, you will receive strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
# •	"InsertSpace:|:{index}":
# o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
# o	Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by ":|:".
# Output
# •	After each set of instructions, print the resulting string.
# •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"
# Examples
# Input	Output
# heVVodar!gniV
# ChangeAll:|:V:|:l
# Reverse:|:!gnil
# InsertSpace:|:5
# Reveal	hellodar!gnil
# hellodarling!
# hello darling!
# You have a new text message: hello darling!
# Comments
# ChangeAll:|:V:|:l
# heVVodar!gniV -> hellodar!gnil (We replace all occurrences of "V" with "l")
# Reverse:|:!gnil
# hellodar!gnil -> !gnil -> ling! -> hellodarling! (We reverse !gnil to ling! And put it at the end of the string)
# InsertSpace:|:5
# hellodarling! -> hello.darling! (We insert a space at index 5)
# Finally, after receiving the "Reveal" command, we print the resulting message.
# Input	Output
# Hiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal	Howare?uoy
# Howareyou?
# error
# How areyou?
# How are you?
# You have a new text message: How are you?