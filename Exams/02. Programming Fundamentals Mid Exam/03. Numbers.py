numbers = list(map(int, input().split(" ")))
numbers_greater = [i for i in numbers if i > sum(numbers) / len(numbers)]
numbers_greater_sorted = sorted(numbers_greater, reverse=True)

if not numbers_greater:
    print("No")
elif len(numbers_greater) > 5:
    for i in range(5):
        print(numbers_greater_sorted[i], end=" ")
else:
    for i in numbers_greater_sorted:
        print(i, end=" ")
