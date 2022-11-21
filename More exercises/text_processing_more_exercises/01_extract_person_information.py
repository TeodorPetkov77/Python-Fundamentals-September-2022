import re

pattern_names = re.compile('(?<=@)[A-Za-z]+(?=|)')
pattern_ages = re.compile('(?<=#)[\d]+(?=\*)')
n = int(input())
text_input = ' '.join([input() for i in range(n)])
names = re.findall(pattern_names, text_input)
ages = re.findall(pattern_ages, text_input)

for index in range(n):
    print(f"{names[index]} is {ages[index]} years old.")

# https://judge.softuni.org/Contests/Practice/Index/1741#0

# 1.	Extract Person Information
# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# •	The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# •	The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."
# Example
# Input	Output
# 2
# Here is a name @George| and an age #18*
# Another name @Billy| #35* is his age	George is 18 years old.
# Billy is 35 years old.
# 3
# random name @lilly| random digits #5*age
# @Marry| with age #19*
# here Comes @Garry|he is #48* years old	lilly is 5 years old.
# Marry is 19 years old.
# Garry is 48 years old.