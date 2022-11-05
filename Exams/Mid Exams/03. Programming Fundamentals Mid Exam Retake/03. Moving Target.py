targets = list(map(int, input().split(" ")))

command = input()

while command != "End":
    command = command.split(" ")
    shot_index = int(command[1])
    if command[0] == "Shoot":
        if shot_index not in range(len(targets)):
            command = input()
            continue
        targets[shot_index] -= int(command[2])
        if targets[int(command[1])] <= 0:
            targets.pop(shot_index)
    elif command[0] == "Add":
        if shot_index not in range(len(targets)):
            print("Invalid placement!")
            command = input()
            continue
        targets.insert(shot_index, int(command[2]))
    elif command[0] == "Strike":
        if shot_index - int(command[2]) in range(len(targets)) and \
                shot_index + int(command[2]) in range(len(targets)):
            for i in range(shot_index + int(command[2]),
                           shot_index - int(command[2]) - 1, -1):
                targets.pop(i)
        else:
            print("Strike missed!")
            command = input()
            continue
    command = input()

print("|".join(list(map(str, targets))))

# https://judge.softuni.org/Contests/Practice/Index/2305#2