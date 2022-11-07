health = 100
bitcoins = 0

levels = input().split('|')

for index, item in enumerate(levels):
    levels[index] = item.split(" ")

for room_num, room in enumerate(levels):
    if room[0] == "potion":
        health_old = health
        health += int(room[1])
        if health > 100:
            health = 100
        print(f"You healed for {health - health_old} hp.")
        print(f"Current health: {health} hp.")
    elif room[0] == "chest":
        bitcoins += int(room[1])
        print(f"You found {room[1]} bitcoins.")
    else:
        monster = room[0]
        attack = int(room[1])
        health -= attack
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_num + 1}")
            break
        else:
            print(f"You slayed {monster}.")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")