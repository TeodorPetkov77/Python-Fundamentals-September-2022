fire_level = input()
water = int(input())

fire_level_list = fire_level.split("#")
fire_level_list_2 = []
fire_level_list_level = []
fire_level_list_value = []
valid_cells = []

for i in fire_level_list:
    fire_level_list_2.append(i.split(" = "))

for i in fire_level_list_2:
    fire_level_list_level.append(i[0])
    fire_level_list_value.append(int(i[1]))

for i in range(len(fire_level_list)):
    if fire_level_list_level[i] == "High" \
            and 81 <= fire_level_list_value[i] <= 125:
        if water < fire_level_list_value[i]:
            continue
        water -= fire_level_list_value[i]
        valid_cells.append(fire_level_list_value[i])
    elif fire_level_list_level[i] == "Medium" \
            and 51 <= fire_level_list_value[i] <= 80:
        if water < fire_level_list_value[i]:
            continue
        water -= fire_level_list_value[i]
        valid_cells.append(fire_level_list_value[i])
    elif fire_level_list_level[i] == "Low" \
            and 1 <= fire_level_list_value[i] <= 50:
        if water < fire_level_list_value[i]:
            continue
        water -= fire_level_list_value[i]
        valid_cells.append(fire_level_list_value[i])

print("Cells:")
for i in valid_cells:
    print(f"- {i}")
print(f"Effort: {sum(valid_cells) * 0.25:.2f}")
print(f"Total Fire: {sum(valid_cells)}")

# https://judge.softuni.org/Contests/Compete/Index/1725#3