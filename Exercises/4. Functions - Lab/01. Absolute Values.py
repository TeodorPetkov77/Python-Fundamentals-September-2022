numbers_list = input().split(" ")
numbers_list_abs = []

for i in numbers_list:
    numbers_list_abs.append(abs(float(i)))

print(numbers_list_abs)