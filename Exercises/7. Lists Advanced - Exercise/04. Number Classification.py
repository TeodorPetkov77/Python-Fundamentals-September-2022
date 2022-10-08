numbers = list(map(int, input().split(", ")))

numbers_pos = [str(i) for i in numbers if i >= 0]
numbers_neg = [str(i) for i in numbers if i < 0]
numbers_even = [str(i) for i in numbers if i % 2 == 0]
numbers_odd = [str(i) for i in numbers if i % 2 != 0]


print(f"Positive: {', '.join(numbers_pos)}")
print(f"Negative: {', '.join(numbers_neg)}")
print(f"Even: {', '.join(numbers_even)}")
print(f"Odd: {', '.join(numbers_odd)}")

