import re

text = input()

modded_text = re.sub(r'\\n', '', text)

pattern_title = re.compile('(?<=<title>)(\w+\s*)+(?=</title>)')
remove_tags_pattern = re.compile('<[^<>]+>')

if re.search(pattern_title, modded_text).group():
    print(f'Title: {re.search(pattern_title, modded_text).group()}')

modded_text = re.sub(r'<title>(\w+\s*)+</title>', '', modded_text)

tags_to_remove = [x.group() for x in re.finditer(remove_tags_pattern, modded_text)]

for tag in tags_to_remove:
    modded_text = re.sub(tag, '', modded_text)

print(f'Content: {modded_text}')

