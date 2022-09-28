lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_broke = 0
total_expenses = 0

for i in range(1, lost_fights + 1):
    is_helmet_broke = False
    is_sword_broke = False
    if i % 2 == 0:
        total_expenses += helmet_price
        is_helmet_broke = True
    if i % 3 == 0:
        total_expenses += sword_price
        is_sword_broke = True
    if is_helmet_broke and is_sword_broke:
        total_expenses += shield_price
        shield_broke += 1
    if shield_broke % 2 == 0 and shield_broke != 0:
        total_expenses += armor_price
        shield_broke = 0

print(f"Gladiator expenses: {total_expenses:.2f} aureus")