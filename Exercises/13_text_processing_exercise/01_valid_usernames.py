usernames = input().split(", ")
allowed_chars = "_-"
for name in usernames:
    valid = True
    for n in name:
        if not n.isalnum() and n not in allowed_chars:
            valid = False
            break
    if 3 <= len(name) <= 16 and valid:
        print(name)




# https://judge.softuni.org/Contests/Compete/Index/1740#0

# 1.	Valid Usernames
# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between
# Examples
# Input	Output
# sh, too_long_username, !lleg@l ch@rs, jeffbutt	jeffbutt
# Jeff, john45, ab, cd, peter-ivanov, @smith	Jeff
# John45
# peter-ivanov