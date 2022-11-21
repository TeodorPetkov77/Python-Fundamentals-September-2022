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