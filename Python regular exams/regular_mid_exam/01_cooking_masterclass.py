import math

budget = float(input())
students = int(input())
package_flour_price = float(input())
single_egg = float(input())
single_apron = float(input())

total_flours = 0
total_eggs = 0
total_aprons = 0

for items in range(1, students + 1):
    total_flours += 1
    total_eggs += 10
    total_aprons += 1
    if items % 5 == 0:
        total_flours -= 1

total_aprons = math.ceil(total_aprons * 1.2)

total_cost = (total_flours * package_flour_price) + \
             (total_eggs * single_egg) + \
             (total_aprons * single_apron)

if budget >= total_cost:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{abs(budget - total_cost):.2f}$ more needed.")