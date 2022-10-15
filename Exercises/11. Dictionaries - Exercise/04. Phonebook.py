phonebook = {}
command = input()

while not command.isnumeric():
    command = command.split("-")
    name = command[0]
    number = command[1]
    if name not in phonebook:
        phonebook[name] = ""
    phonebook[name] = command[1]
    command = input()

for i in range(int(command)):
    name_to_search = input()
    if name_to_search not in phonebook:
        print(f"Contact {name_to_search} does not exist.")
    else:
        print(f"{name_to_search} -> {phonebook[name_to_search]}")