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
