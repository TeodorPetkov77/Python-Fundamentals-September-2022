def tribonacci(number: int):
    sum_list = [1]
    for i in range(number - 1):
        num_to_add = 0
        if len(sum_list) > 3:
            for j in range(len(sum_list) - 1, len(sum_list) - 4, -1):
                num_to_add += sum_list[j]
            sum_list.append(num_to_add)
        else:
            sum_list.append(sum(sum_list))
    print(*sum_list)


tribonacci(int(input()))

# https://judge.softuni.org/Contests/Practice/Index/1729#3

#4.	Tribonacci Sequence
# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting from 1. You will receive a positive integer number as input.
# Examples
# Input	Output		Input	Output
# 4	1 1 2 4
# 		8	1 1 2 4 7 13 24 44
