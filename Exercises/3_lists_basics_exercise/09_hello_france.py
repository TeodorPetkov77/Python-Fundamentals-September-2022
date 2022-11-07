items_price = input()
budget = float(input())
item_list = items_price.split("|")
item_list2 = []
prices_list = []
prices_list_before = []

for i in item_list:
    item_list2.append(i.split("->"))

for i in item_list2:
    if i[0] == "Clothes" and float(i[1]) > 50:
        continue
    elif i[0] == "Shoes" and float(i[1]) > 35:
        continue
    elif i[0] == "Accessories" and float(i[1]) > 20.5:
        continue
    if budget < float(i[1]):
        continue
    budget -= float(i[1])
    prices_list_before.append(float(i[1]))
    prices_list.append(float(i[1]) * 1.4)

turnover = sum(prices_list)
profit = turnover - sum(prices_list_before)
total_money = turnover + budget

for i in prices_list:
    print(f"{i:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

# https://judge.softuni.org/Contests/Compete/Index/1725#8