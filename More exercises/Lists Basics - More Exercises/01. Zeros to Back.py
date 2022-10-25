numbers = list(map(int, input().split(", ")))

for index in range(len(numbers)-1, -1, -1):
    if numbers[index] == 0:
        numbers.pop(index)
        numbers.append(0)

print(numbers)