quantity = int(input())
days = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_spirit = 5
tree_skirt_spirit = 3
tree_garland_spirit = 10
tree_lights_spirit = 17

total_cost = 0
total_spirit = 0


for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += ornament_set_price * quantity
        total_spirit += ornament_set_spirit
    if i % 3 == 0:
        total_cost += (tree_skirt_price * quantity) + \
                      (tree_garland_price * quantity)
        total_spirit += tree_skirt_spirit + tree_garland_spirit
    if i % 5 == 0:
        total_cost += tree_lights_price * quantity
        total_spirit += tree_lights_spirit
    if i % 3 == 0 and i % 5 == 0:
        total_spirit += 30
    if i % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + \
                      tree_garland_price + \
                      tree_lights_price


if i % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

