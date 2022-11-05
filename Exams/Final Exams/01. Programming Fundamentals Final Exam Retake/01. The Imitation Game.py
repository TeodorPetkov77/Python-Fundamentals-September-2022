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

# https://judge.softuni.org/Contests/Practice/Index/2525#0

# Problem 1 - The Imitation Game
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#0.
#
# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code. Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"
# Examples
# Input	Output
# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode	The decrypted message is: Hello
# Comments
# ChangeAll|z|l
# zzHe → llHe (We replace all occurrences of 'z' with 'l')
# Insert|2|o
# llHe → lloHe (We add an 'o' before the character on index 2)
# Move|3
# lloHe → Hello (We take the first three characters and move them to the end of the string)
# Finally, after receiving the "Decode" command, we print the resulting message.
# Input	Output
# owyouh
# Move|2
# Move|3
# Insert|3|are
# Insert|9|?
# Decode	The decrypted message is: howareyou?
# JS Examples
# Input	Output
# [
#   'zzHe',
#   'ChangeAll|z|l',
#   'Insert|2|o',
#   'Move|3',
#   'Decode',
# ]	The decrypted message is: Hello
# Comments
# ChangeAll|z|l
# zzHe → llHe (We replace all occurrences of 'z' with 'l')
# Insert|2|o
# llHe → lloHe (We add an 'o' before the character on index 2)
# Move|3
# lloHe → Hello (We take the first three characters and move them to the end of the string)
# Finally, after receiving the "Decode" command, we print the resulting message.
# Input		Output
# [
#   'owyouh',
#   'Move|2',
#   'Move|3',
#   'Insert|3|are',
#   'Insert|9|?'
#   'Decode',
# ]	The decrypted message is: howareyou?