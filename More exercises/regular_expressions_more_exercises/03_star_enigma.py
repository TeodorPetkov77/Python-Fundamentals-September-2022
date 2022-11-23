import re

n = int(input())

key_pattern = re.compile('[STARstar]')
main_pattern = re.compile('[^@\-!:>]*(@)(?P<planet>[A-Za-z]+)[^@\-!:>]*'
                          '(:)([\d]+)[^@\-!:>]*(!)(?P<attack>[AD])(!)'
                          '[^@\-!:>]*(->)([\d]+)[^@\-!:>]*')

attacked = []
destroyed = []

for _ in range(n):
    text_input = input()
    key = len(re.findall(key_pattern, text_input))
    result_text = ''.join([chr(ord(i) - key) for i in text_input])
    if re.match(main_pattern, result_text):
        planet = re.match(main_pattern, result_text).group('planet')
        attack = re.match(main_pattern, result_text).group('attack')
        if attack == 'A':
            attacked.append(planet)
        elif attack == 'D':
            destroyed.append(planet)

print(f'Attacked planets: {len(attacked)}')
if attacked:
    for planet in sorted(attacked):
        print(f'-> {planet}')
print(f'Destroyed planets: {len(destroyed)}')
if destroyed:
    for planet in sorted(destroyed):
        print(f'-> {planet}')