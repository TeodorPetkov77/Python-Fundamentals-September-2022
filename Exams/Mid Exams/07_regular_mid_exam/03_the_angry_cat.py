price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()

left_items = []
right_items = []

if type_of_items == "cheap":
    for index in range(entry_point + 1, len(price_ratings)):
        if price_ratings[index] < price_ratings[entry_point]:
            right_items.append(price_ratings[index])
    for index in range(entry_point - 1, -1, -1):
        if price_ratings[index] < price_ratings[entry_point]:
            left_items.append(price_ratings[index])
elif type_of_items == "expensive":
    for index in range(entry_point + 1, len(price_ratings)):
        if price_ratings[index] >= price_ratings[entry_point]:
            right_items.append(price_ratings[index])
    for index in range(entry_point - 1, -1, -1):
        if price_ratings[index] >= price_ratings[entry_point]:
            left_items.append(price_ratings[index])

total_left = sum(left_items)
total_right = sum(right_items)

if total_left > total_right or total_left == total_right:
    print(f"Left - {total_left}")
else:
    print(f"Right - {total_right}")