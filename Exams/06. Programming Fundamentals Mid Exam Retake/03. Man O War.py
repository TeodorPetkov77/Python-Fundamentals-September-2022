pirate_ship_status = list(map(int, input().split(">")))
warship_ship_status = list(map(int, input().split(">")))
maximum_health_capacity = int(input())

command = input()
stale = True

while command != "Retire":
    command = command.split(" ")
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if index in range(len(warship_ship_status)):
            warship_ship_status[index] -= damage
            if warship_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stale = False
                break
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index in range(len(pirate_ship_status)) \
                and end_index in range(len(pirate_ship_status)):
            for index in range(start_index, end_index + 1):
                pirate_ship_status[index] -= damage
                if pirate_ship_status[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stale = False
                    break
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index in range(len(pirate_ship_status)):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > maximum_health_capacity:
                pirate_ship_status[index] = maximum_health_capacity
    elif command[0] == "Status":
        danger_damage = maximum_health_capacity * 0.2
        count = sum(map(lambda x: x < danger_damage, pirate_ship_status))
        print(f"{count} sections need repair.")
    if stale is False:
        break
    command = input()

if stale:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_ship_status)}")
