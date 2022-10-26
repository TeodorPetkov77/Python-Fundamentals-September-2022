def alpha_position(a):
    position = ord(a.casefold()) - 96
    return position


sequence = [x.strip() for x in input().split(chr(32)) if x != '' and x != '\t']

total = 0

for item in sequence:
    front_letter = item[0]
    after_letter = item[-1]
    number = int(item[1:-1])
    if front_letter.isupper():
        result = number / alpha_position(front_letter)
    else:
        result = number * alpha_position(front_letter)
    if after_letter.isupper():
        result -= alpha_position(after_letter)
    else:
        result += alpha_position(after_letter)
    total += result

print(f"{total:.2f}")
