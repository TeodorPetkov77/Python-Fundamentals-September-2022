treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split(" ")
    if command[0] == "Loot":
        for index in range(1, len(command)):
            if command[index] not in treasure_chest:
                treasure_chest.insert(0, command[index])
    elif command[0] == "Drop":
        if int(command[1]) in range(len(treasure_chest)):
            removed_item = treasure_chest.pop(int(command[1]))
            treasure_chest.append(removed_item)
    elif command[0] == "Steal":
        stolen_count = int(command[1])
        stolen_items = []
        for index in range(len(treasure_chest) - 1,
                           (len(treasure_chest) - stolen_count) - 1, -1):
            stolen_items.insert(0, treasure_chest.pop(index))
            if not treasure_chest:
                break
        print(", ".join(stolen_items))
    command = input()

if treasure_chest:
    treasure_gain = 0
    for item in treasure_chest:
        treasure_gain += len(item)
    treasure_gain = treasure_gain / len(treasure_chest)
    print(f"Average treasure gain: {treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
