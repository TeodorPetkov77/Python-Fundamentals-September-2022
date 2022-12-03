import re

text = input()

emoji_pattern = re.compile(r'(?P<whole_emoji>(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\2)')
threshold_list = [int(x) for x in re.findall(r'[0-9]', text)]

cool_threshold = 1
for num in threshold_list:
    cool_threshold *= num

emoji_list = []
valid_emotes = 0

for valid_emotes, emoji in enumerate(re.finditer(emoji_pattern, text), start=1):
    if sum([ord(x) for x in emoji.group('emoji')]) > cool_threshold:
        emoji_list.append(emoji.group('whole_emoji'))

print(f'Cool threshold: {cool_threshold}')
print(f'{valid_emotes} emojis found in the text. The cool ones are:')
print(' \n'.join(emoji_list))

