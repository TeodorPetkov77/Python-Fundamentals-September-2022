two_chars = [ord(input()), ord(input())]
small = min(two_chars)
big = max(two_chars)
characters_input = input()
total_sum = 0

for char in characters_input:
    if small < ord(char) < big:
        total_sum += ord(char)

print(total_sum)

# https://judge.softuni.org/Contests/Practice/Index/1741#1

# 2.	ASCII Sumator
# Write a program that prints the sum of all found characters between two given characters (their ASCII code). On each of the first two lines, you will receive a single character. On the last line, you get a random string. Print the sum of the ASCII values of all characters in the random string between the two given characters in the ASCII table.
# Example
# Input	Output
# .
# @
# dsg12gr5653feee5	363	The found characters are 1, 2, 5, 6, 5, 3 and 5. Their ASCII sum is 49 + 50 + 53 + 54 + 53 + 51 + 53 = 363.
# ?
# E
# @ABCEF	262