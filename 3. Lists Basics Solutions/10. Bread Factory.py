energy = 100
coins = 100
event = input()
event_list = event.split("|")
event_list_final = []
gained_energy = 0
rush_over = False

for i in event_list:
    event_list_final.append(i.split("-"))

for i in event_list_final:
    if i[0] == "rest":
        if (int(i[1]) + energy) > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += int(i[1])
            gained_energy = int(i[1])
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif i[0] == "order":
        if energy < 30:
            print("You had to rest!")
            energy += 50
        else:
            coins += int(i[1])
            energy -= 30
            print(f"You earned {int(i[1])} coins.")
    elif i[0] != "order" and i[0] != "rest":
        if coins < int(i[1]):
            print(f"Closed! Cannot afford {i[0]}.")
            rush_over = True
            break
        else:
            coins -= int(i[1])
            print(f"You bought {i[0]}.")

if rush_over is False:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")