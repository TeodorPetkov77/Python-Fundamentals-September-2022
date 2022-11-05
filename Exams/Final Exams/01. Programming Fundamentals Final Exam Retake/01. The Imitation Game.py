def move(string: str, move_letters: int):
    string = string[move_letters: len(string)] + \
             string[0:move_letters]
    return string


def insert(string: str, index: int, value: str):
    string = string[0:index] + value + string[index:len(string)]
    return string


def changeall(string: str, substring: str, replace_string: str):
    string = string.replace(substring, replace_string)
    return string


word = input()
command = input()
while command != "Decode":
    command = command.split("|")
    if command[0] == "ChangeAll":
        substring = command[1]
        replace_string = command[2]
        word = changeall(word, substring, replace_string)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        word = insert(word, index, value)
    elif command[0] == "Move":
        number_of_letters = int(command[1])
        word = move(word, number_of_letters)
    command = input()

print(f"The decrypted message is: {word}")