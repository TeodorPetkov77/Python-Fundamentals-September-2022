numbers_list = input().split(" ")
numbers_list_int = []

for i in numbers_list:
    numbers_list_int.append(int(i))

numbers_filtered = list(filter(lambda x: x % 2 == 0, numbers_list_int))

print(numbers_filtered)
