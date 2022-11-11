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

# https://judge.softuni.org/Contests/Practice/Index/2518#0

# Problem 1 - World Tour
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#0.
#
# You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything first. To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string if it is valid!
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
# •	JavaScript: you will receive a list of strings
# •	An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description
# Examples
# Input	Output
# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel	Hawai::RomeCyprys-Greece
# Hawai::Rome-Greece
# Bulgaria::Rome-Greece
# Ready for world tour! Planned stops: Bulgaria::Rome-Greece
# JS Examples
# Input	Output
# (["Hawai::Cyprys-Greece",
# "Add Stop:7:Rome",
# "Remove Stop:11:16",
# "Switch:Hawai:Bulgaria",
# "Travel"])	Hawai::RomeCyprys-Greece
# Hawai::Rome-Greece
# Bulgaria::Rome-Greece
# Ready for world tour! Planned stops: Bulgaria::Rome-Greece