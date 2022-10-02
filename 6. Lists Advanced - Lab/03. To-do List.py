tasks_list = [0] * 10

command = input()

while True:
    if command == "End":
        break
    command_list = command.split("-")
    position = int(command_list[0]) - 1
    task_to_enter = command_list[1]
    tasks_list.pop(position)
    tasks_list.insert(position, task_to_enter)
    command = input()

final_list = [x for x in tasks_list if x != 0]
print(final_list)
