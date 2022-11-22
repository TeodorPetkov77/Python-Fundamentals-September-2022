def morse_decode(code: list, morse_translate: dict):
    result = ''
    for word in code:
        for letter in word:
            result += morse_translate[letter]
        result += ' '
    print(result[0:len(result) - 1])


morse_codes = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
               '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
               '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
               '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
               '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
               '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
               '-.--': 'Y', '--..': 'Z'}


morse_input = [x.split() for x in input().split(" | ")]
morse_decode(morse_input, morse_codes)


