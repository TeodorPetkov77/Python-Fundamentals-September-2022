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

racers = sorted(racers.items(), key=lambda x: -x[1])
print(f'1st place: {racers[0][0]}')
print(f'2nd place: {racers[1][0]}')
print(f'3rd place: {racers[2][0]}')

# https://judge.softuni.org/Contests/Practice/Index/1744#0

# 1.	Race
# Write a program that processes information about a race.
# On the first line you will be given list of participants separated by ", ".
# On the next few lines until you receive a line "end of race" you will be
# given some info which will be some alphanumeric characters.
# In between them you could have some extra characters which you should ignore.
# For example: "G!32e%o7r#32g$235@!2e".
# The letters are the name of the person and the sum of the digits is
# the distance he ran. So here we have George who ran 29 km.
# Store the information about the person only if the list of racers
# contains the name of the person. If you receive the same person more
# than once just add the distance to his old distance. At the end print
# the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"
# Examples
# Input	Output	Comment
# George, Peter, Bill, Tom
# G4e@55or%6g6!68e!!@
# R1@!3a$y4456@
# B5@i@#123ll
# G@e54o$r6ge#
# 7P%et^#e5346r
# T$o553m&6
# end of race	1st place: George
# 2nd place: Peter
# 3rd place: Tom	On the 3rd input line we have Ray.
# He is not in the list, so we do not count his result.
# The other ones are valid. George has total of 55 km,
# Peter has 25 and Tom has 19. We do not print Bill because he is on 4th place.