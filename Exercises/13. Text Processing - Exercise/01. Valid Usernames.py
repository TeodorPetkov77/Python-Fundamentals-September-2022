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