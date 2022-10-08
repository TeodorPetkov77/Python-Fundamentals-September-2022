orders = int(input())
price_per_capsule = 0
days = 0
capsules_per_day = 0
total = 0
total_coffee = 0

for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 \
            or price_per_capsule > 100 \
            or days < 1 \
            or days > 31 \
            or capsules_per_day < 1 \
            or capsules_per_day > 2000:
        continue
    total_coffee = (price_per_capsule * capsules_per_day) * days
    total += total_coffee
    print(f"The price for the coffee is: ${total_coffee:.2f}")

print(f"Total: ${total:.2f}")
