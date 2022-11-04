numbers = list(map(int, input().split(", ")))

for index in range(len(numbers)-1, -1, -1):
    if numbers[index] == 0:
        numbers.pop(index)
        numbers.append(0)

print(numbers)

# https://judge.softuni.org/Contests/Practice/Index/1726#0

# 1.	Zeros to Back
# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros, and moves them to the back without messing up the other elements. Print the resulting integer list.
# Example
# Input	Output
# 1, 0, 1, 2, 0, 1, 3	[1, 1, 2, 1, 3, 0, 0]
# 0, 5, 0, 4, 0, 0, 5	[5, 4, 5, 0, 0, 0, 0]