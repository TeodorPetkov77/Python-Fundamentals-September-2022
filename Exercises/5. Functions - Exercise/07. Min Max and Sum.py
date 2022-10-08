numbers_list_str = input().split(" ")
numbers_list = []

for i in numbers_list_str:
    numbers_list.append(int(i))

print(f"The minimum number is {min(numbers_list)}")
print(f"The maximum number is {max(numbers_list)}")
print(f"The sum number is: {sum(numbers_list)}")
