two_chars = [ord(input()), ord(input())]
small = min(two_chars)
big = max(two_chars)
characters_input = input()
total_sum = 0

for char in characters_input:
    if small < ord(char) < big:
        total_sum += ord(char)

print(total_sum)