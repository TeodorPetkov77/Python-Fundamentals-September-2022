people = int(input())
days = int(input())
total_coins = 0

for i in range(1, days + 1):
    is_boss = False
    if i % 15 == 0:
        people += 5
    if i % 10 == 0:
        people -= 2
    total_coins += 50
    total_coins -= 2 * people
    if i % 5 == 0:
        total_coins += 20 * people
        is_boss = True
    if i % 3 == 0:
        if is_boss:
            total_coins -= 5 * people
        else:
            total_coins -= 3 * people

total_coins_per_person = total_coins // people

print(f"{people} companions received {total_coins_per_person} coins each.")