import re

demon_names = [x.strip() for x in input().split(',')]
demon_dictionary = {}

health_pattern = re.compile('[^\d\+\-\*\/\.]')
damage_pattern = re.compile('[\-]?[0-9]+[\.]?[0-9]*')
operators_pattern = re.compile('[\*\/]')

for demon_name in demon_names:

    demon_health = sum([ord(x) for x in re.findall(health_pattern, demon_name)])
    demon_damage = sum([float(x) for x in re.findall(damage_pattern, demon_name)])
    operators = re.findall(operators_pattern, demon_name)

    for operator in operators:
        if operator == "*":
            demon_damage *= 2
        elif operator == "/":
            demon_damage /= 2
    demon_dictionary[demon_name] = \
        f'{demon_health} health, {demon_damage:.2f} damage'

for key, value in sorted(demon_dictionary.items()):
    print(f'{key} - {value}')

# https://judge.softuni.org/Contests/Practice/Index/1744#3

# 4.	Nether Realms
# Mighty battle is coming. In the stormy nether realms, demons are fighting against each other for supremacy in a duel from which only one will survive.
# Your job, however is not so exciting. You are assigned to sign in all the participants in the nether realm's mighty battle's demon book, which of course is sorted alphabetically.
# A demon's name contains his health and his damage.
# The sum of the asci codes of all characters (excluding numbers (0-9), arithmetic symbols ('+', '-', '*', '/') and delimiter dot ('.')) gives a demon's total health.
# The sum of all numbers in his name forms his base damage. Note that you should consider the plus '+' and minus '-' signs (e.g. +10 is 10 and -10 is -10). However, there are some symbols ('*' and '/') that can further alter the base damage by multiplying or dividing it by 2 (e.g. in the name "m15*/c-5.0", the base damage is 15 + (-5.0) = 10 and then you need to multiply it by 2 (e.g. 10 * 2 = 20) and then divide it by 2 (e.g. 20 / 2 = 10)).
# So, multiplication and division are applied only after all numbers are included in the calculation and in the order they appear in the name.
# You will get all demons on a single line, separated by commas and zero or more blank spaces. Sort them in alphabetical order and print their names along their health and damage.
# Input
# The input will be read from the console. The input consists of a single line containing all demon names separated by commas and zero or more spaces in the format: "{demon name}, {demon name}, … {demon name}"
# Output
# Print all demons sorted by their name in ascending order, each on a separate line in the format:
# •	"{demon name} - {health points} health, {damage points} damage"
# Constraints
# •	A demon's name will contain at least one character
# •	A demon's name cannot contain blank spaces ' ' or commas ','
# •	A floating point number will always have digits before and after its decimal separator
# •	Number in a demon's name is considered everything that is a valid integer or floating point number (with dot '.' used as separator). For example, all these are valid numbers: '4', '+4', '-4', '3.5', '+3.5', '-3.5'
# Examples
# Input	Output	Comments
# M3ph-0.5s-0.5t0.0**	M3ph-0.5s-0.5t0.0** - 524 health, 8.00 damage	M3ph-0.5s-0.5t0.0**:
# Health = 'M' + 'p' + 'h' + 's' + 't' = 524 health.
# Damage = (3 + (-0.5) + (-0.5) + 0.0) * 2 * 2 = 8 damage.
# Input	Output	Comments
# M3ph1st0**, Azazel	Azazel - 615 health, 0.00 damage
# M3ph1st0** - 524 health, 16.00 damage
# 	Azazel:
# Health - 'A' + 'z' + 'a' + 'z' + 'e' + 'l' = 615 health. Damage - no digits = 0 damage.
#
# M3ph1st0**:
# Health - 'M' + 'p' + 'h' + 's' + 't' = 524 health.
# Damage - (3 + 1 + 0) * 2 * 2 = 16 damage.
# Gos/ho	Gos/ho - 512 health, 0.00 damage