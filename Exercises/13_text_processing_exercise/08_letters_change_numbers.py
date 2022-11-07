def alpha_position(a):
    position = ord(a.casefold()) - 96
    return position


sequence = [x.strip() for x in input().split(chr(32)) if x != '' and x != '\t']

total = 0

for item in sequence:
    front_letter = item[0]
    back_letter = item[-1]
    number = int(item[1:-1])
    if front_letter.isupper():
        result = number / alpha_position(front_letter)
    else:
        result = number * alpha_position(front_letter)
    if back_letter.isupper():
        result -= alpha_position(back_letter)
    else:
        result += alpha_position(back_letter)
    total += result

print(f"{total:.2f}")



# https://judge.softuni.org/Contests/Compete/Index/1740#7

# *Letters Change Numbers
# John invented a game with numbers and letters from the English alphabet. The game was simple.
# You receive a string consisting of a number between two letters. For the given string, you should perform different mathematical operations to achieve a result:
# •	First, if the letter in front of the number is:
# o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# •	Next, if the letter after the number is:
# o	Uppercase: subtract its position from the resulting number (starting from 1)
# o	Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each string.
# Input
# •	The input comes from the console as a single line, holding a sequence of strings
# •	Strings are separated by one or more white spaces
# •	The input data will always be valid. There is no need to check it explicitly
# Output
# •	Print at the console a single number:
# o	The total sum of all processed numbers, formatted to the second decimal separator
# Constraints
# •	The count of the strings will be in the range [1 … 10]
# •	The numbers between the letters will be integers in the range [1 … 2 147 483 647]
# •	Time limit: 0.3 sec. Memory limit: 16 MB
# Examples
# Input	Output	Comments
# A12b s17G	330.00	12/1=12, 12+2=14, 17*19=323, 323–7=316, 14+316=330
# P34562Z q2576f   H456z	46015.12
# a1A	0.00
