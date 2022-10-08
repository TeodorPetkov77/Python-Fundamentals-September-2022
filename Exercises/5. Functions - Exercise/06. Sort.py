numbers_list_str = input().split(" ")
numbers_list = []

for i in numbers_list_str:
    numbers_list.append(int(i))

sorted_list = sorted(numbers_list)
print(sorted_list)