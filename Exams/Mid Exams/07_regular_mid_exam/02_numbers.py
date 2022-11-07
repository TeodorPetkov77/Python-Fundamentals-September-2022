numbers = list(map(int, input().split(" ")))
command = input()

while command != "Finish":
    command = command.split(" ")
    action = command[0]
    value = int(command[1])
    if action == "Add":
        numbers.append(value)
    elif action == "Remove":
        if value in numbers:
            numbers.remove(value)
    elif action == "Replace":
        replacement = int(command[2])
        if value in numbers:
            replace_index = numbers.index(value)
            numbers[replace_index] = replacement
    elif action == "Collapse":
        numbers = [i for i in numbers if i >= value]
    command = input()

print(*numbers, end=" ")

