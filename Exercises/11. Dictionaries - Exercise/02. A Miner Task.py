resources_dict = {}
last_command = ""
command = input()
line = 0

while command != "stop":
    line += 1
    if line % 2 != 0:
        if command not in resources_dict:
            resources_dict[command] = 0
            last_command = command
            command = input()
            continue
    else:
        resources_dict[last_command] += int(command)
    last_command = command
    command = input()

for key, value in resources_dict.items():
    print(f"{key} -> {value}")