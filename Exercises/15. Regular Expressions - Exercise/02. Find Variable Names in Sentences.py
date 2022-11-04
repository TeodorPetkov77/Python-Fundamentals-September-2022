import re

text = input()
pattern = r"\s_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, text)

print(",".join(matches))

# https://judge.softuni.org/Contests/Compete/Index/1743#1

# 2.	Find Variable Names in Sentences
# Write a program that finds all variable names in each string. A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits. Extract only their names without the underscore. Try to do this only with regular expressions.
# The output consists of all variable names extracted and printed on a single line, separated by a comma.
# Input	Output
# The _id and _age variables are both integers.	id,age
# Calculate the _area of the _perfectRectangle object.	area,perfectRectangle
# __invalidVariable _evenMoreInvalidVariable_ _validVariable	validVariable