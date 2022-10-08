def password_validator(pass_word):
    n = 0
    not_alpha_num = False
    valid = True
    for i in pass_word:
        if i.isnumeric():
            n += 1
        if not i.isnumeric() and not i.isalpha():
            not_alpha_num = True
    if not 6 <= len(pass_word) <= 10:
        print("Password must be between 6 and 10 characters")
        valid = False
    if not_alpha_num:
        print("Password must consist only of letters and digits")
        valid = False
    if n < 2:
        print("Password must have at least 2 digits")
        valid = False
    if valid:
        print("Password is valid")


pass_w = input()
password_validator(pass_w)
