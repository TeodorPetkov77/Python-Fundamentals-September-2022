cities = {}
command = input()

while command != "Sail":
    command = command.split('||')
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {'population': 0, 'gold': 0}
    cities[city]['population'] += population
    cities[city]['gold'] += gold
    command = input()

command = input()

while command != 'End':
    command = command.split('=>')
    action = command[0]
    town = command[1]
    if action == "Plunder":
        people = int(command[2])
        gold = int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. "
                  f"{town} now has {cities[town]['gold']} gold.")
    command = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, value in cities.items():
        print(f"{key} -> Population: {value['population']} citizens,"
              f" Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")