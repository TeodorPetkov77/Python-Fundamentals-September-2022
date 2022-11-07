sequence = input().split(" ")
repeated_strings = ""

for word in sequence:
    repeated_strings += word * len(word)

print(repeated_strings)