def swicharoo(dictionary, side, other_side, user):
    index = dictionary[other_side].index(user)
    removed_user = dictionary[other_side].pop(index)
    dictionary[side].append(removed_user)
    return dictionary


def get_position(dictionary, item):
    for key, value in dictionary.items():
        for name in value:
            if name == item:
                position = key
                break
    return position


force_book = {}
list_of_users = []
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        if force_side not in force_book:
            force_book[force_side] = []
        if force_user not in list_of_users:
            force_book[force_side].append(force_user)
            list_of_users.append(force_user)
        if force_user in force_book:
            continue
    elif "->" in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        if force_side not in force_book:
            force_book[force_side] = []
        if force_user not in list_of_users:
            force_book[force_side].append(force_user)
            list_of_users.append(force_user)
        if force_user in list_of_users:
            switch_side = get_position(force_book, force_user)
            force_book = swicharoo(force_book, force_side, switch_side, force_user)
            print(f"{force_user} joins the {force_side} side!")
    command = input()

force_book = {key: value for key, value in force_book.items() if len(value) > 0}

for key, value in force_book.items():
    print(f"Side: {key}, Members: {len(value)}")
    for name in value:
        print(f"! {name}")