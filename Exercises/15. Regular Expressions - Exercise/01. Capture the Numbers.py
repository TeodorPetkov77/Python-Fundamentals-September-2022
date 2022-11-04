import re

string_input = input()

while string_input:
    pattern = r"\d+"
    matches = re.finditer(pattern, string_input)
    for match in matches:
        print(match.group(), end=" ")
    string_input = input()


# https://judge.softuni.org/Contests/Compete/Index/1743#0

# 1.	Capture the Numbers
# Write a program that receives strings on different lines and extracts only the numbers. Print all extracted numbers on a single line, separated by a single space.
# Examples
# Input	Output
# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45	300 3 22 45
# 123a456
# 789b987
# 654c321
# 0	123 456 789 987 654 321 0
# Let's go11!!!11!
# Okey!1!	11 11 1