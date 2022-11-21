import re

pattern_names = re.compile('(?<=@)[A-Za-z]+(?=|)')
pattern_ages = re.compile('(?<=#)[\d]+(?=\*)')
n = int(input())
text_input = ' '.join([input() for i in range(n)])
names = re.findall(pattern_names, text_input)
ages = re.findall(pattern_ages, text_input)

for index in range(n):
    print(f"{names[index]} is {ages[index]} years old.")