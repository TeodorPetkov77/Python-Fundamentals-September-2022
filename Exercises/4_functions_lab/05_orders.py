def total(product, amount):
    result = None
    if product == "coffee":
        result = 1.5 * amount
    elif product == "water":
        result = 1 * amount
    elif product == "coke":
        result = 1.4 * amount
    elif product == "snacks":
        result = 2 * amount
    return result


product_i = input()
amount_i = int(input())

total_price = total(product_i, amount_i)

print(f"{total_price:.2f}")