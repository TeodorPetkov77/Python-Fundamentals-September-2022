elements = input().split(" ")

bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

products_to_search = input().split(" ")

for search_product in products_to_search:
    if search_product in bakery:
        print(f"We have {bakery[search_product]} of {search_product} left")
    else:
        print(f"Sorry, we don't have {search_product}")