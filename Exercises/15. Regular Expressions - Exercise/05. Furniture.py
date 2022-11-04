import re

command = input()
furniture_names = []
furniture_prices = []
furniture_quantities = []
total = 0
furniture_names_pattern = r"(?<=[>]{2})([A-Za-z]+)(?=[<]{2})"
furniture_prices_pattern = r"(?<=[<]{2})([1-9]*[0-9]+\.?[0-9]*)(?=[!]{1})"
furniture_quantities_pattern = r"(?<=[!]{1})([0-9]+)\b"
valid_pattern = r"([>]{2})([a-zA-Z]+)([<]{2})([1-9]*[0-9]+\.?[0-9]*)([!]{1})([0-9]+)"

while command != "Purchase":
    if re.fullmatch(valid_pattern, command):
        furniture = (re.finditer(furniture_names_pattern, command))
        price = (re.finditer(furniture_prices_pattern, command))
        quantity = (re.finditer(furniture_quantities_pattern, command))
        for i in furniture:
            furniture_names.append(i.group())
        for i in price:
            furniture_prices.append(i.group())
        for i in quantity:
            furniture_quantities.append((i.group()))
    command = input()

for i in range(len(furniture_prices)):
    total += float(furniture_prices[i]) * int(furniture_quantities[i])

print("Bought furniture:")
for i in furniture_names:
    print(i)
print(f"Total money spend: {total:.2f}")

# https://judge.softuni.org/Contests/Compete/Index/1743#4

# 5.	Furniture
# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
# The price could be a floating-point or integer number. You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"
# Examples
# Input	Output	Comment
# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase	Bought furniture:
# Sofa
# TV
# Total money spend: 2436.69	Only the Sofa and the TV are valid, for each of them we multiply the price by the quantity and print the result