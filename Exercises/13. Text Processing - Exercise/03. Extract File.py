file_path = input().split(chr(92))
file_and_ext = file_path[-1].split(".")
file_name = file_and_ext[0]
file_ext = file_and_ext[1]

print(f"File name: {file_name}")
print(f"File extension: {file_ext}")




# https://judge.softuni.org/Contests/Compete/Index/1740#2

# Extract File
# Write a program that reads the path to a file and subtracts the file name and its extension.
# Examples
# Input	Output
# C:\Internal\training-internal\Template.pptx	File name: Template
# File extension: pptx