import re

string_input = input()

while string_input:
    pattern = r"\d+"
    matches = re.finditer(pattern, string_input)
    for match in matches:
        print(match.group(), end=" ")
    string_input = input()
