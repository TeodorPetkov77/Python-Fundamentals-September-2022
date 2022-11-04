import re

pattern = r'((www[\.]){1})([a-zA-Z0-9\-]+)([\.]{1}[a-z]+)([\.]{1}[a-z]+)*'
text = input()

while len(text):
    links = re.finditer(pattern, text)
    for i in links:
        print(i.group())
    text = input()
