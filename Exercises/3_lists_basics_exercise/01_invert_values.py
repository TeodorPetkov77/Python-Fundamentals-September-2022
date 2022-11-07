numbers_str = input()
numbers_list = numbers_str.split(" ")
numbers_list_int = []

for i in numbers_list:
    numbers_list_int.append(-int(i))

print(numbers_list_int)

# https://judge.softuni.org/Contests/Compete/Index/1725#0