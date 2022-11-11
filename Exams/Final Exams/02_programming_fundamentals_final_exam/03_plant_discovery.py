plant_rarity_dictionary = {}
n = int(input())

for i in range(n):
    command = input().split('<->')
    plant = command[0]
    rarity = int(command[1])
    if plant not in plant_rarity_dictionary:
        plant_rarity_dictionary[plant] = [{'rarity': 0}, {'rating': [0]}]
    plant_rarity_dictionary[plant][0]['rarity'] = rarity

command = input()

while command != "Exhibition":
    command = command.split(': ')
    action = command[0]
    plant_and_points = command[1].split(' - ')
    plant = plant_and_points[0]
    if action == "Rate":
        points = int(plant_and_points[1])
        if plant in plant_rarity_dictionary:
            if plant_rarity_dictionary[plant][1]['rating'] == [0]:
                plant_rarity_dictionary[plant][1]['rating'] = [points]
            else:
                plant_rarity_dictionary[plant][1]['rating'].append(points)
        else:
            print("error")
    elif action == "Update":
        points = int(plant_and_points[1])
        if plant in plant_rarity_dictionary:
            plant_rarity_dictionary[plant][0]['rarity'] = points
        else:
            print("error")
    elif action == "Reset":
        if plant in plant_rarity_dictionary:
            plant_rarity_dictionary[plant][1]['rating'] = [0]
    command = input()
print("Plants for the exhibition:")
for key, value in plant_rarity_dictionary.items():
    print(f"- {key}; Rarity: {value[0]['rarity']}; "
          f"Rating: {sum(value[1]['rating']) / len(value[1]['rating']):.2f}")