symbols = input()

digits = ""
letters = ""
other = ""

for sym in symbols:
    if sym.isnumeric():
        digits += sym
    elif sym.isalpha():
        letters += sym
    else:
        other += sym

print(digits)
print(letters)
print(other)