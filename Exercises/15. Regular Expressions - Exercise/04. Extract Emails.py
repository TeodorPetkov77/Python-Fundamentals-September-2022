import re

text_input = input()
pattern = r'(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-][A-Za-z]+)+))(\b|(?=\s))'
emails = re.finditer(pattern, text_input)

for i in emails:
    print(i.group())