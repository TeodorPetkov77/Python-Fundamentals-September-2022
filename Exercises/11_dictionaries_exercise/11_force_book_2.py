def find_user(f_user: str, dictionary: dict):
    side = False
    for f_key, f_value in dictionary.items():
        for name in f_value:
            if name == f_user:
                side = f_key
                break
    return side


def add_user(f_user: str, side: str, dictionary: dict):
    if side not in dictionary:
        dictionary[side] = []
    if not find_user(f_user, dictionary):
        dictionary[side].append(f_user)
    return dictionary


def switch_user_side(f_user: str, new_side: str, dictionary: dict):
    if find_user(f_user, dictionary):
        if new_side not in dictionary.keys():
            dictionary[new_side] = []
        dictionary[new_side].append(dictionary[find_user(f_user, dictionary)].
                                    pop(dictionary[find_user(f_user, dictionary)].
                                        index(f_user)))
    if not find_user(f_user, dictionary):
        add_user(f_user, new_side, dictionary)
    print(f'{f_user} joins the {new_side} side!')
    return dictionary


force_dictionary = {}

command = input()

while command != 'Lumpawaroo':
    if ' | ' in command:
        command = command.split(' | ')
        force_side, force_user = command[0], command[1]
        add_user(force_user, force_side, force_dictionary)
    elif ' -> ' in command:
        command = command.split(' -> ')
        force_user, force_side = command[0], command[1]
        switch_user_side(force_user, force_side, force_dictionary)
    command = input()

for key, value in force_dictionary.items():
    if value:
        print(f'Side: {key}, Members: {len(value)}')
        for user in value:
            print(f'! {user}')

# https://judge.softuni.org/Contests/Compete/Index/1737#10
