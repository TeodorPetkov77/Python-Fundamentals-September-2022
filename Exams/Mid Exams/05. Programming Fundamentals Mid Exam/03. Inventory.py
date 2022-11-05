items = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        if command[1] in items:
            command = input()
            continue
        else:
            items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Combine Items":
        combine_items = command[1].split(":")
        if combine_items[0] in items:
            old_item = combine_items[0]
            new_item = combine_items[1]
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)
    elif command[0] == "Renew":
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])
    command = input()

print(', '.join(items))
