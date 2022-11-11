def add_stop(index: int, stop: str, string: str):
    result = string[0:index] + stop + string[index:len(string)]
    return result


def remove_stop(index_start: int, index_end: int, string: str):
    result = string[0:index_start] + string[index_end + 1:len(string)]
    return result


stops_input = input()
command = input()

while command != "Travel":
    command = command.split(':')
    if command[0] == "Add Stop":
        index = int(command[1])
        stop = command[2]
        if 0 <= index <= len(stops_input) - 1:
            stops_input = add_stop(index, stop, stops_input)
        print(stops_input)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(stops_input) - 1 and \
                0 <= end_index <= len(stops_input) - 1:
            stops_input = remove_stop(start_index, end_index, stops_input)
        print(stops_input)
    elif command[0] == "Switch":
        old_stop = command[1]
        new_stop = command[2]
        if old_stop in stops_input:
            stops_input = stops_input.replace(old_stop, new_stop)
        print(stops_input)
    command = input()

print(f"Ready for world tour! Planned stops: {stops_input}")
