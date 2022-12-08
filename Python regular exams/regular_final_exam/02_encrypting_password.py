import re

pattern = re.compile(r'(.+)>(?P<password>[\d]{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1')

n = int(input())

for _ in range(n):
    password_input = input()
    if re.fullmatch(pattern, password_input):
        print(f'Password: '
              f'{"".join(re.search(pattern, password_input).group("password").split("|"))}')
    else:
        print("Try another password!")