def take_odd(text: str):
    return text[1:len(text):2]


def cut_text(text: str, index_f: int, lenght_f: int):
    substring_f = text[index_f: index_f + lenght_f]
    return text.replace(substring_f, '', 1)


text_input = input()
command = input()

while command != 'Done':
    command = command.split()
    if command[0] == 'TakeOdd':
        text_input = take_odd(text_input)
        print(text_input)
    elif command[0] == 'Cut':
        start_index = int(command[1])
        length_input = int(command[2])
        text_input = cut_text(text_input, start_index, length_input)
        print(text_input)
    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in text_input:
            text_input = text_input.replace(substring, substitute)
            print(text_input)
        else:
            print('Nothing to replace!')
    command = input()

print(f'Your password is: {text_input}')