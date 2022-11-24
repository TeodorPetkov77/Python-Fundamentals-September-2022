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
