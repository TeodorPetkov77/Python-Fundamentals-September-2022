import re

text_input = input()
pattern = re.compile(r'(\@|\#)(?P<word_1>[A-Za-z]{3,})\1{2}(?P<word_2>[A-Za-z]{3,})\1')
mirror_words = []
valid = 0

if re.findall(pattern, text_input):
    for valid, item in enumerate(re.finditer(pattern, text_input)):
        if item.group('word_1') == item.group('word_2')[::-1]:
            mirror_words.append(f'{item.group("word_1")} <=> {item.group("word_2")}')
    print(f'{valid + 1} word pairs found!')
else:
    print('No word pairs found!')

if mirror_words:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print('No mirror words!')


