def flip_string(input_text, upper_lower_f, start_index_f, end_index_f):
    work_string = ""
    if upper_lower_f == "Upper":
        work_string = input_text[start_index_f: end_index_f].upper()
    elif upper_lower_f == "Lower":
        work_string = input_text[start_index_f: end_index_f].lower()
    return input_text[:start_index_f] + work_string + input_text[end_index_f:]


def slice_string(input_text, start_index_f, end_index_f):
    return input_text[:start_index_f] + input_text[end_index_f:]


text_input = input()
command = input()

while command != "Generate":
    command = command.split('>>>')
    if command[0] == 'Contains':
        substring = command[1]
        if substring in text_input:
            print(f'{text_input} contains {substring}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        upper_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        text_input = flip_string(text_input, upper_lower, start_index, end_index)
        print(text_input)
    elif command[0] == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        text_input = slice_string(text_input, start_index, end_index)
        print(text_input)
    command = input()

print(f'Your activation key is: {text_input}')