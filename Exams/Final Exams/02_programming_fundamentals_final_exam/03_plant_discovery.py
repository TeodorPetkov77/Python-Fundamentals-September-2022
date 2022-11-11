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
        else:
            print("error")
    command = input()
print("Plants for the exhibition:")

for key, value in plant_rarity_dictionary.items():
    print(f"- {key}; Rarity: {value[0]['rarity']}; "
          f"Rating: {sum(value[1]['rating']) / len(value[1]['rating']):.2f}")


# https://judge.softuni.org/Contests/Practice/Index/2518#2

# Problem 3 - Plant Discovery
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#2.
#
# You have now returned from your world tour. On your way, you have discovered some new plants, and you want to gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. On the next n lines, you will be given some information about the plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need it later. If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.
# Input / Constraints
# •	You will receive the input as described above
# •	JavaScript: you will receive a list of strings
# Output
# •	Print the information about all plants as described above
# Examples
# Input	Output
# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition	Plants for the exhibition:
# - Arnoldii; Rarity: 4; Rating: 0.00
# - Woodii; Rarity: 5; Rating: 7.50
# - Welwitschia; Rarity: 2; Rating: 7.00
# 2
# Candelabra<->10
# Oahu<->10
# Rate: Oahu - 7
# Rate: Candelabra - 6
# Exhibition	Plants for the exhibition:
# - Candelabra; Rarity: 10; Rating: 6.00
# - Oahu; Rarity: 10; Rating: 7.00
# JS Examples
# Input	Output
# (["3",
# "Arnoldii<->4",
# "Woodii<->7",
# "Welwitschia<->2",
# "Rate: Woodii - 10",
# "Rate: Welwitschia - 7",
# "Rate: Arnoldii - 3",
# "Rate: Woodii - 5",
# "Update: Woodii - 5",
# "Reset: Arnoldii",
# "Exhibition"])	Plants for the exhibition:
# - Arnoldii; Rarity: 4; Rating: 0.00
# - Woodii; Rarity: 5; Rating: 7.50
# - Welwitschia; Rarity: 2; Rating: 7.00
# (["2",
# "Candelabra<->10"
# "Oahu<->10",
# "Rate: Oahu - 7",
# "Rate: Candelabra - 6",
# "Exhibition"])	Plants for the exhibition:
# - Candelabra; Rarity: 10; Rating: 6.00
# - Oahu; Rarity: 10; Rating: 7.00