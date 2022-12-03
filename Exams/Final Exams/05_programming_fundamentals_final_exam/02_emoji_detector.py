import re

text = input()

emoji_pattern = re.compile(r'(?P<whole_emoji>(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\2)')
threshold_list = [int(x) for x in re.findall(r'[0-9]', text)]

if threshold_list:
    cool_threshold = 1
    for num in threshold_list:
        cool_threshold *= num
else:
    cool_threshold = 0

emoji_list = []
valids = 0

for valids, emoji in enumerate(re.finditer(emoji_pattern, text)):
    if sum([ord(x) for x in emoji.group('emoji')]) > cool_threshold:
        emoji_list.append(emoji.group('whole_emoji'))

print(f'Cool threshold: {cool_threshold}')
print(f'{valids + 1} emojis found in the text. The cool ones are:')
print(' \n'.join(emoji_list))

