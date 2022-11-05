import re
import math

string = input()
food_pattern = r'([\#\|]{1})([a-zA-Z\s]+)\1' \
               r'([0-3]{1}[1-9]{1})[\/]{1}[0-1]{1}[0-9]{1}[\/]{1}[0-9]{1}[0-9]{1}' \
               r'\1[1-9]+[0-9]{0,4}\1'

food_match = re.finditer(food_pattern, string)
item_date_calo_list = []
food_list = []
best_date_list = []
nurtrition_list = []
total_calo = 0

for i in food_match:
    item_date_calo = i.group()
    if "#" in item_date_calo:
        item_date_calo_list = re.split("#", item_date_calo)
    elif "|" in item_date_calo:
        item_date_calo_list = re.split(r"\|", item_date_calo)
    item_date_calo_list = [i for i in item_date_calo_list if i != ""]
    food_list.append(item_date_calo_list[0])
    best_date_list.append(item_date_calo_list[1])
    nurtrition_list.append(item_date_calo_list[2])
    total_calo += int(item_date_calo_list[2])

print(f"You have food to last you for: {math.floor(total_calo/2000)} days!")
for i in range(len(food_list)):
    print(f"Item: {food_list[i]}, "
          f"Best before: {best_date_list[i]}, "
          f"Nutrition: {nurtrition_list[i]}")

