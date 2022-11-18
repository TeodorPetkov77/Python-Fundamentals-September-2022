def check_match(person_1, person_2, dictionary: dict):
    match = False
    for key in dictionary[person_1].keys():
        if key in dictionary[person_2].keys():
            match = True
            break
    return match


moba = {}

command = input()

while command != "Season end":
    if '->' in command:
        command = command.split(' -> ')
        name = command[0]
        position = command[1]
        points = int(command[2])
        if name not in moba.keys():
            moba[name] = {position: points}
        else:
            if position not in moba[name].keys():
                moba[name][position] = points
            if moba[name][position] < points:
                moba[name][position] = points
    else:
        command = command.split(' vs ')
        name_1 = command[0]
        name_2 = command[1]
        if name_1 in moba and name_2 in moba and \
                check_match(name_1, name_2, moba):
            name_1_total = (sum(moba[name_1].values()))
            name_2_total = (sum(moba[name_2].values()))
            if name_1_total > name_2_total:
                moba.pop(name_2)
            elif name_2_total > name_1_total:
                moba.pop(name_1)
    command = input()

for key, value in sorted(moba.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f'{key}: {(sum(moba[key].values()))} skill')
    for key1, value1 in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f'- {key1} <::> {value1}')
