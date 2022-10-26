sequence = input()
no_same = sequence[0]

for index in range(1, len(sequence)):
    if sequence[index - 1] == sequence[index]:
        continue
    no_same += sequence[index]

print(no_same)

# https://judge.softuni.org/Contests/Compete/Index/1740#5

# 6.	 Replace Repeating Chars
# Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.
# Examples
# Input	Output
# aaaaabbbbbcdddeeeedssaa	abcdedsa
# qqqwerqwecccwd	qwerqwecwd