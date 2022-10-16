command = input()
products = {}

while command != "buy":
    command = command.split(" ")
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in products:
        products[product] = [{"price": 0.0}, {"quantity": 0}]
    products[product][0]["price"] = price
    products[product][1]["quantity"] += quantity
    command = input()

for key, value in products.items():
    print(f"{key} -> {value[0]['price'] * value[1]['quantity']:.2f}")