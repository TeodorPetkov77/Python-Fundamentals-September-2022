def total_points(dictionary: dict):
    total = {}
    for key, value in dictionary.items():
        for key1, value1 in value.items():
            if key1 not in total.keys():
                total[key1] = int(value1)
            else:
                total[key1] += int(value1)
    return total


contests_dictionary = {}

command = input()

while command != 'no more time':
    command = command.split(' -> ')
    username, contest, points = command[0], command[1], int(command[2])
    if contest not in contests_dictionary.keys():
        contests_dictionary[contest] = {}
    if username not in contests_dictionary[contest]:
        contests_dictionary[contest][username] = 0
    if points > contests_dictionary[contest][username]:
        contests_dictionary[contest][username] = points
    command = input()

total_dictionary = total_points(contests_dictionary)

for key, value in contests_dictionary.items():
    print(f"{key}: {len(contests_dictionary[key])} participants")
    for item, (key1, value1) in enumerate(sorted(
            value.items(), key=lambda x: (-x[1], x[0]))):
        print(f'{item + 1}. {key1} <::> {value1}')

print("Individual standings:")
for item, (key, value) in enumerate(sorted(
        total_dictionary.items(), key=lambda x: (-x[1], x))):
    print(f"{item + 1}. {key} -> {value}")
