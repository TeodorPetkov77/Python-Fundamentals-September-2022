import re

racers = {racer: 0 for racer in list(input().split(', '))}

pattern_name = re.compile('[A-Za-z]+')
pattern_distance = re.compile('[0-9]')

scramble = input()

while scramble != 'end of race':
    name = ''.join(re.findall(pattern_name, scramble))
    if name in racers.keys():
        distance = sum([int(x) for x in re.findall(pattern_distance, scramble)])
        racers[name] += distance
    scramble = input()

racers = list(sorted(racers.items(), key=lambda x: -x[1]))
print(f'1st place: {racers[0][0]}')
print(f'2nd place: {racers[1][0]}')
print(f'3rd place: {racers[2][0]}')