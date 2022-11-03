import re

sentence = input()
word = input()
pattern = fr'\b{word}\b'

print(len(list(re.findall(pattern, sentence, re.IGNORECASE))))