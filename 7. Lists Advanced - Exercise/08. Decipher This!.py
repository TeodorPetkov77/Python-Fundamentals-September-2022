message = input().split(" ")
for word in message:
    code = ""
    letters = ""
    for char in word:
        if char.isnumeric():
            code += char
        elif char.isalpha():
            letters += char
    if len(letters) == 1:
        decoded = str(chr(int(code)) + letters[1:(len(letters) - 1)] + letters[0])
    else:
        decoded = str(chr(int(code)) + letters[len(letters) - 1] + \
                  letters[1:(len(letters) - 1)] + letters[0])
    print(decoded, end=" ")
