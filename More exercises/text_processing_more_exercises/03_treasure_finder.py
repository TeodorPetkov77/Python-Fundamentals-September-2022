import re

keys = list(map(int, input().split()))
string_input = input()
result_string = ""

while string_input != 'find':
    key_index = 0
    for index, char in enumerate(string_input):
        if key_index > len(keys) - 1:
            key_index = 0
        result_string += (chr(ord(string_input[index]) - keys[key_index]))
        key_index += 1
    string_input = input()

material_pattern = re.compile('(?<=&)\w+(?=&)')
location_pattern = re.compile('(?<=<)\w+(?=>)')

materials_list = material_pattern.findall(result_string)
locations_list = location_pattern.findall(result_string)

for index in range(len(materials_list)):
    print(f"Found {materials_list[index]} at {locations_list[index]}")

# https://judge.softuni.org/Contests/Practice/Index/1741#2

# 3.	Treasure Finder
# Write a program that decrypts a message by a given key and gathers information about hidden treasure type and its coordinates. On the first line, you will receive a key (sequence of numbers separated by a space). On the next few lines, you will receive lines with strings until you get the command "find".
# You should loop through every string and decrease the ASCII code of each character with a corresponding number of the key sequence. You choose a key number from the sequence by just looping through it. If the length of the key sequence is less than the string sequence, you should continue looping from the beginning.
# For more clarification, see the example below.
# After decrypting the message, you will get a type of treasure and its coordinates. The type will be between the symbol "&", and the coordinates - between the symbols "<' and '>'.
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".
# Example
# Input	Output	Comment
# 1 2 1 3
# ikegfp'jpne)bv=41P83X@
# ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
# find	Found gold at 10N70W
# Found Silver at 32S43W	We start looping through the first string and the key. When we reach the end of the key, we start looping from the beginning of the key, but we continue looping through the string. (until the string is over)
# The first message is: "hidden&gold&at<10N70W>" so we print we found gold at the given coordinates
# We do the same for the second string
# "thereIs&Silver&atCoordinates<32S43W>"(starting from the beginning of the key and the beginning of the string)