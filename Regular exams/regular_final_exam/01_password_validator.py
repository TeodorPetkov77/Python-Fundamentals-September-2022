import re


def make_upper(text_f: str, index_f: int):
    if index_f in range(len(text_f)):
        char_upper = text_f[index_f].upper()
        text_f = text_f[:index_f] + char_upper + text_f[index_f + 1:]
    print(text_f)
    return text_f


def make_lower(text_f: str, index_f: int):
    if index_f in range(len(text_f)):
        char_upper = text_f[index_f].lower()
        text_f = text_f[:index_f] + char_upper + text_f[index_f + 1:]
    print(text_f)
    return text_f


def insert_char(text_f, index_f: int, char_f: str):
    if index_f in range(len(text_f) + 1):
        text_f = text_f[:index_f] + char_f + text_f[index_f:]
    print(text_f)
    return text_f


def replace_char(text_f: str, char_f: str, value_f: int):
    if char_f in text_f:
        text_f = text_f.replace(char_f, chr(ord(char_f) + value_f))
    print(text_f)
    return text_f


def is_valid(text_f: str):
    is_8_chars = False
    contains_l_d = False
    contains_upper = False
    contains_lower = False
    contains_digit = False
    if len(text_f) >= 8:
        is_8_chars = True
    if re.fullmatch(r'[A-Za-z0-9_]+', text_f):
        contains_l_d = True
    for char_f in text_f:
        if char_f.isupper():
            contains_upper = True
        elif char_f.islower():
            contains_lower = True
        elif char_f.isnumeric():
            contains_digit = True
    if not is_8_chars:
        print("Password must be at least 8 characters long!")
    if not contains_l_d:
        print("Password must consist only of letters, digits and _!")
    if not contains_upper:
        print("Password must consist at least one uppercase letter!")
    if not contains_lower:
        print("Password must consist at least one lowercase letter!")
    if not contains_digit:
        print("Password must consist at least one digit!")
    return text_f


password_input = input()
command = input()

while command != "Complete":
    command = command.split()
    action = command[0]
    if action == "Make":
        index = int(command[2])
        if command[1] == "Upper":
            password_input = make_upper(password_input, index)
        elif command[1] == "Lower":
            password_input = make_lower(password_input, index)
    elif action == "Insert":
        index = int(command[1])
        char = command[2]
        password_input = insert_char(password_input, index, char)
    elif action == "Replace":
        char = command[1]
        value = int(command[2])
        password_input = replace_char(password_input, char, value)
    elif action == "Validation":
        password_input = is_valid(password_input)
    command = input()