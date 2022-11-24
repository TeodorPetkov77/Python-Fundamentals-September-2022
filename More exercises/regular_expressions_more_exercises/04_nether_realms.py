import re

health_pattern = re.compile('[^\d\+\-\*\/\.]')
damage_pattern = re.compile('[\-]?[0-9]+[\.]?[0-9]*')
operators_pattern = re.compile('[\*\/]')

demon_names = 'M3ph-0.5s-0.5t0.0**'
demon_health = sum([ord(x) for x in re.findall(health_pattern, demon_names)])
demon_damage = re.findall(damage_pattern, demon_names)
print(re.findall(operators_pattern, demon_names))
