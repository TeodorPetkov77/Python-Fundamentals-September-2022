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

# https://judge.softuni.org/Contests/Practice/Index/1732#3

# 4.	Battle Ships
# You will be given a number n representing the number of rows of the field. On the following n lines, you will receive each field row as a string with numbers separated by a space. Each number greater than zero represents a ship with health equal to the number value.
# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}". Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1. If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.
# Example
# Input	Output	Comment
# 3
# 1 0 0 1
# 2 0 0 0
# 0 3 0 1
# 0-0 1-0 2-1 2-1 2-1 1-1 2-1	2	States after each attack:
# First attack -> 1 ship destroyed
# 0 0 0 1
# 2 0 0 0
# 0 3 0 1
# Second attack -> reduce ship health
# 0 0 0 1
# 1 0 0 0
# 0 2 0 1
# Third attack -> reduce ship health
# 0 0 0 1
# 2 0 0 0
# 0 2 0 1
# Fourth attack -> reduce ship health
# 0 0 0 1
# 2 0 0 0
# 0 1 0 1
# Fifth attack -> another ship destroyed
# 0 0 0 1
# 2 0 0 0
# 0 0 0 1
# Sixth and Seventh attack -> no ship destroyed
# 5
# 1 0 5 0 1
# 6 3 9 0 0
# 7 9 4 3 2
# 1 0 0 4 9
# 5 6 0 3 5
# 0-1 0-2 0-2 0-2 0-2 0-2 3-0	2