def morse_translate(morse_list_input: list):
    result = ''
    for item in morse_list_input:
        for letter in item:
            if letter == '.-':
                result += 'A'
            elif letter == "-...":
                result += "B"
            elif letter == "-.-.":
                result += "C"
            elif letter == "-..":
                result += "D"
            elif letter == ".":
                result += "E"
            elif letter == "..-.":
                result += "F"
            elif letter == "--.":
                result += "G"
            elif letter == "....":
                result += "H"
            elif letter == "..":
                result += "I"
            elif letter == ".---":
                result += "J"
            elif letter == "-.-":
                result += "K"
            elif letter == ".-..":
                result += "L"
            elif letter == "--":
                result += "M"
            elif letter == "-.":
                result += "N"
            elif letter == "---":
                result += "O"
            elif letter == ".--.":
                result += "P"
            elif letter == "--.-":
                result += "Q"
            elif letter == ".-.":
                result += "R"
            elif letter == "...":
                result += "S"
            elif letter == "-":
                result += "T"
            elif letter == "..-":
                result += "U"
            elif letter == "...-":
                result += "V"
            elif letter == ".--":
                result += "W"
            elif letter == "-..-":
                result += "X"
            elif letter == "-.--":
                result += "Y"
            elif letter == "--..":
                result += "Z"
        result += ' '
    print(result[0:len(result) - 1])


morse_list = [item.split() for item in input().split(' | ')]
morse_translate(morse_list)