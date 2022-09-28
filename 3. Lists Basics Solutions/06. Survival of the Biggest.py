numbers = input()
numbers_list = numbers.split(" ")
n = int(input())

for j in range(n):
    smallest = 999999999999
    for i in numbers_list:
        if smallest > int(i):
            smallest = int(i)
    for i in range(len(numbers_list) + 1):
        if smallest == int(numbers_list[i]):
            numbers_list.remove(numbers_list[i])
            break

numbers_str = ", ".join(numbers_list)
print(numbers_str)
