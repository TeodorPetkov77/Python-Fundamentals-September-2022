rows = int(input())
battle_field = []
ships_destroyed = 0

for i in range(rows):
    battle_row = list(map(int, input().split()))
    battle_field.append(battle_row)

attacks = input().split()

for attack in attacks:
    attack_row_col = attack.split("-")
    attack_row = int(attack_row_col[0])
    attack_col = int(attack_row_col[1])
    if battle_field[attack_row][attack_col] > 0:
        battle_field[attack_row][attack_col] -= 1
        if battle_field[attack_row][attack_col] == 0:
            ships_destroyed += 1

print(ships_destroyed)