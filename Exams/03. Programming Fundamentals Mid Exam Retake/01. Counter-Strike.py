energy = int(input())
command = input()
won_battles = 0

while command != "End of battle":
    if energy < int(command):
        print(f"Not enough energy! Game ends with {won_battles}"
              f" won battles and {energy} energy")
        break
    else:
        energy -= int(command)
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles
    command = input()
else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")

