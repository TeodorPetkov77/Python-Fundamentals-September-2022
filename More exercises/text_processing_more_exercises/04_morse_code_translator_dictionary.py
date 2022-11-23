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




# https://judge.softuni.org/Contests/Practice/Index/1741#3

# 4.	Morse Code Translator
# Write a program that translates messages from Morse code to English (capital letters). Use this page to help you (without the numbers). The words will be separated by a space (' '). Each word is separated by a ' | '.
# Print the found words on one line, separated by a space.
# Example
# Input	Output
# .. | -- .- -.. . |  -.-- --- ..- | .-- .-. .. - . | .- | .-.. --- -. --. | -.-. --- -.. .	I MADE YOU WRITE A LONG CODE
# .. | .... --- .--. . | -.-- --- ..- | .- .-. . | -. --- - | -- .- -..	I HOPE YOU ARE NOT MAD