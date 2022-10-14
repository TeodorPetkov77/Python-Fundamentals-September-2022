command = input()
bakery = {}

while command != "statistics":
    command = command.split(": ")
    key = command[0]
    value = int(command[1])
    if key in bakery:
        bakery[key] += value
    else:
        bakery[key] = value
    command = input()

print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")