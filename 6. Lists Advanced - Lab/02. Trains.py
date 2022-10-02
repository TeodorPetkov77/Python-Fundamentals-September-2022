wagons = int(input())
wagons_list = [0] * wagons
command = input()

while True:
    if command == "End":
        break
    command_list = command.split(" ")
    action = command_list[0]
    if action == "add":
        wagons_list[len(wagons_list) - 1] += int(command_list[1])
    elif action == "insert":
        wagons_list[int(command_list[1])] += int(command_list[2])
    elif action == "leave":
        wagons_list[int(command_list[1])] -= int(command_list[2])
    command = input()

print(wagons_list)