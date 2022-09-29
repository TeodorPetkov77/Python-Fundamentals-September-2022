budget = float(input())
budget_before = 0
flour_price_kg = float(input())
eggs_price_pack = flour_price_kg * 0.75
milk_price_liter = flour_price_kg * 1.25
loafs = 0
colored_eggs = 0

while True:
    budget_before = budget
    budget -= flour_price_kg + eggs_price_pack + (milk_price_liter * 0.25)
    if budget <= 0:
        break
    loafs += 1
    colored_eggs += 3
    if loafs % 3 == 0:
        colored_eggs -= loafs - 2

print(f"You made {loafs} loaves of Easter bread! "
      f"Now you have {colored_eggs} eggs and {budget_before:.2f}BGN left.")
