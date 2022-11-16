def best_candidate(dictionary: dict):
    best_name = ''
    best_points = 0
    for key, value in dictionary.items():
        current_points = 0
        for key1, value1 in value.items():
            current_points += int(value1)
        if current_points > best_points:
            best_name = key
            best_points = current_points
    print(f"Best candidate is {best_name} with total {best_points} points.")


contests_passes = {}

command = input()

while command != "end of contests":
    command = command.split(":")
    contest, password = command[0], command[1]
    contests_passes[contest] = password
    command = input()

final_results = {}

command = input()

while command != 'end of submissions':
    command = command.split('=>')
    contest, password, user, points = \
        command[0], command[1], command[2], int(command[3])
    if contest in contests_passes.keys() \
            and password == contests_passes[contest]:
        if user not in final_results:
            final_results[user] = {}
        if contest not in final_results[user].keys():
            final_results[user][contest] = points
        else:
            if points > final_results[user][contest]:
                final_results[user][contest] = points
    command = input()

best_candidate(final_results)
print("Ranking:")
for key, value in sorted(final_results.items()):
    print(key)
    for key1, value1 in sorted(value.items(), key=lambda x: x[1], reverse=True):
        print(f"#  {key1} -> {value1}")